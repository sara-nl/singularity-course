# Running singularity examples on Cartesius

Here are your first steps:

1. [Login to Cartesius](#cartesius-login)
2. [Get familiar with the login node](#cartesius-env)
3. [Submit jobs](#job-submit)

### <a name="cartesius-login"></a> 1. Login to Cartesius

* You may use the same login credentials (e.g., sdemo0001) that were provided to you before the start of the course. Open a terminal in your laptop and login to Cartesius with: 
    
 ```sh
 ssh username@cartesius.surfsara.nl #replace `username` with the username assigned to you
 ```
  
### <a name="cartesius-env"></a> 2. Get familiar with the login node

* Familiarize yourself with your environment:

 ```sh
 pwd
 ls -l
 python --version
 singularity --version # what output do you see?
 ```

### <a name="job-submit"></a> 3. Submit jobs on Cartesius using Singularity images

#### 3.1 Submit a simple job 

* Inspect the script `jobsubmit-lolcow.sh`:
  
 ```sh
 cd ~
 cat jobsubmit-lolcow.sh
  
 #!/bin/bash
 #SBATCH -n 1
 #SBATCH -t 10:00
 #SBATCH --reservation=singularity
 echo "Hello I am running a singularity job with the following singularity version"
 singularity --version
 echo "I am running on " $HOSTNAME
 ./GodloveD-lolcow-master-latest.simg
 ```
 -n: number of tasks  
 -t: max total run time of the job, here it is 10 minutes
  
* Now that you have inspected the script that will submit your job, let's submit a job by running the following:
  
 ```sh
 sbatch jobsubmit-lolcow.sh  #This command will submit a job and give you a job ID in return
 squeue -u $USER  #Check the status of your job
 ls  #Check if the output,slurm-jobID.out, is present
 cat slurm-yourjobid.out
 ```

> **_Food for brain:_**
>
> * But you just checked in Section 2 that Singularity was not installed so how come it worked? Or rather where did it run? You ran a Singularity container that is in your home directory (on the login node) on a worker node where Singularity is actually installed.

#### 3.2 Submit a job that runs a Python script

* Inspect the script `jobsubmit-python2.sh`:

 ```sh
 cd ~/singularity-course
 cat jobsubmit-python2.sh
  
 #!/bin/bash
 #SBATCH -n 1
 #SBATCH -t 10:00
 #SBATCH --reservation=singularity
 echo "Hello I am running a singularity job with the following singularity version"
 singularity --version
 echo "I am running on " $HOSTNAME
 singularity exec python2-docker.simg python python2.py
 ```

* Now submit the job and inspect its output:
  
 ```sh
 sbatch jobsubmit-python2.sh  #This command will submit a job and give you a job ID in return
 squeue -u $USER  #Check the status of your job
 ls  #Check if the output,slurm-jobID.out, is present
 cat slurm-yourjobid.out
 ```

> **_Food for brain:_**
>
> * You may have created a singularity image in a different version on your laptop than on Cartesius and it still worked. Can you explain? 
    
#### 3.3 Submit a job using $TMPDIR (for better performance than $HOME)

* If you wish to have better performance, it is better to use the local `/scratch` space on the worker node. This can be achieved  by using the prederfined `$TMPDIR` variable as described below. Inspect the `jobsubmit-python2-tmpdir.sh` script to see the set up:
 
 ```sh
 cd ~/singularity-course
 cat jobsubmit-python2-tmpdir.sh
  
 #!/bin/bash
 #SBATCH -n 1
 #SBATCH -t 10:00
 #SBATCH --reservation=singularity
 echo "Hello I am running a singularity job with the following singularity version"
 singularity --version
 echo "I am running on " $HOSTNAME
 cp $HOME/singularity-course/python2.py $HOME/singularity-course/python2-docker.simg $TMPDIR
 cd $TMPDIR
 echo "I am now present in the directory " $PWD
 singularity exec python2-docker.simg python python2.py
 ```
    
* Now submit a job and inspect the output:
  
 ```sh
 sbatch jobsubmit-python2-tmpdir.sh  #This command will submit a job and give you a job ID in return  
 squeue -u $USER  #Check the status of your job
 ls  #Check if the output is present in your directory
 cat slurm-yourjobid.out
 ```
 
 > **_Food for brain:_**
>
> * Do you recall the $TMPDIR variable? What is the $TMPDIR path printed in the output and where did your python script run?

  
#### 3.4 Submit a job using the --pwd/--bind option

* Now lets say you need to submit tens of hundreds of jobs. Can you afford an overhead of copying the image everytime to `/scratch` in each job? You may use the `/scratch-shared` space that is shared amongst all the worker nodes (unlike the local `/scratch` space). It can be a temporary placeholder for the images when you run your jobs.

 ```sh
 cd ~/singularity-course
 mkdir /scratch-shared/$USER/
 cp python* /scratch-shared/$USER  
 cp jobsubmit-python2-bind.sh ../
 cd ../
 ```
 
* Inspect the script jobsubmit-python2-bind.sh and run a job:

 ```sh
 cd ~
 cat jobsubmit-python2-bind.sh
  
 #!/bin/bash
 #SBATCH -n 1
 #SBATCH -t 10:00
 #SBATCH --reservation=singularity
 echo "Hello I am running a singularity job with the following singularity version"
 singularity --version
 echo "I am running on " $HOSTNAME
 echo "I am now present in the directory " $PWD
 singularity exec python2-docker.simg python python2.py
 
 sbatch jobsubmit-python2-bind.sh
 ```

Check the output of your job. 

> **_Food for brain:_**
>
> * What do you see and why? Didn't you just tell me that the /scratch-shared is shared amongst on all worker nodes?  
  
* Recall the steps we performed in the previous section (building images) to mount a directory in the container. In this case we want to make our own `/scratch-shared` directory available in the container. There are several ways to do it as follows:

  ```sh
  echo "By specifying the path to the files"
  singularity exec /scratch-shared/$USER/python2-docker.simg python /scratch-shared/$USER/python2.py   
  
  echo "By using the pwd flag"
  singularity exec --pwd  /scratch-shared/$USER /scratch-shared/$USER/python2-docker.simg python /scratch-shared/$USER/python2.py
  
  echo "By using the bind flag"
  singularity exec --bind /scratch-shared/$USER:/mydata /scratch-shared/$USER/python2-docker.simg python /mydata/python2.py
  ```
 
> **_Food for brain:_**
>
> Modify the `jobsubmit-python2-bind.sh` script to make use of the data in your own `/scratch-shared` directory with any of the options above. Inspect the output of your job.
  
  
#### 3.5 Working with different software environments

Now that we have figured out how to work with containers, let us run an example assuming a scenario that your collaborator gave you a Python script to run your analysis. It runs into errors as the script is in Python3 while you have Python2 on your laptop and you do not wish to install Python3. How do you work around it? Singularity comes to your rescue!

* Inspect the script jobsubmit-python.sh, submit the job and check your output:

```sh
cd ~/singularity-course
cat jobsubmit-python.sh

#!/bin/bash
#SBATCH -n 1
#SBATCH -t 10:00
#SBATCH --reservation=singularity
echo "Hello I am running a singularity job with the following singularity version"
singularity --version
echo "I am running on " $HOSTNAME
echo "I am now present in the directory " $PWD
echo "Running your code with Python2"
singularity exec python2-docker.simg python python2.py
echo "Running your code with Python3"
singularity exec python3.simg python python2.py

sbatch jobsubmit-python.sh
```

* Now pay attention and run the correct version of Python script with the corresponding version of Python - change the last line of the above script to the following. You are nearly there!

```sh
singularity exec python3.simg python python3.py

sbatch jobsubmit-python.sh
```

You can see in your output that the run is successful. You basically just ran two different versions of Python with a single script! Yey! Although this is a simple example it demonstrates the power of Singularity. 

 ```sh
 _________________________________________________________________
< You may now show off your Singularity skills to your colleagues! >
 -----------------------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||


 ```




