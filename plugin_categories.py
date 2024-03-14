"""
<Category> = ["<Category desc>",
                "<report name>",
                [<Sub-Category>, <Hive>, <Plugin>]]
"""

OS = ["General Information about the Operating System and its Configuration",
      u"01_operating_system_information.txt",
      [None, 'software', 'winver'],  # added 2020-08-25
      [None, 'software', 'win_cv'],  # removed in Regripper4.0
      [None, 'security', 'polacdms'],  # removed in Regripper4.0
      [None, 'system', 'processor_architecture'],
      [None, 'system', 'source_os'],  # added 2018-07-15
      [None, 'system', 'producttype'],  # removed in Regripper4.0
      [None, 'system', 'minint'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'wtg'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'productpolicy'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'timezone'],
      [None, 'system', 'timeproviders'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'locale'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'environment'],  # added 2020-08-25
      [None, 'system', 'shutdown'],
      [None, 'system', 'shutdowncount'],  # removed in Regripper4.0
      [None, 'software', 'winlogon'],  # removed in Regripper3.0
      [None, 'software', 'lastloggedon'],  # added 2017-12-22
      [None, 'software', 'autoadminlogon'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'hello'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'disableproxy'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'uac'],
      [None, 'software', 'remoteuac'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'windowsupdate'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'amsiproviders'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'sandbox'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'defender'],  # added 2020-08-25
      [None, 'software', 'networkprotection'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'smartscreen'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'wdfilter'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'lsa'],  # added 2020-08-25
      [None, 'system', 'networkproviders'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'networkproviderservices'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'deviceguard'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'cred'],  # added 2020-08-25
      [None, 'system', 'nolmhash'],  # removed in Regripper4.0
      [None, 'software', 'localdumps'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'credentialsdelegation'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'zerologon'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'trailersupport'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'appmodel'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'diagnostics'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'wsh_settings'],  # added 2018-09-29
      [None, 'software', 'certs'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'certpadding'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'maint'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'disabletools'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'disablesr'],
      [None, 'software', 'storagesense'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'driverinstall'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'installelevated'],  # added in Regripper4.0, added 2024-03-13, dupe of elevatedinstall
      [None, 'software', 'pointandprint'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'ports'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'registerspooler'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'usn'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'volsnap'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'vss'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'pagefile'],
      [None, 'system', 'hibernate'],  # removed in Regripper4.0
      [None, 'system', 'disablelastaccess'],
      [None, 'system', 'backuprestore'],
      [None, 'system', 'disableremotescm'],  # added 2020-08-25
      [None, 'system', 'diag_sr'],  # removed in Regripper3.0
      [None, 'software', 'srum'],  # added 2020-08-25
      [None, 'software', 'clipbrd'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'thumbnail_cleanup'],  # added in Regripper4.0, added 2024-03-13
      [None, 'software', 'spp_clients'],
      [None, 'software', 'winbackup'],  # removed in Regripper4.0
      [None, 'software', 'bitbucket'],  # removed in Regripper3.0
      [None, 'software', 'dfrg'],  # removed in Regripper4.0
      [None, 'software', 'secctr'],
      [None, 'system', 'allow_upgrade'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'labconfig'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'netlogon'],  # added 2019-04-14
      [None, 'system', 'wpbt'],  # added in Regripper4.0, added 2024-03-13
      [None, 'system', 'crashcontrol'],  # removed and replaced by ScanButton 2021-05-03
      [None, 'software', 'regback'],  # removed in Regripper3.0
      [None, 'software', 'ctrlpnl'],  # removed in Regripper4.0
      [None, 'software', 'banner'],  # removed in Regripper4.0
      [None, 'software', 'susclient'],
      [None, 'software', 'gpohist']]

