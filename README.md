# autoripy
![](https://img.shields.io/badge/python-3-blue.svg)

autoripy is an attempt to replicate the functions of auto_rip by Corey Harrell in Python.
auto_rip automates the execution of RegRipper according to an examination process.
auto_rip is a Copyright of Corey Harrell (jIIr).

## Why was this created?
I like the concept of auto_rip and have been using it for registry analysis. 
However, it had not been updated for two (2) years. In the meantime, Harlen Carvey (and others) 
had released new regripper plugins that were not executed as part of auto_rip.

This was written in Python because of my familiarity with the language. It was also re-written
in such a way that users can easily update the supported plugins or their categories 
in `plugin_categories.py` without programming knowledge.

## Dependencies
1. Python 3
2. yarp - `pip3 install https://github.com/msuhanov/yarp/archive/1.0.31.tar.gz`

or use the [release executable](https://github.com/Silv3rHorn/autoripy/releases)

## Usage
```bash
usage: autoripy [-h] [rr] [-s SYSTEM] [-a AMCACHE] [-n NTUSER] [-u USRCLASS] [-m MULTIPLE] [-r REPORTDIR] [-c CAT]

autoripy is an attempt to replicate the functions of auto_rip by Corey Harrell in Python.
auto_rip automates the execution of RegRipper according to an examination process.
auto_rip is a Copyright of Corey Harrell (jIIr).

Supported Categories:
         all             gets information from all categories
         os              gets General Operating System Information
         users           gets User Account Information
         software        gets Installed Software Information
         network         gets Networking Configuration Information
         storage         gets Storage Information
         device          gets Device Information
         execution       gets Program Execution Information
         autoruns        gets Autostart Locations Information
         log             gets Logging Information
         malware         gets Malware Indicators
         web             gets Web Browsing Information
         user_config     gets User Account Configuration Information
         user_act        gets User Account General Activity
         user_network    gets User Account Network Activity
         user_file       gets User Account File/Folder Access Activity
         user_virtual    gets User Account Virtualization Access Activity
         comm            gets Communication Software Information

Usage:
         Extract all information from the SAM, Security, Software, and System hives.
         autoripy C:\regripper -s H:\Windows\System32\config -c all

         Flush all transaction logs + Extract all information from the SAM, Security, Software, and System hives.
         autoripy C:\regripper -s H:\Windows\System32\config -c all --flush

         Extract file access information from NTUSER.DAT and UsrClass.dat hive (Windows 7 profile)
         autoripy C:\regripper -n H:\Users\Corey -u H:\Users\Corey\AppData\Local\Microsoft\Windows -c user_file

         Extract all information from all Windows registry hives without using -c switch.
         autoripy C:\regripper -s H:\Windows\System32\config -a H:\Windows\AppCompat\Programs -n H:\Users\Corey -u H:\Users\Corey\AppData\Local\Microsoft\Windows

         Extract all information from the SAM, Security, Software and System hives, then store output reports in a specified directory.
         autoripy C:\regripper -s H:\Windows\System32\config -r C:\reports

         Extract all information from the SAM, Security, Software and System hives, NTUSER.DAT and UsrClass.dat from each user in separate directories, then store output reports in a specified directory.
         autoripy C:\regripper -s H:\hives -m H:\hives\Users -r C:\reports

positional arguments:
  rr                    path to the folder containing RegRipper.

optional arguments:
  -h, --help            show this help message and exit
  -s SYSTEM, --system SYSTEM
                        path to the folder containing the SAM, Security, Software, and System hives.
  -a AMCACHE, --amcache AMCACHE
                        path to the folder containing the Amcache.hve hive.
  -n NTUSER, --ntuser NTUSER
                        path to the folder containing the NTUSER.DAT hive.
  -u USRCLASS, --usrclass USRCLASS
                        path to the folder containing the UsrClass.dat hive.
  -m MULTIPLE, --multiple MULTIPLE
                        path to the folder containing multiple <User>\NTUSER.DAT and/or <User>\UsrClass.DAT.
  -r REPORTDIR, --reportdir REPORTDIR
                        path to the folder to store the output reports.
  -c CAT, --cat CAT     specifies the plugin categories to run. Separate multiple categories with a comma.
  --flush               flush transaction logs
```

## References
1. [Regripper](https://github.com/keydet89/RegRipper4.0)
2. [Unleasing autorip](http://journeyintoir.blogspot.sg/2013/05/unleashing-autorip.html)
