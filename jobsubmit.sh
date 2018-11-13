#!/bin/bash
#SBATCH -N 1
#SBATCH -t 10:00
echo "Hello I am running a singularity job"
singularity --version
echo "I am here" $PWD
echo "Running the job with singularity now"
singularity exec python-2-7.simg python python2.py
singularity exec python-3.simg python python2.py
singularity exec python-3.simg python python3.py

 
