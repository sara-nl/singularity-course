# Running singularity examples on Cartesius

Here are your first steps:

1. [Login to Cartesius](#cartesius-login)
2. [Environment set up](#cartesius-env)
3. [Submit a job](#job-submit)
4. [Word on Docker vs Singularity + some stuff about singularity not covered](#wrap-up)

### <a name="cartesius-login"></a> 1. Login to Cartesius

* The login credentials will be provided to you at the start of the session.
* Open a terminal in your laptop 
    
 ```sh
 ssh username@cartesius.surfsara.nl #replace `username` with the username assigned to you
 ```
  
#### Get familiar with the login node

* Find your home directory and its content:

```sh
pwd
ls -l
singularity --version # what output do you see?
```

### <a name="job-submit"></a> 3. Submit jobs on Cartesius using Singularity images

* Submit a simple job
  The script jobsubmit-lolcow.sh is present in your home directory that has the following contents:
  
  ```sh
  cat jobsubmit-lolcow.sh
  
  #!/bin/bash
  #SBATCH -n 1
  #SBATCH -t 10:00
  echo "Hello I am running a singularity job with the following singularity version"
  singularity --version
  echo "I am running on " $HOSTNAME
  ./GodloveD-lolcow-master-latest.simg
  ```
  -n: number of tasks  
  -t: max total run time of the job allocation
  
  Now that you have inspected the script that will submit your job, let's submit a job by running the following:
  
  ```sh
  sbatch jobsubmit-lolcow.sh  #This command will submit a job and give you a job ID in return
  squeue -u $USER  #Check the status of your job
  ls  #Check if the output is present in your directory
  cat slurm-yourjobid.out
  ```
  So you ran a Singularity container that is in your home directory (on the login node) on a worker node where Singularity is actually installed.

* Submit a job that runs a Python script

 Now inspect the jobsubmit-python2.sh script. The Python scrips is located in your $HOME directory.
 ```sh
  cat jobsubmit-python2.sh
  
  #!/bin/bash
  #SBATCH -n 1
  #SBATCH -t 10:00
  echo "Hello I am running a singularity job with the following singularity version"
  singularity --version
  echo "I am running on " $HOSTNAME
  singularity exec python2-docker.simg python python2.py
  ```
  Now submit the job and inspect its output:
  
  ```sh
  sbatch jobsubmit-python2.sh  #This command will submit a job and give you a job ID in return
  squeue -u $USER  #Check the status of your job
  ls  #Check if the output is present in your directory
  cat slurm-yourjobid.out
  ```
* Submit a job using $TMPDIR (for better performance)

 Now inspect the jobsubmit-python2-tmpdir.sh script
 
 ```sh
  cat jobsubmit-python2-tmpdir.sh
  #!/bin/bash
  #SBATCH -n 1
  #SBATCH -t 10:00
  echo "Hello I am running a singularity job with the following singularity version"
  singularity --version
  echo "I am running on " $HOSTNAME
  cp $HOME/python2.py $HOME/python2-docker.simg $TMPDIR
  cd $TMPDIR
  I am now present in the directory " $PWD
  singularity exec python2-docker.simg python python2.py
  ```
  If you wish to have better performance, it is better to use the local scratch space on the worker node. This can be achieved by using the prederfined $TMPDIR variable as described above. Now submit a job and inspect the output:
  
   ```sh
  sbatch jobsubmit-python2-tmpdir.sh  #This command will submit a job and give you a job ID in return
  squeue -u $USER  #Check the status of your job
  ls  #Check if the output is present in your directory
  cat slurm-yourjobid.out
  ```
  
* Submit a job using the --bind option

singularity exec --pwd $PWD python3.simg python python3.py   #This may also fail
singularity exec --bind $PWD:/data python3.simg python /data/python-example.py
using tmpdir -- discuss bind/mount option in more detail

4. discuss different container formats
5. recap of what we did and close







