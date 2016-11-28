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
$> python parse_smaps.py -p smbd
===============================================================================
Private    Private     Shared     Shared
 Clean   +  Dirty   +  Clean   +  Dirty   =  Total   : library
===============================================================================
   12 kB +  7456 kB +     4 kB +     0 kB =  7472 kB : [heap]
 1584 kB +     4 kB +   484 kB +     0 kB =  2072 kB : libsmbd-base.so.0
    0 kB +  1392 kB +     0 kB +     0 kB =  1392 kB : locking.tdb
   12 kB +     8 kB +  1308 kB +     0 kB =  1328 kB : libc-2.23.so
  512 kB +     0 kB +     8 kB +     0 kB =   520 kB : libndr-standard.so.0.0.1
   80 kB +     4 kB +   268 kB +     0 kB =   352 kB : libsmbconf.so.0
  248 kB +     0 kB +    36 kB +     0 kB =   284 kB : libndr-samba.so.0
  188 kB +     0 kB +    20 kB +     0 kB =   208 kB : libndr-samba4.so.0
  204 kB +     0 kB +     0 kB +     0 kB =   204 kB : libsamba-passdb.so.0.24.1
    0 kB +   176 kB +     0 kB +     0 kB =   176 kB : smbXsrv_open_global.tdb
   32 kB +     0 kB +   144 kB +     0 kB =   176 kB : libsmbregistry.so.0
   84 kB +     0 kB +    80 kB +     0 kB =   164 kB : libsamba-hostconfig.so.0.0.1
  144 kB +    20 kB +     0 kB +     0 kB =   164 kB : [anonymous]
    0 kB +     4 kB +   156 kB +     0 kB =   160 kB : ld-2.23.so
...
===============================================================================
 5832 kB +  9256 kB +  5248 kB +     8 kB = 20344 kB : Total
```

- Use with a specified smaps file

```
$> parse_smaps.py /proc/957/smaps
===============================================================================
Private    Private     Shared     Shared
 Clean   +  Dirty   +  Clean   +  Dirty   =  Total   : library
===============================================================================
    4 kB +     0 kB +   472 kB +     0 kB =   476 kB : libc-2.23.so
   12 kB +     0 kB +   312 kB +     0 kB =   324 kB : libcrypto.so.1.0.0
    8 kB +     0 kB +   284 kB +     0 kB =   292 kB : sshd
   16 kB +     0 kB +     0 kB +     0 kB =    16 kB : [anonymous]
...
===============================================================================
   44 kB +     0 kB +  1072 kB +     0 kB =  1116 kB : Total
```
