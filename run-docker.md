# Running docker on your laptop

1. [Start docker daemon](#start-docker)
2. [Check Docker installation](#check-docker)
3. [Run interactive containers](#run-interactive)
4. [Create a Python image to be converted to Singularity](#create-image) 

### <a name="start-docker"></a> 1. Start docker daemon

Let us first start the docker daemon: 

* Linux: Open a terminal in your laptop and run

    ```sh
    sudo systemctl start docker
    ```
    if the above command fails run 
    ```sh
    sudo service docker start
    ```
* Mac: Start the docker daemon via Launchpad. The Docker whale icon is displayed in your menu bar

* Windows: Search for Docker, select Docker for Windows in the search results, and click it (or hit Enter)

> **NB: For Linux, preface all the docker commands in exercises below with `sudo`**
  
### <a name="check-docker"></a> 2. Check the docker installation

* Getting started: Run the following commands in a terminal  

    ```sh
    # Get help for docker commands and info 
    docker
    docker version
    docker info 
    # List all docker images stored in your laptop
    docker image ls 
    # List all containers spawned in your laptop, running or stopped
    docker container ls --all  #or docker ps -a
    ```

Image: An image  is an executable package that includes everything needed to run an application.    
Container: A container is a runtime instance of an image - what the image becomes when executed. 

* Run the following command and see what happens: 

    ```sh
    docker run hello-world
    ```  

* List your images and your containers again

> **_Food for brain:_**
>
> * How come you ran a container when you didn't have the image in the first place?
> * Repeat the hello-world example a couple of times. What happens to the lists of images and containers?  
> * Can you find the IDs and names of your containers?

    
### <a name="run-interactive"></a> 3. Run interactive containers

* The following command downloads the latest bash image and runs it in the interactive mode. Try it:

   ```sh
   docker run -it bash
   ls #run similar linux commands to see what the environment looks like
   exit
   ```
   -i: This starts the container in interactive mode   
   -t: Allocates a pseudo-TTY
   
 * Start again the container you exited interactively:
 
    ```sh
   docker start -a -i my-container # replace 'my-container' with your container ID or name 
   exit
   ```
   
> **_Food for brain:_**
>
> * You just exited the container but looks like it is still hanging around. Can you explain?
   
By default a container’s file system persists even after the container exits. This can fill up easily your disk space. To remove a container from your system you should run:

   ```sh
   docker rm my-container # replace 'my-container' with the container ID or name to be removed
   docker rm $(docker ps -a -q) # this removes all stopped containers
   ```
   
> **_Food for brain:_**
>
> * What happened to the corresponding images of the deleted containers? Can you still make new instances (or containers) from the same images? 
> * Start a container interactively from the `bash` image and create a file (e.g. `echo "Hello World!" > myfile`), then exit the container and start another container. What happened to your data?


* Now let's run the latest Ubuntu in a container!

   ```sh
   docker run -it --rm -v $PWD:/my-first-docker ubuntu /bin/bash 
   ```
   
  --rm: Docker will automatically clean up the container and remove the file system when the container exits  
  -v: this mounts a file or directory on the host machine into a container
 
   
   ```sh
   cat /etc/os-release
   whoami
   cd /my-first-docker #Whatever changes you make in this directory will also be made on your host so be careful!
   echo "Hello World!" > hello-world.txt
   ls
   exit
   ls
   ```
  
So despite having different machines with different OS and OS versions you had one thing running in common - the latest Ubuntu!
    
### <a name="create-image"></a> 4. Create Python image to be converted to Singularity

* Let's create a Python image using a Dockerfile

   ```sh
   mkdir my-python2-container
   cd my-python2-container/
   ```
   
   Dockerfile: A file that contains all the commands used to assemble an image. 

* We will create an image and run a simple Python script with it. Download the script in your current working directory:

   ```sh
   wget https://raw.githubusercontent.com/maithili-k/singularity-course/master/python2.py
   ```

* Open a an empty file with your favourite text editor and copy the following text in it. Save the file with name `Dockerfile` and do not add any extension (.txt,.doc) to it:

   ```sh
   # Use an official Python runtime as a parent image
   FROM python:2.7 
   # Copy the Python script to the container
   ADD python2.py . 
   # Install any needed packages 
   RUN apt-get update && apt-get install -y vim
   # Run my-python2-script.py when the container launches
   CMD ["python", "./python2.py"]
   ```
   
*  Now let's build an image from the Dockerfile and run it:
   
   ```sh
   docker build -t python2-docker .
   docker images # You should see the image we just created
   docker run --rm python2-docker 
   docker run -it --rm python2-docker /bin/bash # For an interactive session
   python python2.py # you can run the python script that now resides in your container
   exit
   ```

So in a short amount of time, you just ran a Python script in a Python version that was probably different than the one on your laptop, and ran the latest version of Ubuntu without installing either one of it! 


<!---#http://www.scmgalaxy.com/tutorials/location-of-dockers-images-in-all-operating-systems/>

