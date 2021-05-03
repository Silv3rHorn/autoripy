"""
<Category> = ["<Category desc>",
                "<report name>",
                [<Sub-Category>, <Hive>, <Plugin>]]
"""

OS = ["General Information about the Operating System and its Configuration",
      u"01_operating_system_information.txt",
      [None, 'software', 'winver'],  # added 2020-08-25
      [None, 'software', 'win_cv'],  # removed in Regripper3.0
      [None, 'system', 'source_os'],  # added 2018-07-15
      [None, 'system', 'producttype'],  # removed in Regripper3.0
      [None, 'system', 'timezone'],
      [None, 'system', 'environment'],  # added 2020-08-25
      [None, 'system', 'shutdown'],
      [None, 'system', 'shutdowncount'],  # removed in Regripper3.0
      [None, 'security', 'polacdms'],  # removed in Regripper3.0
      [None, 'software', 'winlogon'],  # removed in Regripper3.0
      [None, 'software', 'lastloggedon'],  # added 2017-12-22
      [None, 'software', 'uac'],
      [None, 'software', 'defender'],  # added 2020-08-25
      [None, 'software', 'disablesr'],
      [None, 'system', 'disableremotescm'],  # added 2020-08-25
      [None, 'system', 'diag_sr'],  # removed in Regripper3.0
      [None, 'system', 'backuprestore'],
      [None, 'software', 'spp_clients'],
      [None, 'software', 'winbackup'],  # removed in Regripper3.0
      [None, 'software', 'bitbucket'],  # removed in Regripper3.0
      [None, 'system', 'disablelastaccess'],
      [None, 'software', 'srum'],  # added 2020-08-25
      [None, 'software', 'dfrg'],  # removed in Regripper3.0
      [None, 'software', 'secctr'],
      [None, 'system', 'pagefile'],
      [None, 'system', 'hibernate'],  # removed in Regripper3.0
      [None, 'system', 'processor_architecture'],
      [None, 'system', 'crashcontrol'],  # removed and replaced by ScanButton 2021-05-03
      [None, 'software', 'regback'],  # removed in Regripper3.0
      [None, 'software', 'ctrlpnl'],  # removed in Regripper3.0
      [None, 'software', 'banner'],  # removed in Regripper3.0
      [None, 'system', 'nolmhash'],  # removed in Regripper3.0
      [None, 'system', 'netlogon'],  # added 2019-04-14
      [None, 'software', 'susclient'],
      [None, 'software', 'gpohist']]

USERS = ["User Account Information",
         u"02_user_account_information.txt",
         [None, 'sam', 'samparse'],
         [None, 'software', 'profilelist'],
         [None, 'ntuser', 'logonstats']]  # added 2018-01-30

SOFTWARE = ["Installed Software Information",
            u"03_installed_software_information.txt",
            [None, 'software', 'updates'],  # removed from Regripper3.0, added 2017-12-22
            [None, 'software', 'uninstall'],
            [None, 'software', 'apppaths'],
            [None, 'software', 'installedcomp'],  # removed in Regripper3.0
            [None, 'software', 'msis'],
            [None, 'software', 'product'],  # removed in Regripper3.0
            [None, 'software', 'installer'],
            ["Installed Software Settings", 'software', 'execpolicy'],  # added 2018-07-15
            ["Installed Software Settings", 'software', 'powershellcore'],  # added 2020-08-25
            ["Installed Software Settings", 'software', 'logmein'],  # removed in Regripper3.0, added 2017-12-22
            ["Installed Software Settings", 'software', 'teamviewer'],  # removed in Regripper3.0, added 2017-12-22
            [None, 'software', 'clsid'],
            # [None, 'software', 'assoc'],  # removed in Regripper3.0 (bug)
            # [None, 'usrclass', 'assoc'],  # removed from Regripper3.0, added 2018-01-30 (bug)
            # [None, 'ntuser', 'fileexts'],  # removed in Regripper3.0 (bug)
            [None, 'ntuser', 'appassoc'],  # added 2019-07-06
            [None, 'ntuser', 'apppaths'],  # added 2020-08-25
            [None, 'ntuser', 'listsoft'],
            [None, 'ntuser', 'arpcache'],
            [None, 'ntuser', 'startpage'],  # removed in Regripper3.0
            [None, 'usrclass', 'clsid']]  # added 2020-08-25

