#!/usr/bin/env python
#
# Author: Craig Chi <craig10624@gmail.com>
#

import sys
import os
import getopt
from collections import defaultdict, OrderedDict
from subprocess import check_output

def usage():
    print("""
usage: parse_smaps.py [-p process_name] [-t memory_type] [-h] [smaps_filename]

example: parse_smaps.py /proc/12424/smaps
         parse_smaps.py -p smbd
         parse_smaps.py -p smbd -t Pss
""")


def print_header(mem_idx):
    print('=' * 70)
    for title in zip(*map(lambda x: x.split('_'), mem_idx.keys()),
                     ('', '=    Total : library')):
        print('{:>8} + {:>8} + {:>8} + {:>8} {}'.format(*title,))
    print('=' * 70)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'p:t:ah',
                                   ['process-name=', 'memory-type=',
                                    'all', 'help'])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    ps_name = ''
    mem_type = ''
    mem_idx = OrderedDict([
        ('Private_Clean', 0),
        ('Private_Dirty', 1),
        ('Shared_Clean', 2),
        ('Shared_Dirty', 3)
    ])
    for o, a in opts:
        if o in ('-p', '--process-name'):
            ps_name = a
        elif o in ('-t', '--memory-type'):
            mem_type = a
            mem_idx = {a: 0}
        else:
            usage()
            sys.exit(2)

    if (len(args) == 0 and ps_name == '') or len(args) > 1:
        usage()
        sys.exit(2)

    smaps_file = ''
    if ps_name == '':
        smaps_file = os.path.abspath(args[0])
    else:
        try:
            pids = check_output(['pidof', ps_name]).decode().strip().split()
            if len(pids) > 1:
                print('There are multiple pids:')
                for i, p in enumerate(pids):
                    cmdline_file = '/proc/' + p + '/cmdline'
                    with open(cmdline_file, 'r') as cmdline:
                        line = next(cmdline)
                        print('[{}] {:>8}: {}'.format(i, p, line))
                num = input('Choose which one process you want (default=0): ')
                num = int(num) if num != '' else 0
                pid = pids[num]
            else:
                pid = pids[0]
        except Exception as err:
            print(err)
            sys.exit(1)

        smaps_file = '/proc/' + pid + '/smaps'

    mapinfo = defaultdict(lambda: [0] * len(mem_idx))
    total = [0] * len(mem_idx)

    with open(smaps_file, 'r') as smap:
        for line in smap:
            line_arr = line.split()
            if '-' in line_arr[0]:
                if len(line_arr) < 6:
                    filename = '[anonymous]'
                else:
                    filename = os.path.basename(line_arr[-1])
            else:
                line_arr[0] = line_arr[0].strip(':')

            if line_arr[0] in mem_idx:
                mapinfo[filename][mem_idx[line_arr[0]]] += int(line_arr[1])
                total[mem_idx[line_arr[0]]] += int(line_arr[1])

    if mem_type == '':
        print_header(mem_idx)

        for filename, mem in sorted(mapinfo.items(), key=lambda x: -sum(x[1])):
            print('{:>5} kB + {:>5} kB + {:>5} kB + {:>5} kB'
                  ' = {:>5} kB : {:<}'.format(*mem, sum(mem), filename))

        print('=' * 70)
        print('{:>5} kB + {:>5} kB + {:>5} kB + {:>5} kB'
              ' = {:>5} kB : Total'.format(*total, sum(total)))

    else:
        for filename, mem in sorted(mapinfo.items(), key=lambda x: -sum(x[1])):
            print('{:>11} kB {:<}'.format(mem[0], filename))

        print('=' * 30)
        print('Total: {} kB'.format(total[0]))


if __name__ == '__main__':
    main()
