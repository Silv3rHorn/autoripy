"""
<Category> = ["<Category desc>",
                "<report name>",
                [<Sub-Category>, <Hive>, <Plugin>]]
"""

OS = ["General Information about the Operating System and its Configuration",
      u"01_operating_system_information.txt",
      [None, 'software', 'winnt_cv'],
      [None, 'system', 'producttype'],
      [None, 'software', 'win_cv'],  # fixed bug 2017-22-31 (system -> software)
      [None, 'system', 'timezone'],
      [None, 'system', 'shutdown'],
      [None, 'system', 'shutdowncount'],
      [None, 'security', 'polacdms'],
      [None, 'software', 'winlogon'],
      [None, 'software', 'lastloggedon'],  # added 2017-12-22
      [None, 'software', 'uac'],
      [None, 'software', 'disablesr'],
      [None, 'system', 'diag_sr'],  # fixed bug 2017-22-31 (software -> system)
      [None, 'software', 'spp_clients'],
      [None, 'system', 'backuprestore'],
      [None, 'software', 'winbackup'],
      [None, 'software', 'bitbucket'],
      [None, 'system', 'disablelastaccess'],
      [None, 'software', 'dfrg'],  # fixed bug 2017-22-31 (system -> software)
      [None, 'software', 'secctr'],
      [None, 'system', 'pagefile'],
      [None, 'system', 'hibernate'],
      [None, 'system', 'processor_architecture'],
      [None, 'system', 'crashcontrol'],
      [None, 'software', 'regback'],
      [None, 'software', 'ctrlpnl'],
      [None, 'software', 'banner'],
      [None, 'system', 'nolmhash'],
      [None, 'software', 'susclient'],
      [None, 'software', 'gpohist']]

USERS = ["User Account Information",
         u"02_user_account_information.txt",
         [None, 'sam', 'samparse'],
         [None, 'software', 'profilelist']]

SOFTWARE = ["Installed Software Information",
            u"03_installed_software_information.txt",
            [None, 'software', 'updates'],  # added 2017-12-22
            [None, 'software', 'uninstall'],
            [None, 'software', 'apppaths'],
            [None, 'software', 'assoc'],
            [None, 'software', 'installedcomp'],
            [None, 'software', 'msis'],
            [None, 'software', 'product'],
            [None, 'software', 'installer'],
            [None, 'software', 'clsid'],
            [None, 'ntuser', 'listsoft'],
            [None, 'ntuser', 'fileexts'],
            [None, 'ntuser', 'arpcache'],
            [None, 'ntuser', 'startpage']]

NETWORK = ["Networking Configuration Information",
           u"04_network_configuration_information.txt",
           [None, 'system', 'compname'],
           [None, 'software', 'networkcards'],
           [None, 'system', 'nic'],
           [None, 'system', 'nic2'],
           [None, 'software', 'macaddr'],
           [None, 'system', 'shares'],
           [None, 'system', 'fw_config'],
           [None, 'system', 'routes'],
           [None, 'software', 'networklist'],
           [None, 'software', 'ssid'],
           [None, 'software', 'networkuid'],
           [None, 'system', 'network'],
           [None, 'system', 'termserv'],
           [None, 'system', 'termcert'],
           [None, 'system', 'rdpport'],
           [None, 'system', 'rdpnla'],  # added 2017-12-22
           [None, 'system', 'remoteaccess'],  # added 2017-12-22
           [None, 'software', 'sql_lastconnect']]

STORAGE = ["Storage information",
           u"05_storage_information.txt",
           [None, 'system', 'mountdev2'],
           [None, 'system', 'ide'],
           [None, 'system', 'usbdevices'],
           [None, 'system', 'usb'],  # added 2017-12-22
           [None, 'system', 'usbstor'],
           [None, 'system', 'devclass'],
           [None, 'software', 'volinfocache'],  # added 2017-12-22
           [None, 'system', 'emdmgmt'],
           [None, 'system', 'wpdbusenum'],
           [None, 'system', 'bthport'],
           [None, 'software', 'btconfig'],  # fixed bug 2017-22-31 (system -> software)
           [None, 'system', 'imagedev'],
           [None, 'system', 'stillimage'],
           [None, 'ntuser', 'mp2'],
           [None, 'ntuser', 'mndmru'],
           [None, 'ntuser', 'knowndev'],
           [None, 'ntuser', 'ddo']]

DEVICE = ["Device Information",
          u"06_device_information.txt",
          [None, 'software', 'audiodev']]

