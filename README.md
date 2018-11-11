# autoripy
![](https://img.shields.io/badge/python-2.7-blue.svg) ![](https://img.shields.io/badge/python-3.7-blue.svg)

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
1. Python 2.7 or 3.7
2. Perl
3. `Parse::Win32Registry` perl module

Regripper's `rip.pl` is used instead of `rip.exe` due to some discrepancies in the latter's output

## Usage
See `python autoripy.py -h`

## References
1. [Regripper](https://github.com/keydet89/RegRipper2.8)
2. [Unleasing autorip](http://journeyintoir.blogspot.sg/2013/05/unleashing-autorip.html)
