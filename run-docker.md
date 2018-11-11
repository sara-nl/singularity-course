# Running docker on your workstation

1. [Start docker daemon](#start-docker)
2. [Check Docker installation](#check-docker)
3. [Run interactive containers](#run-interactive)
4. [Create a Python image to be used to run on Cartesius](#create-image) 

### <a name="start-docker"></a> 1. Start docker daemon

Let us first start the docker daemon: 

* Linux: Open a terminal in your laptop and run

    ```sh
    $sudo systemctl start docker
    ```
    if the above command fails run 
    ```sh
    $sudo service docker start
    ```
* Mac: Start the docker daemon via Launchpad.

* Windows: Search for Docker, select Docker for Windows in the search results, and click it (or hit Enter)
 
  
### <a name="check-docker"></a> 2. Check the docker installation

* Getting started: Run the following commands in a terminal 

    ```sh
    $docker --version
    $docker info
    $docker image ls
    $docker container ls --all
    ```

Image: An image  is an executable package that includes everything needed to run an application.    
Container: A container is a runtime instance of an image - what the image becomes when executed. 

* This command downloads a test image and runs it in a container. 


    ```sh
    $docker run hello-world
    $docker image ls  # can you see your hello-world image?
    $docker container ls --all   # can you see your hello-world container?
    ```  
    
### <a name="run-interactive"></a> 3. Run interactive containers

* The following command downloads the latest bash image and runs it in the interactive mode

   ```sh
   $docker run -it bash
   $ls #run similar linux commands to see what the environment looks like
   $exit
   $docker container ls -all  # or docker ps -a
   ```
   -i: This starts the container in interactive mode   
   -t: Allocates a pseudo-TTY
   
By default a container’s file system persists even after the container exits. To remove the container (this does not remove the image) you should run

   ```sh
   $docker rm container-name # replace with your container-name
   $docker rm $(docker ps -a -q) # this removes all stopped containers
   ```
   
Now let's run the latest Ubuntu in a container!

   ```sh
   $docker run -it --rm -v $PWD:/my-first-docker ubuntu /bin/bash 
   ```
   
  --rm: Docker will automatically clean up the container and remove the file system when the container exits  
  -v: this mounts a file or directory on the host machine into a container
 
   
   ```sh
   $cat /etc/os-release
   $whoami
   $cd /my-first-docker #Whatever hcanges you make in this directory will also be made on your host so be careful!
   $echo "Hello World!" > hello-world.txt
   $ls
   $exit
   $ls
   ```
  
So you all have different machines with different OS and OS versions but one thing running in common - the latest Ubuntu!

If you wish to remove all your containers/did not use the --rm flag you can run the following command:

   ```sh
   $docker rm $(docker ps -a -q) # this removes all stopped containers
   ```
    
### <a name="create-image"></a> 4. Create Python images to be used to run on Cartesius

In the section we will create a Python image
   ```sh
   $mkdir my-python2-container
   $cd my-python2-container/
   $vi (check which editor Carlos used) Dockerfile
   ```

The content of the Dockerfile should look like this:
   ```sh
   # Use an official Python runtime as a parent image
   FROM python:2.7 
   # Copy the Python script to the container
   ADD my-python2-script.py . 
   # Run my-python2-script.py when the container launches
   CMD ["python", "./my-python2-script.py"]
   ```
    
   $docker build -t python-for-cartesius .
   $docker run --rm python-for-cartesius /bin/bash

<!---#http://www.scmgalaxy.com/tutorials/location-of-dockers-images-in-all-operating-systems/>