EXECUTION = ["Program Execution Information",
             u"07_program_execution_information.txt",
             [None, 'system', 'prefetch'],
             # [None, 'system', 'appcompatcache'],  # removed 2017-12-22 (does not parse all controlsets)
             [None, 'system', 'shimcache'],  # added 2017-12-22
             [None, 'system', 'legacy'],
             [None, 'software', 'tracing'],
             [None, 'software', 'at'],
             [None, 'software', 'direct'],
             [None, 'software', 'logmein'],  # added 2017-12-22
             [None, 'software', 'teamviewer'],  # added 2017-12-22
             [None, 'security', 'secrets'],  # added 2017-12-22
             [None, 'amcache', 'amcache'],
             [None, 'usrclass', 'muicache'],
             [None, 'ntuser', 'muicache'],
             [None, 'ntuser', 'userassist'],
             [None, 'ntuser', 'appcompatflags'],
             [None, 'ntuser', 'recentapps'],
             [None, 'ntuser', 'cain'],  # added 2017-12-22
             [None, 'ntuser', 'mixer']]

AUTORUNS = ["Autostart Locations Information",
            u"08_autoruns_information.txt",
            ["Run Keys", 'software', 'soft_run'],
            ["Run Keys", 'ntuser', 'user_run'],
            ["Services", 'system', 'services'],
            ["Services", 'system', 'svc'],
            ["Services", 'system', 'svcdll'],
            [None, 'software', 'appinitdlls'],
            [None, 'software', 'init_dlls'],
            [None, 'software', 'bho'],
            [None, 'software', 'installedcomp'],
            [None, 'software', 'imagefile'],
            [None, 'software', 'winlogon'],
            [None, 'software', 'svchost'],
            [None, 'software', 'drivers32'],
            [None, 'software', 'cmd_shell'],
            [None, 'software', 'shellexec'],
            [None, 'software', 'shellext'],
            [None, 'software', 'schedagent'],
            [None, 'software', 'psscript'],  # added 2017-12-22
            [None, 'system', 'appcertdlls'],
            [None, 'system', 'lsa_packages'],
            [None, 'system', 'safeboot'],
            [None, 'system', 'dllsearch'],
            [None, 'system', 'securityproviders'],
            [None, 'system', 'profiler'],
            [None, 'ntuser', 'load'],
            [None, 'ntuser', 'winlogon_u'],
            [None, 'ntuser', 'cmdproc'],
            [None, 'ntuser', 'startup'],
            [None, 'ntuser', 'cached'],
            [None, 'ntuser', 'profiler'],
            [None, 'usrclass', 'cmd_shell_u']]

LOG = ["Logging Information",
       u"09_log_information.txt",
       [None, 'software', 'mrt'],
       [None, 'security', 'auditpol'],
       [None, 'security', 'auditpol_xp'],  # added 2017-12-22
       [None, 'system', 'eventlog'],
       [None, 'system', 'eventlogs'],
       [None, 'software', 'winevt'],
       [None, 'system', 'auditfail'],
       [None, 'software', 'drwatson']]

MALWARE = ["Malware Indicators",
           u"10_malware_indicators.txt",
           [None, 'system', 'pending'],
           [None, 'system', 'netsvcs'],
           [None, 'system', 'malware'],  # added 2017-12-22
           [None, 'software', 'inprocserver'],
           [None, 'software', 'fileless'],
           [None, 'software', 'malware'],  # added 2017-12-22
           [None, 'ntuser', 'cpldontload'],
           [None, 'ntuser', 'fileless'],
           [None, 'ntuser', 'malware'],  # added 2017-12-22
           [None, 'ntuser', 'inprocserver'],
           [None, 'usrclass', 'inprocserver'],
           [None, 'usrclass', 'malware']]  # added 2017-12-22

WEB = ["Web Browsing Information",
       u"11_web-browsing_information.txt",
       [None, 'software', 'defbrowser'],
       [None, 'software', 'startmenuinternetapps_lm'],
       ["Internet Explorer Related", 'software', 'ie_version'],
       ["Internet Explorer Related", 'software', 'ie_zones'],
       ["Internet Explorer Related", 'software', 'javasoft'],
       [None, 'ntuser', 'startmenuinternetapps_cu'],
       [None, 'ntuser', 'proxysettings'],
       [None, 'ntuser', 'menuorder'],
       ["Internet Explorer Related", 'ntuser', 'ie_settings'],
       ["Internet Explorer Related", 'ntuser', 'internet_settings_cu'],
       ["Internet Explorer Related", 'ntuser', 'internet_explorer_cu'],
       ["Internet Explorer Related", 'ntuser', 'domains'],
       ["Internet Explorer Related", 'ntuser', 'typedurls'],
       ["Internet Explorer Related", 'ntuser', 'typedurlstime'],  # added 2017-12-22
       ["Internet Explorer Related", 'ntuser', 'ie_zones']]

