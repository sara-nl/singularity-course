# Building Singularity images

1. [Pull and run Singularity images](#pull-singularity)
2. [Build Singularity images from a recipe](#build-singularity)
3. [Convert Docker images to Singularity](#convert-docker)
4. [Copy Singularity images to Cartesius](#copy-sing-cart)
   
### <a name="pull-singularity"></a> 1. Pull and run Singularity images
 
You will need Singularity installed on your laptop to proceed. If you did not manage to install it, the below steps will be shown in the demo.

   ```sh
   singularity -h # displays usage options
   singularity pull shub://GodloveD/lolcow  # you may also use docker hub - singularity pull docker://godlovedc/lolcow
   ls
   singularity inspect GodloveD-lolcow-master-latest.simg
   ```
   pull: Pull an image from e.g., Docker or Singularity Hub  
   inspect: Display a container's metadata
   
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

    ./GodloveD-lolcow-master-latest.simg 
    ________________________________________
    < Your present plans will be successful. >
    ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
   ```

### <a name="build-singularity"></a> 2. Build Singularity images from a recipe

You will need Singularity installed on your laptop to proceed. If you did not manage to install it, the below steps  will be shown in the demo. Create a file python3-recipe with your favourite text editor. The contents of the file should look like as below:

   ```sh
   Bootstrap: docker

   From: python:latest

   Registry: index.docker.io

   Namespace: library

   %runscript

      exec echo "I am running your Singulariy container!"
      
   ```
   We are downloading the latest python version from docker://index.docker.io/library/ubuntu:latest. The Bootstrap and From keywords are mandatory. With this recipe let's build the image and run the container:

   ```sh
   sudo singularity build python3.simg python3-recipe
   singularity exec python3.simg python
   exit()
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
   
### <a name="copy-sing-cart"></a> 4. Copy Singularity images to Cartesius

We can copy all our sinularity images to Cartesius. As this may take long or you don't have singularity installed on your workstation there are some ready to use Singularity images for you on Cartesius so you can also skip this step.

   ```sh
   du -sh *simg  #make sure it is not too big
   scp *simg username@cartesius.surfsara.nl:/home/$USER
   ```

**Note: If you want to build Singularity images without having singularity installed in a build environment, you can build images using Singularity Hub instead - https://github.com/singularityhub/singularityhub.github.io/wiki
