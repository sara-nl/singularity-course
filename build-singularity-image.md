# Building Singularity images

1. [Convert Docker images to Singularity](#convert-docker)
2. [Pull Singularity images](#pull-singularity)
3. [Build Singularity images from a recipe](#build-singularity)

### <a name="convert-docker"></a> 1. Convert Docker images to Singularity

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
   
### <a name="pull-singularity"></a> 2. Pull Singularity images
 
You will need Singularity installed on your workstation to proceed. If you did not manage to perform this, the below steps  will be shown in the demo.
 
### <a name="build-singularity"></a> 3. Build Singularity images from a recipe

You will need Singularity installed on your workstation to proceed. If you did not manage to perform this, the below steps  will be shown in the demo.

 
 singularity build python-2.7.simg docker://python:2.7.15-jessie