NETWORK = ["Networking Configuration Information",
           u"04_network_configuration_information.txt",
           [None, 'system', 'compname'],
           [None, 'system', 'ips'],  # added 2020-08-25
           [None, 'software', 'macaddr'],
           [None, 'software', 'ssid'],
           [None, 'system', 'network'],  # removed in Regripper3.0
           [None, 'system', 'networksetup2'],  # added 2020-08-25
           [None, 'system', 'nic'],  # removed in Regripper3.0
           [None, 'system', 'nic2'],
           [None, 'system', 'routes'],
           [None, 'software', 'networklist'],
           [None, 'software', 'networkcards'],
           [None, 'software', 'networkuid'],  # removed in Regripper3.0
           [None, 'system', 'shares'],
           [None, 'system', 'fw_config'],  # removed in Regripper3.0
           [None, 'system', 'termserv'],
           [None, 'system', 'termcert'],
           [None, 'system', 'rdpport'],
           [None, 'system', 'rdpnla'],  # removed in Regripper3.0, added 2017-12-22
           [None, 'system', 'remoteaccess'],  # added 2017-12-22
           [None, 'software', 'sql_lastconnect']]  # removed in Regripper3.0

STORAGE = ["Storage information",
           u"05_storage_information.txt",
           [None, 'system', 'mountdev2'],
           [None, 'system', 'usbdevices'],
           [None, 'system', 'usb'],  # added 2017-12-22
           [None, 'system', 'usbstor'],
           [None, 'system', 'devclass'],
           [None, 'system', 'ide'],  # removed in Regripper3.0
           [None, 'software', 'volinfocache'],  # added 2017-12-22
           [None, 'system', 'emdmgmt'],
           [None, 'system', 'wpdbusenum'],
           [None, 'system', 'imagedev'],
           # [None, 'system', 'stillimage'],  # removed in Regripper3.0 (bug)
           [None, 'ntuser', 'mp2'],
           [None, 'ntuser', 'mndmru'],
           [None, 'ntuser', 'knowndev'],
           [None, 'ntuser', 'ddo']]

DEVICE = ["Device Information",
          u"06_device_information.txt",
          [None, 'system', 'bthenum'],  # added 2020-08-25
          [None, 'system', 'bthport'],
          [None, 'software', 'btconfig'],
          [None, 'software', 'audiodev']]

EXECUTION = ["Program Execution Information",
             u"07_program_execution_information.txt",
             [None, 'system', 'bam'],  # added 2017-03-31
             [None, 'system', 'shimcache'],  # added 2017-12-22
             [None, 'amcache', 'amcache'],
             [None, 'system', 'legacy'],  # removed in Regripper3.0
             [None, 'system', 'prefetch'],
             [None, 'software', 'tracing'],
             [None, 'software', 'direct'],
             [None, 'software', 'heap'],  # added 2020-08-25
             [None, 'software', 'runvirtual'],  # added 2020-08-25
             [None, 'security', 'secrets'],  # added 2017-12-22
             [None, 'usrclass', 'muicache'],
             [None, 'ntuser', 'userassist'],
             [None, 'ntuser', 'recentapps'],
             [None, 'ntuser', 'featureusage'],  # added 2020-08-25
             [None, 'ntuser', 'muicache'],
             [None, 'ntuser', 'mixer'],
             [None, 'ntuser', 'runvirtual'],  # added 2020-08-25
             [None, 'ntuser', 'appcompatflags'],
             [None, 'ntuser', 'jumplistdata'],  # added 2018-07-15
             [None, 'ntuser', 'heidisql']]  # added 2021-05-03

