# Running docker on your workstation

1. [Save docker images](#save-docker)
2. [Convert Docker images to Singularity](#check-docker)

### <a name="save-docker"></a> 1. Save docker images

   ```sh
   docker images #Check the IMAGE ID of your image
   docker save 0ff753f19523 > python2-for-cartesius.tar #Replace 0ff753f19523 with your Image ID
   ```
   
 Save Docker images from containers
 
   ```sh
   docker ps #Check the Container ID of your image
   docker export pedantic_payne -o python2-container-for-cartesius.tar #Replace pedantic_payne with your Container Name/ID
   ```
   
