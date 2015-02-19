## Docker/Fig demo for OSX or Linux

This demo shows how easy it can be to get started with docker 
in a distributed environment using fig for orchestration.  
Setup instructions are included for OSX and Linux

### Tool setup for all environments

Visit the links below and install the software as per their instructions:

[Install Docker here](https://docs.docker.com/installation/mac/)

[Install Vagrant here](http://www.vagrantup.com/downloads.html)

[Install Virtualbox here](https://www.virtualbox.org/wiki/Downloads)


### Tool setup for Linux
[Install Fig here](http://www.fig.sh/)


### Tool setup for OSX
[Install boot2docker here](http://boot2docker.io/)

Setup boot2docker by running the installer.
In the future you will need to start boot2docker manually by running:

`$ boot2docker start`

Boot2docker tells you to export some variables when it runs, 
we need to put them somewhere they'll be exported on boot.
I put mine at the end of my ~/.bash_profile:

	$ export DOCKER_HOST=tcp://192.168.59.103:2376
	$ export DOCKER_CERT_PATH=/Users/corylee/.boot2docker/certs/boot2docker-vm
	$ export DOCKER_TLS_VERIFY=1
  
Then run:

`$ source ~/.bash_profile`

`$ docker version` // ---> should see no errors


Next we will install homebrew:

[Install homebrew](http://brew.sh/)


It is important to note that if you dont update brew, included below, that you may receive an elusive error: 'illegal command: 4'.  Run the following commands to install fig:

	$ brew update 
	$ brew install python
	$ brew install fig


### Run the app
#### OSX

	$ boot2docker start
	$ fig up
	$ boot2docker ip // ---> 192.168.59.103

Use the ip address from the previous step in addition to the ports specified in the fig.yml:

	$ curl 192.168.59.103:5000 // HTTP Response body from webserver 1
	$ curl 192.168.59.103:5001 // HTTP Response body from webserver 2
	$ curl 192.168.59.103:5002 // HTTP Response body from webserver 3

Stop boot2docker with the following command:

`$ boot2docker stop`


#### Linux
	$ fig up
	$ curl localhost:5000 // HTTP Response body from webserver 1
	$ curl localhost:5001 // HTTP Response body from webserver 2
	$ curl localhost:5002 // HTTP Response body from webserver 3