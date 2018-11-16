# Running singularity examples on Cartesius

Here are your first steps:

1. [Login to Cartesius](#cartesius-login)
2. [Get familiar with the login node](#cartesius-env)
3. [Submit jobs](#job-submit)
4. [Word on Docker vs Singularity + some stuff about singularity not covered](#wrap-up)

### <a name="cartesius-login"></a> 1. Login to Cartesius

* The login credentials will be provided to you at the start of the session.
* Open a terminal in your laptop 
    
 ```sh
 ssh username@cartesius.surfsara.nl #replace `username` with the username assigned to you
 ```
  
### <a name="cartesius-env"></a> 2. Get familiar with the login node

* Familiarize yourself with your environment :

```sh
pwd
ls -l
python --version
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
  -t: max total run time of the job, here it is 10 minutes
  
  Now that you have inspected the script that will submit your job, let's submit a job by running the following:
  
  ```sh
  sbatch jobsubmit-lolcow.sh  #This command will submit a job and give you a job ID in return
  squeue -u $USER  #Check the status of your job
  ls  #Check if the output,slurm-jobID.out, is present
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
  ls  #Check if the output,slurm-jobID.out, is present
  cat slurm-yourjobid.out
  ```
* Submit a job using $TMPDIR (for better performance than $HOME)

  If you wish to have better performance, it is better to use the local /scratch space on the worker node. This can be achieved  by using the prederfined $TMPDIR variable as described below. Inspect the jobsubmit-python2-tmpdir.sh script to see the set up:
 
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
  echo "I am now present in the directory " $PWD
  singularity exec python2-docker.simg python python2.py
  ```
  Now submit a job and inspect the output:
  
   ```sh
  sbatch jobsubmit-python2-tmpdir.sh  #This command will submit a job and give you a job ID in return
  squeue -u $USER  #Check the status of your job
  ls  #Check if the output is present in your directory
  cat slurm-yourjobid.out
  ```
  
* Submit a job using the --bind option
  Now lets say you need to submit tens of hundreds of jobs. Can you afford an overhead of copying the image everytime? Is there a better way? You can use a /scratch space that is shared by the worker nodes. It can be a temporary placeholder when you run your jobs.

  ```sh
  mkdir /scratch-shared/$USER/
  cp python* /scratch-shared/$USER  
  ```
  In addition we will use both the containers with differing versions of Python.
  
  ```sh
  cat jobsubmit-python2-bind.sh
  
  #!/bin/bash
  #SBATCH -n 1
  #SBATCH -t 10:00
  echo "Hello I am running a singularity job with the following singularity version"
  singularity --version
  echo "I am running on " $HOSTNAME
  echo "I am now present in the directory " $PWD
  singularity exec python2-docker.simg python python2.py
  singularity exec python3.simg python python3.py
  ```
  Check the output of your job. What do you see and why?
  
  If you recall the steps we performed in the previous section of building images there is the answer. Edit the above script for the Singularity commands to look as follows:

  ```sh
  ls /scratch-shared/$USER/
  echo "By specifying the path to the files"
  singularity exec /scratch-shared/$USER/python2-docker.simg python /scratch-shared/$USER/python2.py   
  singularity exec /scratch-shared/$USER/python3.simg python /scratch-shared/$USER/python3.py   
  echo "By using the pwd flag"
  singularity exec --pwd  /scratch-shared/$USER python3.simg python python3.py  
  singularity exec --pwd  /scratch-shared/$USER python3.simg python python3.py  

  ```
  Depending on how the /scratch space is mounted the above may or may not work on other systems. In this case you can use one of the following comamnds:
  
  ```sh
  singularity exec --pwd $PWD python3.simg python python3.py   #This may also fail
  singularity exec --bind $PWD:/data python3.simg python /data/python-example.py
  ```

singularity exec --exec --pwd /scratch-shared/$USER python3.simg python python3.py
singularity exec --bind /scratch-shared/$USER:/data python3.simg python /data/python3.py
  ```
  
  
  
  ```
  
  singularity exec --pwd $PWD python3.simg python python3.py   #This may also fail
  singularity exec --bind $PWD:/data python3.simg python /data/python-example.py
  using tmpdir -- discuss bind/mount option in more detail

4. discuss different container formats
5. recap of what we did and close







