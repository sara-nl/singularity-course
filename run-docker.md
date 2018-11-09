# Running docker on your workstation

1. [Start docker daemon](#start-docker)
2. [Test Docker installation](#check-docker)

### <a name="start-docker"></a> 1. Start docker daemon

* Linux: Open a terminal in your laptop

    ```sh
    sudo systemctl start docker
    ```
    or 
    ```sh
    sudo service docker start
    ```
* Mac: Start the docker daemon via Launchpad.

* Windows: Search for Docker, select Docker for Windows in the search results, and click it (or hit Enter)
 
  
### <a name="check-docker"></a> 2. Check the docker installation

* Run the following command in a terminal. This command downloads a test image and runs it in a container. 

    ```sh
    docker --version
    docker run hello-world
    ```
Image: An image is an executable package that includes everything needed to run an application.    
Container: A container is a runtime instance of an image--what the image becomes when executed. 


