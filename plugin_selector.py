from __future__ import print_function
import argparse
import os

from argparse import RawTextHelpFormatter

REGRIPPER_PATH = u''
VALID_HIVES = set([])
HIVE_PATH = {}
NTUSER_PATH = {}  # used only when 'multiple' argument is specified
USRCLASS_PATH = {}  # used only when 'multiple' argument is specified


def _validate_input(options):
    global REGRIPPER_PATH
    global VALID_HIVES
    global HIVE_PATH
    global NTUSER_PATH
    global USRCLASS_PATH

    # validate regripper executable
    if options.rr is None:
        print("RegRipper path was not provided.")
        return False
    if not os.path.isfile(os.path.join(options.rr, u'rip.exe')):
        print("Regripper {} does not exist.".format(os.path.join(options.rr, u'rip.exe')))
        return False
    else:
        REGRIPPER_PATH = os.path.join(options.rr, u'rip.exe')

    # validate report directory
    if not os.path.isdir(options.reportdir):
        print("Directory {} does not exist.".format(options.reportdir))
        return False

    # validate system
    if os.path.isfile(os.path.join(options.system, u'SAM')):
        VALID_HIVES.add('sam')
        HIVE_PATH['sam'] = os.path.join(options.system, u'SAM')
    if os.path.isfile(os.path.join(options.system, u'SECURITY')):
        VALID_HIVES.add('security')
        HIVE_PATH['security'] = os.path.join(options.system, u'SECURITY')
    if os.path.isfile(os.path.join(options.system, u'SOFTWARE')):
        VALID_HIVES.add('software')
        HIVE_PATH['software'] = os.path.join(options.system, u'SOFTWARE')
    if os.path.isfile(os.path.join(options.system, u'SYSTEM')):
        VALID_HIVES.add('system')
        HIVE_PATH['system'] = os.path.join(options.system, u'SYSTEM')

    # validate amcache
    if os.path.isfile(os.path.join(options.amcache, u'Amcache.hve')):
        VALID_HIVES.add('amcache')
        HIVE_PATH['amcache'] = os.path.join(options.amcache, u'Amcache.hve')

    # validate ntuser
    if os.path.isfile(os.path.join(options.ntuser, u'NTUSER.DAT')):
        VALID_HIVES.add('ntuser')
        HIVE_PATH['ntuser'] = os.path.join(options.ntuser, u'NTUSER.DAT')

    # validate usrclass
    if os.path.isfile(os.path.join(options.usrclass, u'UsrClass.DAT')):
        VALID_HIVES.add('usrclass')
        HIVE_PATH['usrclass'] = os.path.join(options.usrclass, u'UsrClass.DAT')

    # validate multiple
    if options.multiple is not None:
        subdirs = os.listdir(options.multiple)
        for subdir in subdirs:
            path_ntuser = os.path.join(options.multiple, subdir, u'NTUSER.DAT')
            path_usrclass = os.path.join(options.multiple, subdir, u'UsrClass.DAT')
            if os.path.isfile(path_ntuser):
                VALID_HIVES.add('multiple')
                NTUSER_PATH[os.path.basename(subdir)] = path_ntuser
            if os.path.isfile(path_usrclass):
                VALID_HIVES.add('multiple')
                USRCLASS_PATH[os.path.basename(subdir)] = path_usrclass

    for key in HIVE_PATH:
        HIVE_PATH[key] = '"' + HIVE_PATH[key] + '"'

    if not any(x in ['sam', 'security', 'software', 'system', 'amcache', 'ntuser', 'usrclass', 'multiple']
               for x in VALID_HIVES):
        return False

    return True


def _parse_selection(artifacts):
    supported = {'all', 'os', 'users', 'software', 'network', 'storage', 'device', 'execution', 'autoruns', 'log',
                 'malware', 'web', 'user_config', 'user_act', 'user_network', 'user_file', 'user_virtual', 'comm'}

    selection = artifacts.split(',')
    selection = set(selection)

    # remove unsupported artifacts
    unsupported = set()
    for selected in selection:
        if selected not in supported:
            print("{} artifact is not supported.\n".format(selected))
            unsupported.add(selected)
    selection = selection - unsupported

    # expand 'all'
    if 'all' in selection:
        selection = selection | supported

    # remove 'all'
    selection = selection - {'all'}

    if len(selection) == 0:
        selection = None

    return selection


