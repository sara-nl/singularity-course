# Running docker on your workstation

1. [Start docker daemon](#start-docker)
2. [Environment set up](#cartesius-env)
3. [Submit a job](#job-submit)

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
 
  
### Check the docker installation

* This command downloads a test image and runs it in a container. 

    ```sh
    sudo docker run hello-world
    ```