USERS = ["User Account Information",
         u"02_user_account_information.txt",
         [None, 'sam', 'samparse'],
         [None, 'software', 'profilelist'],
         [None, 'software', 'auth'],  # added in Regripper4.0, added 2024-03-13
         [None, 'ntuser', 'userextendedproperties'],  # added in Regripper4.0, added 2024-03-13
         [None, 'ntuser', 'locale'],  # added in Regripper4.0, added 2024-03-13
         [None, 'ntuser', 'nation'],  # added 2018-07-15
         [None, 'ntuser', 'logonstats']]  # added 2018-01-30

SOFTWARE = ["Installed Software Information",
            u"03_installed_software_information.txt",
            [None, 'software', 'updates'],  # removed in Regripper3.0, added 2017-12-22
            [None, 'software', 'uninstall'],
            [None, 'software', 'apppaths'],
            [None, 'software', 'installedcomp'],
            [None, 'software', 'msis'],
            [None, 'software', 'product'],  # removed in Regripper4.0
            [None, 'software', 'installer'],
            [None, 'software', 'installproperties'],  # added in Regripper4.0, added 2024-03-13
            ["Installed Software Settings", 'software', 'execpolicy'],  # added 2018-07-15
            ["Installed Software Settings", 'software', 'feature_block'],  # added in Regripper4.0, added 2024-03-13
            ["Installed Software Settings", 'software', 'powershellcore'],  # added 2020-08-25
            ["Installed Software Settings", 'software', 'disableonedrive'],  # added in Regripper4.0, added 2024-03-13
            ["Installed Software Settings", 'software', 'logmein'],  # removed in Regripper4.0, added 2017-12-22
            ["Installed Software Settings", 'software', 'teamviewer'],  # removed in Regripper3.0, added 2017-12-22
            ["Installed Software Settings", 'software', 'ddpe'],  # removed in Regripper4.0, added 2024-01-28
            ["Installed Software Settings", 'software', 'duo'],  # added in Regripper4.0, added 2024-03-13
            [None, 'software', 'clsid'],
            # [None, 'software', 'assoc'],  # removed in Regripper3.0 (bug)
            # [None, 'usrclass', 'assoc'],  # removed in Regripper3.0, added 2018-01-30 (bug)
            # [None, 'ntuser', 'fileexts'],  # removed in Regripper4.0 (bug)
            [None, 'ntuser', 'appassoc'],  # added 2019-07-06
            [None, 'ntuser', 'apppaths'],  # added 2020-08-25
            [None, 'ntuser', 'listsoft'],
            [None, 'ntuser', 'arpcache'],
            [None, 'ntuser', 'startpage'],  # removed in Regripper4.0
            [None, 'usrclass', 'clsid']]  # added 2020-08-25

NETWORK = ["Networking Configuration Information",
           u"04_network_configuration_information.txt",
           [None, 'system', 'compname'],
           [None, 'system', 'ips'],  # added 2020-08-25
           [None, 'software', 'macaddr'],
           [None, 'software', 'ssid'],
           [None, 'system', 'network'],  # removed in Regripper4.0
           [None, 'system', 'networksetup2'],  # added 2020-08-25
           [None, 'system', 'nic'],  # removed in Regripper4.0
           [None, 'system', 'nic2'],
           [None, 'system', 'routes'],
           [None, 'system', 'sourcerouting'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'tls'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'networklist'],
           [None, 'software', 'networkcards'],
           [None, 'software', 'networkuid'],  # removed in Regripper4.0
           [None, 'software', 'dnsclient'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'shares'],
           [None, 'system', 'smb'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'disable445'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'guestauth'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'fw_config'],  # removed in Regripper4.0
           [None, 'system', 'termserv'],
           [None, 'system', 'termcert'],
           [None, 'system', 'rdpport'],
           [None, 'system', 'rdplockout'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'shadow'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'rdpnla'],  # removed in Regripper4.0, added 2017-12-22
           [None, 'system', 'remoteaccess'],  # added 2017-12-22
           [None, 'system', 'portproxy'],  # added 2024-01-28
           [None, 'system', 'databasepath'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'sql_lastconnect']]  # removed in Regripper4.0