AUTORUNS = ["Autostart Locations Information",
            u"08_autoruns_information.txt",
            ["Run Keys", 'software', 'run'],  # added 2020-08-25
            ["Run Keys", 'software', 'runonceex'],  # added 2020-08-25
            ["Run Keys", 'ntuser', 'run'],  # added 2020-08-25
            ["Services", 'system', 'ntds'],  # added 2020-08-25
            ["Services", 'system', 'services'],
            ["Services", 'system', 'svc'],
            ["Services", 'system', 'svcdll'],
            [None, 'software', 'at'],
            [None, 'software', 'appinitdlls'],
            [None, 'software', 'init_dlls'],  # removed in Regripper3.0
            [None, 'software', 'bho'],  # removed in Regripper3.0
            [None, 'software', 'installedcomp'],
            [None, 'software', 'imagefile'],
            [None, 'software', 'winlogon'],  # removed in Regripper3.0
            [None, 'software', 'svchost'],  # removed in Regripper3.0
            [None, 'software', 'drivers32'],
            [None, 'software', 'cmd_shell'],
            [None, 'software', 'shellexec'],  # removed in Regripper3.0
            [None, 'software', 'shellext'],  # removed in Regripper3.0
            [None, 'software', 'schedagent'],
            [None, 'software', 'psscript'],  # added 2017-12-22
            [None, 'software', 'silentprocessexit'],  # removed in Regripper3.0, added 2018-06-07
            [None, 'software', 'appkeys'],  # added 2018-09-29
            [None, 'system', 'appcertdlls'],
            [None, 'system', 'safeboot'],  # removed in Regripper3.0
            [None, 'system', 'dllsearch'],  # removed in Regripper3.0
            [None, 'system', 'securityproviders'],
            [None, 'system', 'profiler'],
            [None, 'ntuser', 'environment'],
            [None, 'ntuser', 'load'],
            [None, 'ntuser', 'winlogon_u'],  # removed in Regripper3.0
            [None, 'ntuser', 'cmdproc'],
            [None, 'ntuser', 'cached'],
            [None, 'ntuser', 'profiler'],
            [None, 'ntuser', 'appkeys'],  # added 2018-09-29
            [None, 'ntuser', 'psscript'],  # added 2020-08-25
            [None, 'ntuser', 'pendinggpos'],  # added 2020-08-25
            [None, 'usrclass', 'appx'],  # added 2020-08-25
            [None, 'usrclass', 'cmd_shell_u']]  # removed in Regripper3.0

LOG = ["Logging Information",
       u"09_log_information.txt",
       [None, 'software', 'mrt'],  # removed in Regripper3.0
       [None, 'security', 'auditpol'],
       [None, 'security', 'auditpol_xp'],  # removed in Regripper3.0, added 2017-12-22
       [None, 'system', 'eventlog'],  # removed in Regripper3.0
       [None, 'system', 'eventlogs'],  # removed in Regripper3.0
       [None, 'software', 'winevt'],  # removed in Regripper3.0
       [None, 'software', 'pslogging'],  # added 2018-12-30
       [None, 'ntuser', 'pslogging'],  # added 2018-12-30
       [None, 'system', 'auditfail'],  # removed in Regripper3.0
       [None, 'software', 'drwatson']]  # removed in Regripper3.0

MALWARE = ["Malware Indicators",
           u"10_malware_indicators.txt",
           [None, 'system', 'cred'],  # added 2020-08-25
           [None, 'system', 'lsa'],  # added 2020-08-25
           [None, 'system', 'printmon'],  # added 2020-08-25
           [None, 'system', 'pending'],
           [None, 'system', 'netsvcs'],  # removed in Regripper3.0
           [None, 'system', 'malware'],  # removed in Regripper3.0, added 2017-12-22
           [None, 'software', 'inprocserver'],
           [None, 'software', 'wbem'],  # added 2020-08-25
           [None, 'software', 'calibrator'],  # added 2020-08-25
           [None, 'software', 'printdemon'],  # added 2020-08-25
           [None, 'software', 'wab'],  # added 2020-08-25
           [None, 'software', 'uacbypass'],  # added 2020-08-25
           [None, 'software', 'fileless'],
           [None, 'software', 'malware'],  # removed in Regripper3.0, added 2017-12-22
           [None, 'software', 'wsh_settings'],  # added 2018-09-29
           [None, 'software', 'scriptleturl'],  # added 2020-08-25
           [None, 'software', 'injectdll64'],  # added 2020-08-25
           [None, 'software', 'outlook_homepage'],  # added 2021-05-03
           [None, 'ntuser', 'outlook_homepage'],  # added 2021-05-03
           [None, 'ntuser', 'injectdll64'],  # added 2020-08-25
           [None, 'ntuser', 'cpldontload'],  # removed in Regripper3.0
           [None, 'ntuser', 'fileless'],
           [None, 'ntuser', 'malware'],  # removed in Regripper3.0, added 2017-12-22
           [None, 'ntuser', 'inprocserver'],
           [None, 'usrclass', 'inprocserver'],
           [None, 'usrclass', 'uacbypass'],  # added 2020-08-25
           [None, 'usrclass', 'scriptleturl'],  # added 2020-08-25
           [None, 'usrclass', 'malware']]  # removed in Regripper3.0, added 2017-12-22

