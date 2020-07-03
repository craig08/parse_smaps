# Parse smaps

`smaps` is an useful file to inspect the memory footprint of the process in linux.

It shows the memory mapping entries of a given process.

This tool simply parses 4 values and sums up the memory used from the same file:

- Private Clean
- Private Dirty
- Shared Clean
- Shared Dirty

## Usage

- Use with a process name (automatically get the first pid by `pidof`)

```
$> sudo python parse_smaps.py -p sshd
There are multiple pids:
[0]    83568: sshd: vagrant@pts/6
[1]    83566: sshd: vagrant [priv]
[2]      360: sshd: /usr/bin/sshd -D [listener] 0 of 10-100 startups
Choose which one process you want (default=0):
======================================================================
 Private +  Private +   Shared +   Shared
   Clean +    Dirty +    Clean +    Dirty =    Total : library
======================================================================
    0 kB +     0 kB +  1364 kB +   184 kB =  1548 kB : libcrypto.so.1.1
    0 kB +     8 kB +  1380 kB +    16 kB =  1404 kB : libc-2.31.so
    0 kB +     4 kB +   640 kB +    12 kB =   656 kB : sshd
    0 kB +   436 kB +     0 kB +   136 kB =   572 kB : [heap]
    0 kB +     4 kB +   184 kB +    12 kB =   200 kB : libnss_systemd.so.2
    0 kB +    32 kB +     0 kB +    68 kB =   100 kB : [anonymous]
    0 kB +     4 kB +    64 kB +    20 kB =    88 kB : pam_systemd.so
    0 kB +     4 kB +    80 kB +     4 kB =    88 kB : libpthread-2.31.so
   24 kB +     0 kB +    56 kB +     8 kB =    88 kB : libz.so.1.2.11
    0 kB +     0 kB +     0 kB +    68 kB =    68 kB : libkrb5.so.3.3
    0 kB +     0 kB +    48 kB +     8 kB =    56 kB : libpam.so.0.84.2
    0 kB +     4 kB +    40 kB +     4 kB =    48 kB : ld-2.31.so
    0 kB +     0 kB +    36 kB +     8 kB =    44 kB : pam_unix.so
    0 kB +     0 kB +    36 kB +     8 kB =    44 kB : libnss_files-2.31.so
    0 kB +     4 kB +    36 kB +     4 kB =    44 kB : libaudit.so.1.0.0
    0 kB +    36 kB +     0 kB +     4 kB =    40 kB : [stack]
...
===============================================================================
   24 kB +   536 kB +  4012 kB +   800 kB =  5372 kB : Total
```

- Use with a specified smaps file

```
$> sudo python parse_smaps.py /proc/83581/smaps
======================================================================
 Private +  Private +   Shared +   Shared
   Clean +    Dirty +    Clean +    Dirty =    Total : library
======================================================================
    0 kB +    24 kB +  1528 kB +     0 kB =  1552 kB : libc-2.31.so
    4 kB +    52 kB +   544 kB +     0 kB =   600 kB : tmux
    0 kB +     0 kB +   400 kB +     0 kB =   400 kB : locale-archive
   32 kB +    12 kB +   252 kB +     0 kB =   296 kB : libevent-2.1.so.7.0.0
    0 kB +   228 kB +     0 kB +     0 kB =   228 kB : [heap]
    0 kB +    24 kB +   156 kB +     0 kB =   180 kB : libncursesw.so.6.2
    0 kB +     8 kB +   168 kB +     0 kB =   176 kB : ld-2.31.so
    0 kB +     8 kB +    92 kB +     0 kB =   100 kB : libpthread-2.31.so
    0 kB +     8 kB +    72 kB +     0 kB =    80 kB : libresolv-2.31.so
    0 kB +    52 kB +     0 kB +     0 kB =    52 kB : [anonymous]
    0 kB +    32 kB +     0 kB +     0 kB =    32 kB : [stack]
    0 kB +     8 kB +     8 kB +     0 kB =    16 kB : libutempter.so.1.2.0
    0 kB +     8 kB +     8 kB +     0 kB =    16 kB : libutil-2.31.so
    0 kB +     0 kB +     4 kB +     0 kB =     4 kB : [vdso]
    0 kB +     0 kB +     0 kB +     0 kB =     0 kB : [vvar]
    0 kB +     0 kB +     0 kB +     0 kB =     0 kB : [vsyscall]
======================================================================
   36 kB +   464 kB +  3232 kB +     0 kB =  3732 kB : Total
```
