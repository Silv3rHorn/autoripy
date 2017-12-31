from __future__ import print_function
import codecs
import logging
import os
import subprocess
import sys

import plugin_categories as pc
import plugin_selector as ps

from datetime import datetime as dt

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

                cmd = u"perl -I. rip.pl -r " + hive_path[plugin[1]] + u' -p ' + plugin[2]
                p = subprocess.Popen(cmd, stdout=outfile, stderr=subprocess.PIPE)
                stderr = p.communicate()
                if stderr:
                    logging.info(stderr[1].rstrip('\r\n'))

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
                print("---- Processing {}'s {} category".format(user, cat))
                logging.info("---- Processing the {}'s {} category".format(user, cat))

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


def main():
    options = ps.get_selection()
    if not options:
        return False

    date_timestamp = dt.now()
    global LOG_FILE
    LOG_FILE = os.path.join(options.reportdir, "_autoripy_log.{}.txt".format(date_timestamp.strftime("%Y-%m-%d@%H%M%S")))
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format=u'%(message)s')

    run_autorip(options)


if __name__ == '__main__':
    if not main():
        sys.exit(1)
    else:
        sys.exit(0)