WEB = ["Web Browsing Information",
       u"11_web-browsing_information.txt",
       [None, 'software', 'defbrowser'],  # removed in Regripper3.0
       [None, 'software', 'startmenuinternetapps_lm'],  # removed in Regripper3.0
       [None, 'ntuser', 'startmenuinternetapps_cu'],  # removed in Regripper3.0
       [None, 'ntuser', 'proxysettings'],  # removed in Regripper3.0
       [None, 'ntuser', 'menuorder'],  # removed in Regripper3.0
       ["Internet Explorer Related", 'software', 'ie_version'],  # removed in Regripper3.0
       ["Internet Explorer Related", 'software', 'ie_zones'],  # removed in Regripper3.0
       ["Internet Explorer Related", 'software', 'javasoft'],  # removed in Regripper3.0
       ["Internet Explorer Related", 'ntuser', 'ie_settings'],  # removed in Regripper3.0
       ["Internet Explorer Related", 'ntuser', 'internet_settings_cu'],  # removed in Regripper3.0
       ["Internet Explorer Related", 'ntuser', 'internet_explorer_cu'],  # removed in Regripper3.0
       ["Internet Explorer Related", 'ntuser', 'domains'],  # removed in Regripper3.0
       ["Internet Explorer Related", 'ntuser', 'typedurls'],
       ["Internet Explorer Related", 'ntuser', 'typedurlstime'],  # added 2017-12-22
       ["Internet Explorer Related", 'usrclass', 'msedge_win10'],  # removed in Regripper3.0, added 2017-12-22
       ["Internet Explorer Related", 'ntuser', 'ie_zones']]  # removed in Regripper3.0

USER_CONFIG = ["User Account Configuration Information",
               u"12_user-configuration_information.txt",
               [None, 'ntuser', 'nation'],  # added 2018-07-15
               [None, 'ntuser', 'lxss'],  # added 2020-08-25
               [None, 'ntuser', 'shellfolders'],
               [None, 'ntuser', 'policies_u'],  # removed in Regripper3.0
               [None, 'ntuser', 'userinfo'],  # removed in Regripper3.0
               [None, 'ntuser', 'vista_bitbucket'],  # removed in Regripper3.0
               [None, 'ntuser', 'autorun'],  # removed in Regripper3.0
               [None, 'ntuser', 'attachmgr'],
               [None, 'ntuser', 'autoendtasks'],  # removed in Regripper3.0
               [None, 'ntuser', 'winlogon_u'],  # removed in Regripper3.0
               [None, 'ntuser', 'user_win'],  # removed in Regripper3.0
               [None, 'ntuser', 'gpohist'],
               [None, 'ntuser', 'disablemru'],  # added 2018-08-11
               [None, 'ntuser', 'bitbucket_user'],  # removed in Regripper3.0, added 2017-12-22
               [None, 'ntuser', 'filehistory'],  # removed in Regripper3.0, added 2017-12-22
               [None, 'ntuser', 'printermru'],  # removed in Regripper3.0, added 2017-12-22
               ["User Software Related Information", 'ntuser', 'onedrive'],  # added 2020-08-25
               ["User Software Related Information", 'ntuser', 'ccleaner'],  # removed in Regripper3.0
               ["User Software Related Information", 'ntuser', 'eraser'],  # removed in Regripper3.0, added 2018-07-15
               ["User Software Related Information", 'ntuser', 'sysinternals'],
               ["User Software Related Information", 'ntuser', 'cain'],  # removed in Regripper3.0, added 2017-12-22
               ["User Network Settings Information", 'ntuser', 'logonusername'],  # removed in Regripper3.0
               ["User Network Settings Information", 'ntuser', 'ntusernetwork'],  # removed in Regripper3.0
               ["User Network Settings Information", 'ntuser', 'printers'],  # removed in Regripper3.0
               ["User Network Settings Information", 'ntuser', 'winvnc'],  # removed in Regripper3.0
               ["User Network Settings Information", 'ntuser', 'userlocsvc']]  # removed in Regripper3.0