STORAGE = ["Storage information",
           u"05_storage_information.txt",
           [None, 'system', 'mountdev2'],
           [None, 'system', 'fvestats'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'usbdevices'],
           [None, 'system', 'usb'],  # added 2017-12-22
           [None, 'system', 'usbstor'],
           [None, 'system', 'usbstor2'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'automount'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'fsdepends'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'iso'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'devclass'],
           [None, 'system', 'ide'],  # removed in Regripper4.0
           [None, 'system', 'scsi'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'volinfocache'],  # added 2017-12-22
           [None, 'system', 'emdmgmt'],
           [None, 'system', 'wpdbusenum'],
           [None, 'system', 'imagedev'],
           # [None, 'system', 'stillimage'],  # removed in Regripper4.0 (bug)
           [None, 'ntuser', 'mp2'],
           [None, 'ntuser', 'mndmru'],
           [None, 'ntuser', 'knowndev'],
           [None, 'ntuser', 'ddo']]

DEVICE = ["Device Information",
          u"06_device_information.txt",
          [None, 'bcd', 'bcd'],  # added in Regripper4.0, added 2024-03-13
          [None, 'system', 'bthenum'],  # added 2020-08-25
          [None, 'system', 'bthport'],
          [None, 'software', 'btconfig'],
          [None, 'system', 'printer_settings'],  # added in Regripper4.0, added 2024-03-13
          [None, 'software', 'printer_settings'],  # added in Regripper4.0, added 2024-03-13
          [None, 'software', 'audiodev'],
          [None, 'software', 'denydeviceids'],  # added in Regripper4.0, added 2024-03-13
          [None, 'ntuser', 'devicecache']]  # added in Regripper4.0, added 2024-03-13

EXECUTION = ["Program Execution Information",
             u"07_program_execution_information.txt",
             [None, 'system', 'bam'],  # added 2017-03-31
             [None, 'system', 'shimcache'],  # added 2017-12-22
             [None, 'amcache', 'amcache'],
             [None, 'system', 'legacy'],  # removed in Regripper4.0
             [None, 'system', 'prefetch'],
             [None, 'system', 'defrag'],  # added in Regripper4.0, added 2024-03-13
             [None, 'software', 'tracing'],
             [None, 'software', 'direct'],
             [None, 'software', 'heap'],  # added 2020-08-25
             [None, 'software', 'runvirtual'],  # added 2020-08-25
             [None, 'software', 'consentstore'],  # added in Regripper4.0, added 2024-03-13
             [None, 'security', 'secrets'],  # added 2017-12-22
             [None, 'usrclass', 'muicache'],
             [None, 'ntuser', 'userassist'],
             [None, 'ntuser', 'recentapps'],
             [None, 'ntuser', 'featureusage'],  # added 2020-08-25
             # [None, 'ntuser', 'sourcelist'],  # added in Regripper4.0, added 2024-03-13 (bug)
             [None, 'ntuser', 'muicache'],
             [None, 'ntuser', 'mixer'],
             [None, 'ntuser', 'runvirtual'],  # added 2020-08-25
             [None, 'ntuser', 'consentstore'],  # added in Regripper4.0, added 2024-03-13
             [None, 'ntuser', 'appcompatflags'],
             [None, 'ntuser', 'jumplistdata'],  # added 2018-07-15
             [None, 'ntuser', 'heidisql']]  # removed in Regripper4.0, added 2021-05-03

