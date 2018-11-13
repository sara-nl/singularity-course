# Building Singularity images

singularity build python-2.7.simg docker://python:2.7.15-jessie

1. [Convert Docker images to Singularity](#convert-docker)

### <a name="convert-docker"></a> 1. Convert Docker images to Singularity

 Save Docker images from containers
 
   ```sh
   sudo docker run -v /var/run/docker.sock:/var/run/docker.sock --privileged -t --rm singularityware/docker2singularity    python2-for-cartesius
   ```
   
