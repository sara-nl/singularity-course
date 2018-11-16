# Running singularity examples on Cartesius

Here are your first steps:

1. [Login to Cartesius](#cartesius-login)
2. [Get familiar with the login node](#cartesius-env)
3. [Submit jobs](#job-submit)
4. [Word on Docker vs Singularity + some stuff about singularity not covered](#wrap-up)

### <a name="cartesius-login"></a> 1. Login to Cartesius

The login credentials will be provided to you at the start of the session. Open a terminal in your laptop 
    
 ```sh
 ssh username@cartesius.surfsara.nl #replace `username` with the username assigned to you
 ```
  
### <a name="cartesius-env"></a> 2. Get familiar with the login node

Familiarize yourself with your environment :

 ```sh
 pwd
 ls -l
 python --version
 singularity --version # what output do you see?
 ```

### <a name="job-submit"></a> 3. Submit jobs on Cartesius using Singularity images

#### 3.1 Submit a simple job 

Inspect the script jobsubmit-lolcow.sh:
  
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

#### 3.2 Submit a job that runs a Python script

Inspect the script jobsubmit-python2.sh:

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

#### 3.3 Submit a job using $TMPDIR (for better performance than $HOME)

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
  
#### 3.4 Submit a job using the --bind option

Now lets say you need to submit tens of hundreds of jobs. Can you afford an overhead of copying the image everytime? Is there a better way? You can use a /scratch-shared space that is shared by the worker nodes. It can be a temporary placeholder for the images when you run your jobs.

 ```sh
 mkdir /scratch-shared/$USER/
 cp python* /scratch-shared/$USER  
 ```
Inspect the script jobsubmit-python2-bind.sh

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
 ```

Check the output of your job. What do you see and why?
  
If you recall the steps we performed in the previous section of building images there is the answer. Depending on how the /scratch space is mounted the above may or may not work on other systems. Edit the above script to add the Singularity commands as follows:

  ```sh
  ls /scratch-shared/$USER/
  echo "By specifying the path to the files"
  singularity exec /scratch-shared/$USER/python2-docker.simg python /scratch-shared/$USER/python2.py   
  
  echo "By using the pwd flag"
  singularity exec --pwd  /scratch-shared/$USER python2-docker.simg python python2.py
  
  echo "By binding the path"
  singularity exec --bind /scratch-shared/$USER:/data python2-docker.simg python /data/python3.py
  ```
  
  
 

What does not output look like now? Do you know what the error means and how to fix it? 
Hint: Recall the discussion in the previous section about which directories are accessible to Singularity

5. recap of what we did and close