AUTORUNS = ["Autostart Locations Information",
            u"08_autoruns_information.txt",
            ["Run Keys", 'software', 'run'],  # added 2020-08-25
            ["Run Keys", 'software', 'runonceex'],  # added 2020-08-25
            ["Run Keys", 'software', 'rundisabled'],  # added in Regripper4.0, added 2024-03-13
            ["Run Keys", 'software', 'activesetup'],  # added in Regripper4.0, added 2024-03-13
            ["Run Keys", 'system', 'railrunonce'],  # added in Regripper4.0, added 2024-03-13
            ["Run Keys", 'ntuser', 'run'],  # added 2020-08-25
            ["Run Keys", 'ntuser', 'rundisabled'],  # added in Regripper4.0, added 2024-03-13
            ["Run Keys", 'ntuser', 'activesetup'],  # added in Regripper4.0, added 2024-03-13
            ["Services", 'system', 'ntds'],  # added 2020-08-25
            ["Services", 'system', 'services'],
            ["Services", 'system', 'triggerinfo'],  # added in Regripper4.0, added 2024-03-13
            ["Services", 'system', 'svc'],  # removed in Regripper4.0
            ["Services", 'system', 'svcdll'],  # removed in Regripper4.0
            [None, 'software', 'at'],  # removed in Regripper4.0
            [None, 'software', 'appinitdlls'],
            [None, 'software', 'init_dlls'],  # removed in Regripper4.0
            [None, 'software', 'bho'],  # removed in Regripper4.0
            [None, 'software', 'imagefile'],
            [None, 'software', 'winlogon'],  # removed in Regripper4.0
            [None, 'software', 'svchost'],  # removed in Regripper4.0
            [None, 'software', 'drivers32'],  # removed in Regripper4.0
            [None, 'software', 'cmd_shell'],
            [None, 'software', 'shellexec'],  # removed in Regripper4.0
            [None, 'software', 'shellext'],  # removed in Regripper4.0
            [None, 'software', 'schedagent'],
            [None, 'software', 'telemetrycontroller'],  # added in Regripper4.0, added 2024-03-13
            [None, 'software', 'psscript'],  # added 2017-12-22
            [None, 'software', 'silentprocessexit'],  # removed in Regripper3.0, added 2018-06-07
            [None, 'software', 'appkeys'],  # added 2018-09-29
            [None, 'software', 'exefile'],  # removed in Regripper4.0, added 2024-01-28
            [None, 'software', 'appsetup'],  # added in Regripper4.0, added 2024-03-13
            [None, 'software', 'datatracing'],  # added in Regripper4.0, added 2024-03-13
            [None, 'software', 'eventsasp'],  # added in Regripper4.0, added 2024-03-13
            [None, 'software', 'mpnotify'],  # added in Regripper4.0, added 2024-03-13
            [None, 'software', 'recyclepersist'],  # added in Regripper4.0, added 2024-03-13
            [None, 'software', 'office_test'],  # added in Regripper4.0, added 2024-03-13
            [None, 'software', 'update_test'],  # added in Regripper4.0, added 2024-03-13
            [None, 'software', 'outlook_homepage'],  # removed in Regripper4.0, added 2021-05-03
            [None, 'software', 'volumecaches'],  # added in Regripper4.0, added 2024-03-13
            [None, 'system', 'appcertdlls'],
            [None, 'system', 'safeboot'],  # removed in Regripper4.0
            [None, 'system', 'dllsearch'],  # removed in Regripper3.0
            [None, 'system', 'securityproviders'],
            [None, 'system', 'pending'],
            [None, 'system', 'profiler'],
            [None, 'system', 'appenvironment'],  # added in Regripper4.0, added 2024-03-13
            [None, 'system', 'autodialdll'],  # added in Regripper4.0, added 2024-03-13
            [None, 'system', 'coinstallers'],  # added in Regripper4.0, added 2024-03-13
            [None, 'system', 'printprocessors'],  # added in Regripper4.0, added 2024-03-13
            [None, 'system', 'utilities'],  # added in Regripper4.0, added 2024-03-13, dup of tsutilities
            [None, 'ntuser', 'environment'],
            [None, 'ntuser', 'load'],
            [None, 'ntuser', 'winlogon_u'],  # removed in Regripper4.0
            [None, 'ntuser', 'cmdproc'],
            [None, 'ntuser', 'cached'],
            [None, 'ntuser', 'profiler'],
            [None, 'ntuser', 'appkeys'],  # added 2018-09-29
            [None, 'ntuser', 'psscript'],  # added 2020-08-25
            [None, 'ntuser', 'pendinggpos'],  # added 2020-08-25
            [None, 'ntuser', 'office_test'],  # added in Regripper4.0, added 2024-03-13
            [None, 'ntuser', 'outlook_homepage'],  # removed in Regripper4.0, added 2021-05-03
            [None, 'ntuser', 'outlookhomepage'],  # added in Regripper4.0, added 2024-03-13
            [None, 'ntuser', 'outlookmacro'],  # added in Regripper4.0, added 2024-03-13
            [None, 'ntuser', 'screensaver'],  # added in Regripper4.0, added 2024-03-13
            [None, 'usrclass', 'appx'],  # added 2020-08-25
            [None, 'usrclass', 'cmd_shell_u'],  # removed in Regripper4.0
            [None, 'usrclass', 'exefile'],  # removed in Regripper4.0, added 2024-01-28
            [None, 'usrclass', 'recyclepersist']]  # added in Regripper4.0, added 2024-03-13

