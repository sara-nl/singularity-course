# Running singularity examples on Cartesius

Here are your first steps:

1. [Login to Cartesius](#cartesius-login)
2. [Environment set up](#cartesius-env)
3. [Submit a job](#job-submit)

### <a name="cartesius-login"></a> 1. Login to Cartesius

* The login credentials will be provided to you at the start of the session.
* Open a terminal in your laptop
  * Windows users only: 
    * Make sure that Xming program is running. If not, start it first.
    * Type the following commands to prepare your environment support graphical windows (press enter to submit each command):
  
  
    ```sh
    echo "export DISPLAY=localhost:0.0" >> $HOME/.bashrc
    source $HOME/.bashrc
    ```
    
 ```ss
 ssh username@cartesius.surfsara.nl #replace `username` with the username assigned to you
 ```
  
#### Get familiar with the UI 

* Find your home directory and its content:

```sh
pwd

ls -l
```