USER_ACT = ["User Account General Activity",
            u"13_user-account-general-activity.txt",
            [None, 'ntuser', 'typedpaths'],
            [None, 'ntuser', 'wordwheelquery'],
            [None, 'ntuser', 'mmc'],
            [None, 'ntuser', 'runmru'],
            [None, 'ntuser', 'applets'],
            [None, 'ntuser', 'acmru'],  # removed in Regripper3.0
            [None, 'ntuser', 'cortana'],  # removed in Regripper3.0, added 20171222
            [None, 'ntuser', 'cdstaginginfo'],  # removed in Regripper3.0
            [None, 'ntuser', 'gthist']]  # removed in Regripper3.0

USER_NETWORK = ["User Network Activity",
                u"14_user-account-network-activity.txt",
                [None, 'ntuser', 'mndmru'],
                [None, 'ntuser', 'compdesc'],
                [None, 'ntuser', 'tsclient'],
                [None, 'ntuser', 'rdphint'],  # removed in Regripper3.0
                [None, 'ntuser', 'ssh_host_keys'],  # removed in Regripper3.0
                [None, 'ntuser', 'winscp'],
                [None, 'ntuser', 'winscp_sessions'],  # removed in Regripper3.0
                [None, 'ntuser', 'putty'],  # added 2017-12-22
                [None, 'ntuser', 'putty_sessions'],  # removed in Regripper3.0, added 2017-12-22
                [None, 'ntuser', 'realvnc'],  # removed in Regripper3.0, added 2017-12-22
                [None, 'ntuser', 'vncviewer'],  # removed in Regripper3.0
                [None, 'ntuser', 'vnchooksapplicationprefs']]  # removed in Regripper3.0

USER_FILE = ["User Account File/Folder Access Activity",
             u"15_user-account-file-access-activity.txt",
             [None, 'usrclass', 'shellbags'],
             [None, 'ntuser', 'shellbags'],
             [None, 'ntuser', 'shellbags_xp'],  # removed in Regripper3.0, added 2017-12-22
             [None, 'ntuser', 'itempos'],  # removed in Regripper3.0
             [None, 'ntuser', 'comdlg32'],
             [None, 'ntuser', 'recentdocs'],
             [None, 'ntuser', 'winzip'],
             [None, 'ntuser', 'winrar'],
             [None, 'ntuser', 'winrar2'],  # removed in Regripper3.0, added 2017-12-22
             [None, 'ntuser', 'sevenzip'],
             [None, 'ntuser', 'mspaper'],  # removed in Regripper3.0
             [None, 'ntuser', 'nero'],  # removed in Regripper3.0
             [None, 'ntuser', 'imgburn1'],  # removed in Regripper3.0
             ["Microsoft Office Files Accessed", 'ntuser', 'msoffice'],  # added 2020-08-25
             ["Microsoft Office Files Accessed", 'ntuser', 'oisc'],
             ["Microsoft Office Files Accessed", 'ntuser', 'snapshot_viewer'],  # removed in Regripper3.0
             ["Adobe Files Accessed", 'ntuser', 'adobe'],  # added 2020-08-25
             ["Adobe Files Accessed", 'ntuser', 'foxitrdr'],  # removed in Regripper3.0, added 2017-12-22
             ["Multimedia Files Accessed", 'usrclass', 'photos'],
             ["Multimedia Files Accessed", 'usrclass', 'photos_win10'],  # removed in Regripper3.0, added 2018-07-15
             ["Multimedia Files Accessed", 'ntuser', 'wallpaper'],  # removed in Regripper3.0
             ["Multimedia Files Accessed", 'ntuser', 'mpmru'],
             ["Multimedia Files Accessed", 'ntuser', 'realplayer6']]    # removed in Regripper3.0

USER_VIRTUAL = ["User Account Virtualization Access Activity",
                u"16_user-account-virtual-access.txt",
                [None, 'ntuser', 'vmplayer'],  # removed in Regripper3.0
                [None, 'ntuser', 'vmware_vsphere_client']]  # removed in Regripper3.0

COMM = ["Communication Software Information",
        u"17_communications_information.txt",
        ["Email Communication Information", 'ntuser', 'outlook'],  # removed in Regripper3.0
        ["Email Communication Information", 'ntuser', 'outlook2'],  # removed in Regripper3.0, added 2017-12-22
        ["Email Communication Information", 'ntuser', 'olsearch'],  # removed in Regripper3.0
        ["Email Communication Information", 'ntuser', 'unreadmail'],  # removed in Regripper3.0
        ["Telecommunications Information", 'ntuser', 'skype'],  # removed in Regripper3.0
        ["Messaging Communication Information", 'ntuser', 'liveContactsGUID']]  # removed in Regripper3.0
