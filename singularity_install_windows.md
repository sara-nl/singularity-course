#=======================================================================================
# Singularity course 2018: Singularity Version 2.6.0

AUTHOR: SURFsara DDP Team @ SURFsara

DESCRIPTION: Instructions for installing Singularity version 2.6.0 for Windows below.

VERSION/DATE: 0.1/16-11-2018 
#=======================================================================================

We will use the public Singularity version from GitHub (also known as the community version)

# **Installation on Windows**

The below documentation for the installation follows the information as provided by Sylabs: 

- https://www.sylabs.io/docs/
- https://www.sylabs.io/guides/2.6/user-guide/installation.html#install-on-windows

Windows does not provide support for Singularity. Singularity for Windows is therefore based on first installing Oracle VirtualBox which is a free and open-source hosted hypervisor for x86 computers. We will install Vagrant on top of VirtualBox. Vagrant is a tool for building and distributing development environments (https://github.com/hashicorp/vagrant). Using Vagrant we will then pull an Ubuntu 16.04.3 VM, containing a pre-built Singularity installation, and run it in VirtualBox. 

*Please note that the available Vagrant files have not yet moved moved beyond Singularity version 2.4. If a higher version of singularity is required then it is possible to build your own [Linux](https://github.com/maithili-k/singularity-course/blob/master/singularity_install_linux.md) VM using VirtualBox and/or Vagrant and install Singularity within that. This is however beyond thescope of this course and we will therefore stick to version 2.4 when considering Windows.*



**Installation steps for Singularity version 2.4 on Windows**

*Please note that the above steps have not been tested by us and we can guarentee that these will work*

1. Download Git for Windows, from: https://gitforwindows.org/  On this website click download, which will take you to the page that contains the necessary .exe files, i.e. https://github.com/git-for-windows/git/releases/tag/v2.19.1.windows.1

*Please note that for Git you need to chose the correct version of the .exe file that suits your specific laptop. On the linked webpage select Git-(version)-(XX-bit).exe, where XX-bit is either 32-bit or 64-bit. To determine the correct .exe file you may for Windows 10 use; Tap or click PC and devices, and then tap or click PC info. Look under Windows for the version and edition of Windows that your PC is running. Look under PC for System type to see if you're running a 32-bit or 64-bit version of Windows.*  

2. Run the .exe file (e.g.  Git-2.19.1-64-bit.exe) to install Git

2. Download VirtualBox (here version 5.2.22), for Windows hosts, from: https://www.virtualbox.org/wiki/Downloads

3. Run the .exe file (e.g. VirtualBox-5.2.22-126460-Win.exe) to install VirtualBox

4. Download Vagrant for Windows, from: https://www.vagrantup.com/downloads.html

*Please note that you need to select the appropriate version 32-bit or 64-bit for your laptop. You may use the note in (1) to obtain this information for Windows 10.*

5. Run the .msi file (e.g. vagrant_2.2.1_x86_64.msi) to install Vagrant

6. Download Vagrant Manager for Windows, from: http://vagrantmanager.com/downloads/  On this website select the Windows option in the Download section. This which will take you to the page that contains the necessary .zip files, i.e. https://github.com/lanayotech/vagrant-manager-windows/releases

7. Select the appropriate .zip file (e.g. vagrant-manager-windows-1.0.0.6.zip), open and unpack it. Run the necessary files from the unpacked .zip file to install Vagrant manager. 

8. Run GitBash , this will open a bash terminal and take you to the default home directory which will be C:Usersyour_username

*The following commands need to be executed from the bash terminal that you opened with GitBash*


    $ mkdir singularity-2.4
    $ cd singularity-2.4
    $ vagrant init singularityware/singularity-2.4
    
    Note: If this directory is not new then first run $ vagrant destroy
    
    $ vagrant init singularityware/singularity-2.4       
    $ vagrant up
    $ vagrant ssh

The vagrant ssh command will take you inside the Vagrant VirtualBox VM image and here you can run singularity (2.4).

    $ vagrant ssh
    $ which singularity
      /usr/local/bin/singularity
    $ singularity selftest
      + sh -c test -f /usr/local/etc/singularity/singularity.conf                           (retval=0) OK
      + test -u /usr/local/libexec/singularity/bin/action-suid                              (retval=0) OK
      + test -u /usr/local/libexec/singularity/bin/mount-suid                               (retval=0) OK
      + test -u /usr/local/libexec/singularity/bin/start-suid                               (retval=0) OK

Exit your Vagrant environment.
    
    $ exit
      logout
      Connection to 127.0.0.1 closed.

Halt your running VM (i.e. terminate it and thereby release the resources it is using on your laptop)

    $ vagrant halt
       Attempting graceful shutdown of VM...

To restart the VM and access the image containing singularity again, use  

    $ vagrant up  
    $ vagrant ssh