LOG = ["Logging Information",
       u"09_log_information.txt",
       [None, 'security', 'auditpol'],
       [None, 'security', 'auditpol_xp'],  # removed in Regripper4.0, added 2017-12-22
       [None, 'system', 'disableeventlog'],  # removed in Regripper4.0, added 2024-01-28
       [None, 'system', 'eventlog'],  # removed in Regripper4.0
       [None, 'system', 'eventlogs'],  # removed in Regripper4.0
       [None, 'system', 'auditfail'],  # removed in Regripper4.0
       [None, 'system', 'lsass_auditlevel'],  # added in Regripper4.0, added 2024-03-13
       [None, 'system', 'defenderautologger'],  # added in Regripper4.0, added 2024-03-13
       [None, 'software', 'winevt'],  # removed in Regripper3.0
       [None, 'software', 'winevtchannels'],  # added in Regripper4.0, added 2024-03-13
       [None, 'software', 'eventtranscript'],  # added in Regripper4.0, added 2024-03-13
       [None, 'software', 'installerlogging'],  # added in Regripper4.0, added 2024-03-13
       [None, 'software', 'pslogging'],  # added 2018-12-30
       [None, 'software', 'mrt'],  # removed in Regripper4.0
       [None, 'software', 'drwatson'],  # removed in Regripper4.0
       [None, 'ntuser', 'pslogging']]  # added 2018-12-30

MALWARE = ["Malware Indicators",
           u"10_malware_indicators.txt",
           [None, 'system', 'printmon'],  # added 2020-08-25
           [None, 'system', 'printnightmare'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'netsvcs'],  # removed in Regripper4.0
           [None, 'system', 'kdc'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'tgt'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'perf'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'spooler'],  # added in Regripper4.0, added 2024-03-13
           [None, 'system', 'malware'],  # removed in Regripper4.0, added 2017-12-22
           [None, 'software', 'printdemon'],  # added 2020-08-25
           [None, 'software', 'wrdata'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'inprocserver'],
           [None, 'software', 'wbem'],  # added 2020-08-25
           [None, 'software', 'calibrator'],  # added 2020-08-25
           [None, 'software', 'wab'],  # added 2020-08-25
           [None, 'software', 'uacbypass'],  # added 2020-08-25
           [None, 'software', 'comautoapproval'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'scriptleturl'],  # added 2020-08-25
           [None, 'software', 'injectdll64'],  # added 2020-08-25
           [None, 'software', 'hiddentasks'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'blm'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'symlink'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'enablelinkedconn'],  # added in Regripper4.0, added 2024-03-13
           [None, 'software', 'fileless'],
           [None, 'software', 'malware'],  # removed in Regripper4.0, added 2017-12-22
           [None, 'ntuser', 'injectdll64'],  # added 2020-08-25
           [None, 'ntuser', 'inprocserver'],
           [None, 'ntuser', 'outlook_attach'],  # added in Regripper4.0, added 2024-03-13
           [None, 'ntuser', 'protectedview'],  # added in Regripper4.0, added 2024-03-13
           [None, 'ntuser', 'cpldontload'],  # removed in Regripper4.0
           [None, 'ntuser', 'blm'],  # added in Regripper4.0, added 2024-03-13
           [None, 'ntuser', 'ua_wiper'],  # added in Regripper4.0, added 2024-03-13
           [None, 'ntuser', 'fileless'],
           [None, 'ntuser', 'malware'],  # removed in Regripper4.0, added 2017-12-22
           [None, 'usrclass', 'inprocserver'],
           [None, 'usrclass', 'uacbypass'],  # added 2020-08-25
           [None, 'usrclass', 'scriptleturl'],  # added 2020-08-25
           [None, 'usrclass', 'malware']]  # removed in Regripper4.0, added 2017-12-22

