#=======================================================================================
# Singularity course 2018: Singularity Version 2.6.0

AUTHOR: SURFsara DDP Team @ SURFsara

DESCRIPTION: Instructions for installing Singularity version 2.6.0 for Linux distributions below.

VERSION/DATE: 0.1/16-11-2018
#=======================================================================================
    
  
  
We will use the public Singularity version from GitHub (also known as the community version)

The instructions below refer to two different flavors of Linux: 
- (A) RPM-based distributions: here we will focus on CentOS 7.5
- (B) Debian-based distributions: here we will focus on Ubuntu 18.04.1 (and 16.04.5)

The installations have been tested on the Oort HPC Cloud systems at SURFsara
- https://www.surf.nl/
- https://userinfo.surfsara.nl/systems/hpc-cloud
  
  
# **A. Installation on CentOS verion 7.5 (2018-11-01)**

Please use a bash terminal.

        $ sudo yum groupinstall "Development Tools"
        $ sudo yum install -y xorg-x11-server-Xorg xorg-x11-xauth xorg-x11-apps
        $ sudo yum install libarchive-devel
        $ sudo yum install squashfs-tools
        $ VERSION=2.6.0
        $ wget https://github.com/singularityware/singularity/releases/download/$VERSION/singularity-$VERSION.tar.gz
        $ tar xvf singularity-$VERSION.tar.gz
        $ cd singularity-$VERSION/
        $ ./configure --prefix=/usr/local
        $ make
        $ sudo make install
        $ singularity --version
        $ singularity selftest
          + sh -c test -f /usr/local/etc/singularity/singularity.conf                           (retval=0) OK
          + test -u /usr/local/libexec/singularity/bin/action-suid                              (retval=0) OK
          + test -u /usr/local/libexec/singularity/bin/mount-suid                               (retval=0) OK
          + test -u /usr/local/libexec/singularity/bin/start-suid                               (retval=0) OK
          
  
  
  
# **B. Installation on Ubuntu 18.04.1 and 16.04.5 (2018-11-01)** 

Please use a bash terminal.

        $ sudo apt-get install libarchive-dev
        $ sudo apt-get install squashfs-tools
        $ sudo apt install gcc
        $ sudo apt-get install build-essential
        $ VERSION=2.6.0
        $ wget https://github.com/singularityware/singularity/releases/download/$VERSION/singularity-$VERSION.tar.gz
        $ tar xvf singularity-$VERSION.tar.gz
        $ cd singularity-$VERSION/
        $ ./configure --prefix=/usr/local
        $ make
        $ sudo make install
        $ singularity --version
        $ singularity selftest
          + sh -c test -f /usr/local/etc/singularity/singularity.conf                           (retval=0) OK
          + test -u /usr/local/libexec/singularity/bin/action-suid                              (retval=0) OK
          + test -u /usr/local/libexec/singularity/bin/mount-suid                               (retval=0) OK
          + test -u /usr/local/libexec/singularity/bin/start-suid                               (retval=0) OK
  
  


Additional information and alternative installation options may e.g., be obtained from the singularity documentation 

[1] https://www.sylabs.io/docs/

[2] https://www.sylabs.io/guides/2.6/user-guide/index.html
