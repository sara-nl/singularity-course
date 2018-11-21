# singularity-course

# Course at VU: Using Singularity application containerization for reproducible scientific computing

**Content**

The workshop aims to provide an introduction and hands-on experience in containerization. Container technologies, such as docker and Singularity, are a new way to package your software in a portable way providing mobility to your computing. You can build your containerized application once and run the same application on various HPC systems e.g., the Cartesius supercomputer, the HPC Cloud, Grid clusters, etc. By packaging specific versions of your application and all dependent libraries, you ensure reproducibility of your own results and you allow others to verify your results.

**Objectives**

 - Understanding containerization basics
 
 - Hands-on experience with Docker & Singularity
 
 - Hands-on experience in building containerized applications
 
 - Hands-on experience in running containerized applications on your laptop and different HPC systems

**Target group / Prerequisites**

Scientists or application developers interested in software portability among various compute platforms and particularly containerization are welcome. Prior knowledge about containerization is not required.

  - Familiarity with Linux commands
  
  - Familiarity with batch systems (ssh access, job submission), preferably you have followed Introduction to cluster computing course (cluster-computing)
  
  - Please install Docker to your laptop prior to the course. Install from https://store.docker.com/search?offering=community&type=edition (may require creation of a free Docker account)

**Where**: VU campus, Room - WN-F201 

**When**: November 23, 2018, 9-12:30

Program:
--------
9.00 - 9.20  -  Presentation: Introduction to containers

9.20 - 10.00   -  Hands on: Interacting with [Docker](https://github.com/maithili-k/singularity-course/blob/master/run-docker.md) containers on your laptop

10:00 - 10.20  -  Hands on: Installing Singularity on your [Linux](https://github.com/maithili-k/singularity-course/blob/master/singularity_install_linux.md), [Mac OS X](https://github.com/maithili-k/singularity-course/blob/master/singularity_install_mac_osx.md) or [Windows](https://github.com/maithili-k/singularity-course/blob/master/singularity_install_windows.md) laptop.

10.20 - 10.30  - Break

10.30 - 11:00  -  Demo followed by Hands on: [Build](https://github.com/maithili-k/singularity-course/blob/master/build-singularity-image.md) singularity images 

11:00 - 12:30  -  Hands on: Running Singularity containers on a [Supercomputer](https://github.com/maithili-k/singularity-course/blob/master/run-singularity-cartesius.md)
