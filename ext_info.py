#!/usr/bin/env python3
import sys
from pathlib import Path
from collections import defaultdict, OrderedDict

def add_suffix():
    return {'count': 0, 'size': 0}

usage = '''usage: ext_info.py path
displays number of files and total size of files per extension in the specified path.'''

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help']:
        print(usage)
        exit(-1)
    suffices = defaultdict(add_suffix)
    files = Path(sys.argv[1]).iterdir()
    for f in files:
        if f.is_file():
            suf = f.suffix
            if suf == '':
                suf = '.'
            if suf != '.': 
                suf = suf[1:] #skip dot
            s = suffices[suf]
            s['count'] += 1
            s['size'] += f.stat().st_size

    
    for k, v in OrderedDict(sorted(suffices.items())).items():
        print(k, v['count'], v['size'])
