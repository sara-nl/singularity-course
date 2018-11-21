#=====================================================================================
# Singularity course 2018: Singularity Version 2.6.0

AUTHOR: SURFsara DDP Team @ SURFsara

DESCRIPTION: Instructions for installing Singularity version 2.6.0 for Mac OS X distributions below.

VERSION/DATE: 0.1/16-11-2018 
#=====================================================================================

We will use the public Singularity version from GitHub (also known as the community version)

# **Installation on Mac OS X Mojave (2018-11-05)**

The below documentation for the installation closely follows: 

- https://www.sylabs.io/docs/
- https://www.sylabs.io/guides/2.6/user-guide/installation.html#install-on-mac

Mac OS X does not provide support for Singularity. Singularity for Mac OS X is therefore based on first installing Oracle VirtualBox which is a free and open-source hosted hypervisor for x86 computers. We will install Vagrant on top of VirtualBox. Vagrant is a tool for building and distributing development environments (https://github.com/hashicorp/vagrant). Using Vagrant we will then pull an Ubuntu 16.04.3 VM, containing a pre-built Singularity installation, and run it in VirtualBox. 

*Please note that the available Vagrant files have not yet moved moved beyond Singularity version 2.4. If a higher version of singularity is required then it is possible to build your own [Linux](https://github.com/maithili-k/singularity-course/blob/master/singularity_install_linux.md) VM using VirtualBox and/or Vagrant and install Singularity within that. This is however beyond thescope of this course and we will therefore stick to version 2.4 when considering Mac OS X.*



**Installation steps for Singularity version 2.4 on Mac OS X (Mojave)**

1. Download VirtualBox (here version 5.2.22), for OS X hosts, from: https://www.virtualbox.org/wiki/Downloads

2. Unpack the dmg and install it. This may not work directly as Mac OS X prevents Oracle to have access. To resolved this please go to;

Apple menu -> System preferences -> Security & Privacy -> General -> "Allow access ... Oracle" 

  * note the Oracle part may not be directly visible in General (check for generic sentence and click it)
  * the access being prevented may not show up in General under after the first failed installation trial
  * This error would also be visible as an "NE_ERROR_" error, e.g. when trying to run (a) $ vagrant up, or (b) $ trying to create a new VM in the GUI for VirtualBox
  
When the access issue has been resolved, try to install VirtualBox again and it should now succeed. 

3. Continue by installing Vagrant.
    
    ```sh
    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    $ brew cask install vagrant
    $ brew cask install vagrant-manager
    $ mkdir singularity-vm
    $ cd singularity-vm
    $ vagrant init singularityware/singularity-2.4   (note do vagrant destroy if it already exists, or create new dir)
    $ vagrant up
    $ vagrant ssh
    ```

The vagrant ssh command will take you inside the Vagrant VirtualBox VM image and here you can run singularity (2.4):

    ```sh
    $ vagrant ssh
    $ which singularity
      /usr/local/bin/singularity
    $ singularity selftest
      + sh -c test -f /usr/local/etc/singularity/singularity.conf                           (retval=0) OK
      + test -u /usr/local/libexec/singularity/bin/action-suid                              (retval=0) OK
      + test -u /usr/local/libexec/singularity/bin/mount-suid                               (retval=0) OK
      + test -u /usr/local/libexec/singularity/bin/start-suid                               (retval=0) OK
    ```

Exit your Vagrant environment 
    
    ```sh
    $ exit
      logout
      Connection to 127.0.0.1 closed.
    ```

Halt your running VM (i.e. terminate it and thereby release the resources it is using on your laptop)

    $  vagrant halt
       Attempting graceful shutdown of VM...

To restart the VM, use  

    $ vagrant up  (and follow this by , $ vagrant ssh , to get into the image again)
