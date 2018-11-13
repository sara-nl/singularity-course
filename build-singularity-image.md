# Building Singularity images

1. [Pull Singularity images](#pull-singularity)
2. [Build Singularity images from a recipe](#build-singularity)
3. [Convert Docker images to Singularity](#convert-docker)

   
### <a name="pull-singularity"></a> 1. Pull and run Singularity images
 
You will need Singularity installed on your workstation to proceed. If you did not manage to perform this, the below steps  will be shown in the demo.

   ```sh
   singularity pull shub://GodloveD/lolcow  # you may also use docker hub - singularity pull docker://godlovedc/lolcow
   ls
   singularity inspect GodloveD-lolcow-master-latest.simg
   ```
 Now let's run the image:
    
   ```sh
   ./GodloveD-lolcow-master-latest.simg 
    ________________________________________
   / Let me put it this way: today is going \
   \ to be a learning experience.           /
    ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

   ```

### <a name="build-singularity"></a> 2. Build Singularity images from a recipe

You will need Singularity installed on your workstation to proceed. If you did not manage to perform this, the below steps  will be shown in the demo.

   ```sh
   cat python3-recipe
   Bootstrap: docker

   From: python:latest

   Registry: index.docker.io

   Namespace: library

   %runscript

      exec echo "I am running your Singulariy container!"
      
   ```
With this recipe let's build the image

   ```sh
   sudo singularity build python3.simg python3-recipe
   singularity exec python3.simg python
   singularity exec python3.simg python python3.py #This may fail 
   ```
   
   By default singularity bind mounts /home/$USER, /tmp, and $PWD into your container at runtime. to bind more mounts more do the following:
   
   ```sh
   singularity exec --bind $PWD:/data python3.simg python /data/python3.py
   singularity exec --bind $PWD:/data python3.simg python /data/python-example.py
   ``` 
 
### <a name="convert-docker"></a> 3. Convert Docker images to Singularity

To convert a local Docker image run the folowing command 
   ```sh
   sudo docker run -v /var/run/docker.sock:/var/run/docker.sock --privileged -t --rm singularityware/docker2singularity    python2-for-cartesius
   ls
   ```
   
If you have singularity installed, you can test if your image works

   ```sh
   singularity shell python2-for-cartesius-2018-11-05-51908ebcb7a7.simg
   ls
   pwd
   ls /
   python --version
   which python
   ```

**Note: If you want to build Singularity images without having singularity installed in a build environment, you can build images using Singularity Hub instead - https://github.com/singularityhub/singularityhub.github.io/wiki