WEB = ["Web Browsing Information",
       u"11_web-browsing_information.txt",
       [None, 'software', 'defbrowser'],  # removed in Regripper4.0
       [None, 'software', 'startmenuinternetapps_lm'],  # removed in Regripper4.0
       [None, 'ntuser', 'startmenuinternetapps_cu'],  # removed in Regripper4.0
       [None, 'ntuser', 'proxysettings'],  # removed in Regripper4.0
       [None, 'ntuser', 'menuorder'],  # removed in Regripper4.0
       ["Internet Explorer Related", 'software', 'ie_version'],  # removed in Regripper4.0
       ["Internet Explorer Related", 'software', 'ie_zones'],  # removed in Regripper4.0
       ["Internet Explorer Related", 'software', 'javasoft'],  # removed in Regripper4.0
       ["Internet Explorer Related", 'software', 'win11_edge'],  # added in Regripper4.0, added 2024-03-13
       ["Internet Explorer Related", 'ntuser', 'ie_settings'],  # removed in Regripper4.0
       ["Internet Explorer Related", 'ntuser', 'internet_settings_cu'],  # removed in Regripper4.0
       ["Internet Explorer Related", 'ntuser', 'internet_explorer_cu'],  # removed in Regripper4.0
       ["Internet Explorer Related", 'ntuser', 'domains'],  # removed in Regripper4.0
       ["Internet Explorer Related", 'ntuser', 'typedurls'],
       ["Internet Explorer Related", 'ntuser', 'typedurlstime'],  # added 2017-12-22
       ["Internet Explorer Related", 'ntuser', 'ie_zones'],   # removed in Regripper4.0
       ["Internet Explorer Related", 'ntuser', 'win11_edge'],  # added in Regripper4.0, added 2024-03-13
       ["Internet Explorer Related", 'usrclass', 'msedge_win10']]  # removed in Regripper4.0, added 2017-12-22