USER_CONFIG = ["User Account Configuration Information",
               u"12_user-configuration_information.txt",
               [None, 'ntuser', 'shellfolders'],
               [None, 'ntuser', 'policies_u'],
               [None, 'ntuser', 'environment'],
               [None, 'ntuser', 'userinfo'],
               [None, 'ntuser', 'vista_bitbucket'],
               [None, 'ntuser', 'autorun'],
               [None, 'ntuser', 'attachmgr'],
               [None, 'ntuser', 'autoendtasks'],
               [None, 'ntuser', 'winlogon_u'],
               [None, 'ntuser', 'user_win'],
               [None, 'ntuser', 'gpohist'],
               [None, 'ntuser', 'bitbucket_user'],  # added 2017-12-22
               [None, 'ntuser', 'filehistory'],  # added 2017-12-22
               [None, 'ntuser', 'printermru'],  # added 2017-12-22
               ["User Software Related Information", 'ntuser', 'ccleaner'],
               ["User Software Related Information", 'ntuser', 'sysinternals'],
               ["User Network Settings Information", 'ntuser', 'logonusername'],
               ["User Network Settings Information", 'ntuser', 'ntusernetwork'],
               ["User Network Settings Information", 'ntuser', 'printers'],
               ["User Network Settings Information", 'ntuser', 'winvnc'],
               ["User Network Settings Information", 'ntuser', 'userlocsvc']]

USER_ACT = ["User Account General Activity",
            u"13_user-account-general-activity.txt",
            [None, 'ntuser', 'typedpaths'],
            [None, 'ntuser', 'mmc'],
            [None, 'ntuser', 'runmru'],
            [None, 'ntuser', 'applets'],
            [None, 'ntuser', 'acmru'],
            [None, 'ntuser', 'cortana'],  # added 20171222
            [None, 'ntuser', 'wordwheelquery'],
            [None, 'ntuser', 'cdstaginginfo'],
            [None, 'ntuser', 'gthist']]

USER_NETWORK = ["User Network Activity",
                u"14_user-account-network-activity.txt",
                [None, 'ntuser', 'mndmru'],
                [None, 'ntuser', 'compdesc'],
                [None, 'ntuser', 'tsclient'],
                [None, 'ntuser', 'rdphint'],
                [None, 'ntuser', 'ssh_host_keys'],
                [None, 'ntuser', 'winscp'],
                [None, 'ntuser', 'winscp_sessions'],
                [None, 'ntuser', 'putty'],  # added 2017-12-22
                [None, 'ntuser', 'putty_sessions'],  # added 2017-12-22
                [None, 'ntuser', 'realvnc'],  # added 2017-12-22
                [None, 'ntuser', 'vncviewer'],
                [None, 'ntuser', 'vnchooksapplicationprefs']]

USER_FILE = ["User Account File/Folder Access Activity",
             u"15_user-account-file-access-activity.txt",
             [None, 'usrclass', 'shellbags'],
             [None, 'ntuser', 'shellbags'],
             [None, 'ntuser', 'shellbags_xp'],  # added 20171222
             [None, 'ntuser', 'itempos'],
             [None, 'ntuser', 'comdlg32'],
             [None, 'ntuser', 'recentdocs'],
             [None, 'ntuser', 'winzip'],
             # [None, 'ntuser', 'winrar'],  # removed 20171222 (winrar2 is more updated)
             [None, 'ntuser', 'winrar2'],  # added 20171222
             [None, 'ntuser', 'sevenzip'],
             [None, 'ntuser', 'mspaper'],
             [None, 'ntuser', 'nero'],
             [None, 'usrclass', 'photos'],
             ["Microsoft Office Files Accessed", 'ntuser', 'officedocs'],
             ["Microsoft Office Files Accessed", 'ntuser', 'officedocs2010'],
             ["Microsoft Office Files Accessed", 'ntuser', 'reading_locations'],
             ["Microsoft Office Files Accessed", 'ntuser', 'oisc'],
             ["Microsoft Office Files Accessed", 'ntuser', 'trustrecords'],
             ["Microsoft Office Files Accessed", 'ntuser', 'snapshot_viewer'],
             ["Adobe Files Accessed", 'ntuser', 'adoberdr'],
             ["Adobe Files Accessed", 'ntuser', "Adobe Files Accessed", 'foxitrdr'],  # added 20171222
             ["Multimedia Files Accessed", 'ntuser', 'wallpaper'],
             ["Multimedia Files Accessed", 'ntuser', 'mpmru'],
             ["Multimedia Files Accessed", 'ntuser', 'realplayer6']]

USER_VIRTUAL = ["User Account Virtualization Access Activity",
                u"16_user-account-virtual-access.txt",
                [None, 'ntuser', 'vmplayer'],
                [None, 'ntuser', 'vmware_vsphere_client']]

COMM = ["Communication Software Information",
        u"17_communications_information.txt",
        ["Email Communication Information", 'ntuser', 'outlook'],
        ["Email Communication Information", 'ntuser', 'outlook2'],  # added 20171222
        ["Email Communication Information", 'ntuser', 'olsearch'],
        ["Email Communication Information", 'ntuser', 'unreadmail'],
        ["Telecommunications Information", 'ntuser', 'skype'],
        ["Messaging Communication Information", 'ntuser', 'aim'],
        ["Messaging Communication Information", 'ntuser', 'liveContactsGUID'],
        ["Messaging Communication Information", 'ntuser', 'yahoo_lm'],  # added 20171222
        ["Messaging Communication Information", 'ntuser', 'yahoo_cu']]
