# Building Singularity images

singularity build python-2.7.simg docker://python:2.7.15-jessie

1. [Convert Docker images to Singularity](#convert-docker)

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