USER_CONFIG = ["User Account Configuration Information",
               u"12_user-configuration_information.txt",
               [None, 'ntuser', 'lxss'],  # added 2020-08-25
               [None, 'ntuser', 'shellfolders'],
               [None, 'ntuser', 'policies_u'],  # removed in Regripper4.0
               [None, 'ntuser', 'userinfo'],  # removed in Regripper4.0
               [None, 'ntuser', 'vista_bitbucket'],  # removed in Regripper4.0
               [None, 'ntuser', 'autorun'],  # removed in Regripper3.0
               [None, 'ntuser', 'attachmgr'],
               [None, 'ntuser', 'autoendtasks'],  # removed in Regripper4.0
               [None, 'ntuser', 'winlogon_u'],  # removed in Regripper3.0
               [None, 'ntuser', 'user_win'],  # removed in Regripper4.0
               [None, 'ntuser', 'location'],  # added in Regripper4.0, added 2024-03-13
               [None, 'ntuser', 'gpohist'],
               [None, 'ntuser', 'installelevated'],  # added in Regripper4.0, added 2024-03-13, dupe of elevatedinstall
               [None, 'ntuser', 'disablemru'],  # added 2018-08-11
               [None, 'ntuser', 'disableuserassist'],  # removed in Regripper4.0, added 2024-01-28
               [None, 'ntuser', 'disabletools'],  # added in Regripper4.0, added 2024-03-13
               [None, 'ntuser', 'bitbucket_user'],  # removed in Regripper4.0, added 2017-12-22
               [None, 'ntuser', 'filehistory'],  # removed in Regripper4.0, added 2017-12-22
               [None, 'ntuser', 'printermru'],  # removed in Regripper4.0, added 2017-12-22
               [None, 'ntuser', 'amsienable'],  # added in Regripper4.0, added 2024-03-13
               [None, 'ntuser', 'certs'],  # added in Regripper4.0, added 2024-03-13
               [None, 'ntuser', 'certpadding'],  # added in Regripper4.0, added 2024-03-13
               [None, 'ntuser', 'clipbrd'],  # added in Regripper4.0, added 2024-03-13
               [None, 'ntuser', 'notif'],  # added in Regripper4.0, added 2024-03-13
               [None, 'ntuser', 'restartmanager'],  # added in Regripper4.0, added 2024-03-13
               [None, 'ntuser', 'storagesense'],  # added in Regripper4.0, added 2024-03-13
               ["User Software Related Information", 'ntuser', 'wordstartup'],  # added in Regripper4.0, added 2024-03-13
               ["User Software Related Information", 'ntuser', 'onedrive'],  # added 2020-08-25
               ["User Software Related Information", 'ntuser', 'onenote'],  # added in Regripper4.0, added 2024-03-13
               ["User Software Related Information", 'ntuser', 'thostperms'],  # added in Regripper4.0, added 2024-03-13
               ["User Software Related Information", 'ntuser', 'ccleaner'],  # removed in Regripper4.0
               ["User Software Related Information", 'ntuser', 'eraser'],  # removed in Regripper4.0, added 2018-07-15
               ["User Software Related Information", 'ntuser', 'sysinternals'],
               ["User Software Related Information", 'ntuser', 'cain'],  # removed in Regripper4.0, added 2017-12-22
               ["User Network Settings Information", 'ntuser', 'logonusername'],  # removed in Regripper4.0
               ["User Network Settings Information", 'ntuser', 'ntusernetwork'],  # removed in Regripper4.0
               ["User Network Settings Information", 'ntuser', 'printers'],  # removed in Regripper4.0
               ["User Network Settings Information", 'ntuser', 'winvnc'],  # removed in Regripper4.0
               ["User Network Settings Information", 'ntuser', 'userlocsvc']]  # removed in Regripper4.0

USER_ACT = ["User Account General Activity",
            u"13_user-account-general-activity.txt",
            [None, 'ntuser', 'typedpaths'],
            [None, 'ntuser', 'wordwheelquery'],
            [None, 'ntuser', 'mmc'],
            [None, 'ntuser', 'runmru'],
            [None, 'ntuser', 'applets'],
            [None, 'ntuser', 'screenshotindex'],  # added in Regripper4.0, added 2024-03-13
            [None, 'ntuser', 'acmru'],  # removed in Regripper4.0
            [None, 'ntuser', 'cortana'],  # removed in Regripper4.0, added 20171222
            [None, 'ntuser', 'link_click'],  # added in Regripper4.0, added 2024-03-13
            [None, 'ntuser', 'doctoidmapping'],  # added in Regripper4.0, added 2024-03-13
            [None, 'ntuser', 'cdstaginginfo'],  # removed in Regripper4.0
            [None, 'ntuser', 'staginginfo'],  # added in Regripper4.0, added 2024-03-13
            [None, 'ntuser', 'gthist']]  # removed in Regripper4.0

