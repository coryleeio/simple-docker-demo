## Docker/fig demo for OSX or linux

This demo shows how easy it can be to get started with docker in a distributed environment using
fig for orchestration.

### Tool setup for everyone:
[Install Docker here](https://docs.docker.com/installation/mac/)

[Install Vagrant here](http://www.vagrantup.com/downloads.html)

[Install Virtualbox here](https://www.virtualbox.org/wiki/Downloads)


### Tool setup for OSX:
[Install boot2docker here](http://boot2docker.io/)

setup boot2docker by running the installer.
in the future you will need to start boot2docker manually by running:

`boot2docker start`

boot2docker tells you to export some variables, put them somewhere they'll be run on boot...
get your own variables from boot2docker start
in .bash_profile:

`export DOCKER_HOST=tcp://192.168.59.103:2376`

`export DOCKER_CERT_PATH=/Users/corylee/.boot2docker/certs/boot2docker-vm`

`export DOCKER_TLS_VERIFY=1`
  
then run:
`source ~/.bash_profile`

no ssh is needed, just type:
`docker version` // ---> should see no errors


### Docker is functioning, Now lets get fig working:
#### Fig installation for mac:
install homebrew
http://brew.sh/

`brew update`

`brew install python`

`brew install fig`


#### Fig installation for everyone else:
[Install fig here](http://www.fig.sh/)


### Test Docker:
#### OSX:
`boot2docker start`

`fig up`

`boot2docker ip` // ---> 192.168.59.103

`curl 192.168.59.103:5000` // hit webserver 1

`curl 192.168.59.103:5001` // hit webserver 2

`curl 192.168.59.103:5002` // hit webserver 3


#### Everyone else:
`fig up`

`curl localhost:5000` // hit webserver 1

`curl localhost:5001` // hit webserver 2

`curl localhost:5002` // hit webserver 3