def get_selection():
    argument_parser = argparse.ArgumentParser(description=(
        'autoripy is an attempt to replicate the functions of auto_rip by Corey Harrell in Python. \n'
        'auto_rip automates the execution of RegRipper according to an examination process. \n'
        'auto_rip is a Copyright of Corey Harrell (jIIr). \n\n'


        'Supported Categories: \n'
        '\t all \t\t gets information from all categories\n'
        '\t os \t\t gets General Operating System Information\n'
        '\t users \t\t gets User Account Information\n'
        '\t software \t gets Installed Software Information\n'
        '\t network \t gets Networking Configuration Information\n'
        '\t storage \t gets Storage Information\n'
        '\t device \t gets Device Information\n'
        '\t execution \t gets Program Execution Information\n'
        '\t autoruns \t gets Autostart Locations Information\n'
        '\t log \t\t gets Logging Information\n'
        '\t malware \t gets Malware Indicators\n'
        '\t web \t\t gets Web Browsing Information\n'
        '\t user_config \t gets User Account Configuration Information\n'
        '\t user_act \t gets User Account General Activity\n'
        '\t user_network \t gets User Account Network Activity\n'
        '\t user_file \t gets User Account File/Folder Access Activity\n'
        '\t user_virtual \t gets User Account Virtualization Access Activity\n'
        '\t comm \t\t Communication Software Information\n\n'


        'Usage: \n'
        '\t Extract all information from the SAM, Security, Software, and System hives.\n'
        '\t autoripy C:\\regripper -s H:\\Windows\\System32\\config -c all\n\n'
        
        '\t Flush all transaction logs + Extract all information from the SAM, Security, Software, and System hives.\n'
        '\t autoripy C:\\regripper -s H:\\Windows\\System32\\config -c all --flush\n\n'

        '\t Extract file access information from NTUSER.DAT and UsrClass.dat hive (Windows 7 profile)\n'
        '\t autoripy C:\\regripper -n H:\\Users\\Corey -u H:\\Users\\Corey\\AppData\\Local\\Microsoft\\Windows '
        '-c user_file\n\n'

        '\t Extract all information from all Windows registry hives without using -c switch.\n'
        '\t autoripy C:\\regripper -s H:\\Windows\\System32\\config -a H:\\Windows\\AppCompat\\Programs '
        '-n H:\\Users\\Corey -u H:\\Users\\Corey\\AppData\\Local\\Microsoft\\Windows\n\n'

        '\t Extract all information from the SAM, Security, Software and System hives, then store output reports '
        'in a specified directory.\n'
        '\t autoripy C:\\regripper -s H:\\Windows\\System32\\config -r C:\\reports\n\n'
        
        '\t Extract all information from the SAM, Security, Software and System hives, NTUSER.DAT and UsrClass.dat '
        'from each user in separate directories, then store output reports in a specified directory.\n'
        '\t autoripy C:\\regripper -s H:\\hives -m H:\\hives\\Users -r C:\\reports'),
        formatter_class=RawTextHelpFormatter)

    argument_parser.add_argument('rr', nargs='?', default=None, help='path to the folder containing RegRipper.')
    argument_parser.add_argument('-s', '--system', default=os.getcwd(), help=(
        'path to the folder containing the SAM, Security, Software, and System hives.'))
    argument_parser.add_argument('-a', '--amcache', default=os.getcwd(), help=(
        'path to the folder containing the Amcache.hve hive.'))
    argument_parser.add_argument('-n', '--ntuser', default=os.getcwd(), help=(
        'path to the folder containing the NTUSER.DAT hive.'))
    argument_parser.add_argument('-u', '--usrclass', default=os.getcwd(), help=(
        'path to the folder containing the UsrClass.dat hive.'))
    argument_parser.add_argument('-m', '--multiple', help=(
        'path to the folder containing multiple <User>\\NTUSER.DAT and/or <User>\\UsrClass.DAT.'))
    argument_parser.add_argument('-r', '--reportdir', default=os.getcwd(), help=(
        'path to the folder to store the output reports.'))
    argument_parser.add_argument('-c', '--cat', default='all', help=(
        'specifies the plugin categories to run. Separate multiple categories with a comma.'))
    argument_parser.add_argument('--flush', action='store_true', help="flush transaction logs.")
    options = argument_parser.parse_args()

    for path in dir(options):
        if not path.startswith('__') and not callable(getattr(options, path)):
            if path not in ('cat', 'flush') and getattr(options, path) is not None:
                setattr(options, path, os.path.abspath(getattr(options, path)))

    if not _validate_input(options):
        return False

    options.cat = _parse_selection(options.cat)
    if options.cat is None:
        return False
    else:
        return options