USER_NETWORK = ["User Network Activity",
                u"14_user-account-network-activity.txt",
                [None, 'ntuser', 'mndmru'],
                [None, 'ntuser', 'compdesc'],
                [None, 'ntuser', 'tsclient'],
                [None, 'ntuser', 'rdphint'],  # removed in Regripper4.0
                [None, 'ntuser', 'ssh_host_keys'],  # removed in Regripper4.0
                [None, 'ntuser', 'persistconn'],  # added in Regripper4.0, added 2024-03-13
                [None, 'ntuser', 'winscp'],
                [None, 'ntuser', 'winscp_sessions'],  # removed in Regripper4.0
                [None, 'ntuser', 'putty'],  # added 2017-12-22
                [None, 'ntuser', 'putty_sessions'],  # removed in Regripper4.0, added 2017-12-22
                [None, 'ntuser', 'realvnc'],  # removed in Regripper4.0, added 2017-12-22
                [None, 'ntuser', 'vncviewer'],  # removed in Regripper4.0
                [None, 'ntuser', 'vnchooksapplicationprefs']]  # removed in Regripper4.0

USER_FILE = ["User Account File/Folder Access Activity",
             u"15_user-account-file-access-activity.txt",
             [None, 'usrclass', 'shellbags'],
             [None, 'ntuser', 'shellbags'],
             [None, 'ntuser', 'shellbags_xp'],  # removed in Regripper4.0, added 2017-12-22
             [None, 'ntuser', 'itempos'],  # removed in Regripper4.0
             [None, 'ntuser', 'iconlayouts'],  # removed in Regripper4.0, added 2024-01-28
             [None, 'ntuser', 'comdlg32'],
             [None, 'ntuser', 'recentdocs'],
             [None, 'ntuser', 'winzip'],
             [None, 'ntuser', 'winrar'],
             [None, 'ntuser', 'winrar2'],  # removed in Regripper4.0, added 2017-12-22
             [None, 'ntuser', 'sevenzip'],
             [None, 'ntuser', 'mspaper'],  # removed in Regripper4.0
             [None, 'ntuser', 'nero'],  # removed in Regripper4.0
             [None, 'ntuser', 'imgburn1'],  # removed in Regripper3.0
             ["Microsoft Office Files Accessed", 'ntuser', 'msoffice'],  # added 2020-08-25
             ["Microsoft Office Files Accessed", 'ntuser', 'oisc'],
             ["Microsoft Office Files Accessed", 'ntuser', 'snapshot_viewer'],  # removed in Regripper4.0
             ["Microsoft Office Files Accessed", 'ntuser', 'resiliency'],  # added in Regripper4.0, added 2024-03-13
             ["Adobe Files Accessed", 'ntuser', 'adobe'],  # added 2020-08-25
             ["Adobe Files Accessed", 'ntuser', 'foxitrdr'],  # removed in Regripper4.0, added 2017-12-22
             ["Multimedia Files Accessed", 'usrclass', 'photos'],
             ["Multimedia Files Accessed", 'usrclass', 'photos_win10'],  # removed in Regripper4.0, added 2018-07-15
             ["Multimedia Files Accessed", 'ntuser', 'wallpaper'],  # removed in Regripper4.0
             ["Multimedia Files Accessed", 'ntuser', 'mpmru'],
             ["Multimedia Files Accessed", 'ntuser', 'realplayer6']]    # removed in Regripper4.0

USER_VIRTUAL = ["User Account Virtualization Access Activity",
                u"16_user-account-virtual-access.txt",
                [None, 'ntuser', 'vmplayer'],  # removed in Regripper4.0
                [None, 'ntuser', 'vmware_vsphere_client']]  # removed in Regripper4.0

COMM = ["Communication Software Information",
        u"17_communications_information.txt",
        ["Email Communication Information", 'ntuser', 'outlook'],  # removed in Regripper4.0
        ["Email Communication Information", 'ntuser', 'outlook2'],  # removed in Regripper4.0, added 2017-12-22
        ["Email Communication Information", 'ntuser', 'olsearch'],  # removed in Regripper4.0
        ["Email Communication Information", 'ntuser', 'unreadmail'],  # removed in Regripper4.0
        ["Telecommunications Information", 'ntuser', 'skype'],  # removed in Regripper4.0
        ["Messaging Communication Information", 'ntuser', 'improviders'],  # added in Regripper4.0, added 2024-03-13
        ["Messaging Communication Information", 'ntuser', 'liveContactsGUID']]  # removed in Regripper4.0
