# Running docker on your workstation

1. [Start docker daemon](#start-docker)
2. [Test Docker installation](#check-docker)
3. [Run interactive containers](#run-interactive)

### <a name="start-docker"></a> 1. Start docker daemon

* Linux: Open a terminal in your laptop and run

    ```sh
    sudo systemctl start docker
    ```
    if the above command fails run 
    ```sh
    sudo service docker start
    ```
* Mac: Start the docker daemon via Launchpad.

* Windows: Search for Docker, select Docker for Windows in the search results, and click it (or hit Enter)
 
  
### <a name="check-docker"></a> 2. Check the docker installation

* Getting started: Run the following commands in a terminal 

    ```sh
    docker --version
    docker info
    docker image ls
    docker container ls --all
    ```

Image: An image  is an executable package that includes everything needed to run an application.    
Container: A container is a runtime instance of an image--what the image becomes when executed. 

* This command downloads a test image and runs it in a container. 


    ```sh
    docker run hello-world
    docker image ls  # can you see your hello-world image?
    docker container ls --all   # can you see your hello-world container?
    ```  
    
### <a name="run-interactive"></a> 3. Run interactive containers

* The following command downloads the bash:latest image and runs it

   ```sh
   docker run -it bash
   docker run -it --rm -v $PWD ubuntu /bin/bash
   
   ```
    
<!---#http://www.scmgalaxy.com/tutorials/location-of-dockers-images-in-all-operating-systems/>

