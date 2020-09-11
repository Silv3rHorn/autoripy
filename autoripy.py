from __future__ import print_function
import codecs
import logging
import os
import subprocess
import sys

import plugin_categories as pc
import plugin_selector as ps

from datetime import datetime as dt
from yarp import Registry
from yarp.RegistryFile import HiveBinException

LOG_FILE = ''


def _run_regripper(cat, valid_hives, report_file, hive_path=ps.HIVE_PATH):
    has_output = False
    with codecs.open(report_file, 'w', encoding='utf-8') as outfile:
        # Write report file header
        outfile.write(u'=' * 105 + u'\r\n')
        outfile.write(getattr(pc, cat)[0] + u'\r\n')
        outfile.write(u'=' * 105 + u'\r\n\r\n')
        outfile.flush()

        sub_cat = ''
        plugins = getattr(pc, cat)[2:]
        for plugin in plugins:
            if plugin[1] in valid_hives:
                has_output = True
                # print sub-category
                if plugin[0] is not None and plugin[0] != sub_cat:
                    outfile.write(u'+' * 10 + ' ' + plugin[0] + u' ' + u'+' * 10)
                    outfile.write(u'\r\n+\r\n')
                    outfile.flush()
                sub_cat = plugin[0]

                # cmd = u"perl -I. rip.pl -r " + hive_path[plugin[1]] + u' -p ' + plugin[2]
                cmd = u"rip.exe -r " + hive_path[plugin[1]] + u' -p ' + plugin[2]
                p = subprocess.Popen(cmd, stdout=outfile, stderr=subprocess.PIPE)
                stderr = p.communicate()[1].decode('utf-8')
                if stderr:
                    logging.info('\t' + stderr.rstrip('\r\n'))

                outfile.write(u'.' * 107)
                outfile.write(u'\r\n.\r\n')
                outfile.flush()

    if not has_output:
        os.remove(report_file)


def run_autorip(options):
    os.chdir(os.path.dirname(ps.REGRIPPER_PATH))

    options.cat = [cat.upper() for cat in options.cat]
    for cat in options.cat:
        print("---- Processing the {} category".format(cat))
        logging.info("---- Processing the {} category".format(cat))

        valid_hives = ps.VALID_HIVES
        report_file = os.path.join(options.reportdir, getattr(pc, cat)[1])
        _run_regripper(cat, valid_hives, report_file)

    if 'multiple' in ps.VALID_HIVES:
        users = set(ps.NTUSER_PATH.keys()) | set(ps.USRCLASS_PATH.keys())  # merge keys in two dicts
        for user in users:
            for cat in options.cat:
                print("---- Processing {0}'s {1} category".format(user, cat))
                logging.info("---- Processing the {0}'s {1} category".format(user, cat))

                # create output dir
                if not os.path.isdir(os.path.join(options.reportdir, user)):
                    os.makedirs(os.path.join(options.reportdir, user))

                valid_hives = []
                hive_path = {}
                if user in ps.NTUSER_PATH:
                    valid_hives.append('ntuser')
                    hive_path['ntuser'] = ps.NTUSER_PATH[user]
                if user in ps.USRCLASS_PATH:
                    valid_hives.append('usrclass')
                    hive_path['usrclass'] = ps.USRCLASS_PATH[user]

                report_file = os.path.join(options.reportdir, user, getattr(pc, cat)[1])
                _run_regripper(cat, valid_hives, report_file, hive_path)


def _flush(path):
    log_paths = list()
    log_paths.append(path + '.LOG')
    log_paths.append(path + '.LOG1')
    log_paths.append(path + '.LOG2')

    # check if each transaction log exists
    for idx in range(len(log_paths)):
        if not os.path.isfile(log_paths[idx]):
            log_paths[idx] = None

    # if log path is invalid or no transaction logs at log path exists
    if log_paths[0] is None and log_paths[1] is None and log_paths[2] is None:
        print("Flush failed (no logs)        - {}".format(path))
        logging.info("Flush failed (no logs)        - {}".format(path))
        return 1

    with open(path, 'rb') as hive:
        log = []
        try:
            yarp_hive = Registry.RegistryHive(hive)

            for log_path in log_paths:
                if log_path is None:
                    log.append(None)
                else:
                    log.append(open(log_path, 'rb'))

            result = yarp_hive.recover_auto(log[0], log[1], log[2])
        except HiveBinException as e:
            error_msg = e
            result = None

    if result is None:
        print("Flush failed (HiveBinException: {0}) - {1}".format(error_msg, path))
        logging.info("Flush failed (HiveBinException: {0}) - {1}".format(error_msg, path))
    elif result.recovered:
        print("Flush successful              - {}".format(path))
        logging.info("Flush successful              - {}".format(path))
        outfile = os.path.join(path)
        os.rename(outfile, outfile + '.old')  # backup original file
        yarp_hive.save_recovered_hive(outfile)
    elif result.is_new_log is None:
        print("Flush failed (no new data)    - {}".format(path))
        logging.info("Flush failed (no new data) - {}".format(path))
    elif not result.recovered:
        print("Flush failed (unknown reason) - {}".format(path))
        logging.info("Flush failed (unknown reason) - {}".format(path))

    for file in log:
        if file is not None:
            file.close()


def run_flush():
    print('\n')
    logging.info('\n')

    for key, path in ps.HIVE_PATH.items():
        _flush(path.replace('"', ''))

    for key, path in ps.NTUSER_PATH.items():
        _flush(path.replace('"', ''))

    for key, path in ps.USRCLASS_PATH.items():
        _flush(path.replace('"', ''))

    print('\n')
    logging.info('\n')


def main():
    options = ps.get_selection()
    if not options:
        return False

    date_timestamp = dt.now()

    global LOG_FILE
    LOG_FILE = os.path.join(options.reportdir, "_autoripy_log.{}.txt".format(date_timestamp.strftime("%Y-%m-%d@%H%M%S")))
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format=u'%(message)s')

    for arg in dir(options):
        if not arg.startswith('__') and not callable(getattr(options, arg)):
            logging.info(u"{0}:\t{1}".format(arg, getattr(options, arg)))

    if options.flush:
        run_flush()

    run_autorip(options)


if __name__ == '__main__':
    if not main():
        sys.exit(1)
    else:
        sys.exit(0)
