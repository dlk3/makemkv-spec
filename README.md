# Fedora RPM Package For makemkv Application

`makemkv` is a tool to rip and transcode DVD and Blu-Ray disks to MKV
files.  See its [home page](https://www.makemkv.com) for details.

This repository contains a `makemkv.spec` file that helps me build
an installation RPM file for `makemkv` for my Fedora 30 desktop.  In 
addition, I posted the RPMs that I built in the
[Releases tab](https://github.com/dlk3/makemkv-spec/releases) of this
repository

`makemkv` provides a replacement for the `libaacs` library RPM that
adds Blu-Ray decryption support to the VLC app and any others that use
`libaacs`.  I have included the necessary setup for this in this 
`makemkv` package.  See [this makemkv forum post](https://www.makemkv.com/forum/viewtopic.php?f=3&t=7009)
for additional details.
