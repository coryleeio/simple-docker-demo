## Docker/fig demo for OSX using boot2docker.

This setup will assume your running macOSX simply because it's incredibly trivial to run it on linux just install docker, vagrant, virtualbox, and fig.  Then run fig -f 'fig-production.yml' up

### Tool setup for everyone:
[Install Docker here](https://docs.docker.com/installation/mac/)
[Install Vagrant here](http://www.vagrantup.com/downloads.html)
[Install Virtualbox here](https://www.virtualbox.org/wiki/Downloads)
[Install boot2docker here](http://boot2docker.io/)


### Tool setup for macOSX
Mac users setup boot2docker
run the installer... boot2docker
this will automatically run:
`boot2docker start`

boot2docker tells you to export some variables, put them somewhere they'll be run on boot...
get your own variables from boot2docker start
in .bash_profile:
   `export DOCKER_HOST=tcp://192.168.59.103:2376
   export DOCKER_CERT_PATH=/Users/corylee/.boot2docker/certs/boot2docker-vm
   export DOCKER_TLS_VERIFY=1`
   then run:
`source ~/.bash_profile`

### Test Docker installation
no ssh is needed, just type:
`docker version` // ---> should see no errors

### Docker is functioning, Now lets get fig working:
#### Fig installation for mac:
install homebrew
http://brew.sh/

brew update
brew install python
brew install fig

#### Fig installation for everyone else:
[Click here to install fig](http://www.fig.sh/)

### Test Docker:
`docker run --name mynginx1 -P -d nginx
docker ps   // ---> 0.0.0.0:49153->443/tcp, 0.0.0.0:49154->80/tcp 
boot2docker ip // ---> 192.168.59.103
curl 192.168.59.103:49154  // ---> http
curl https://192.168.59.103:49153 -k // ---> https

docker ps // ---> f713327106b6        nginx:latest        "nginx -g 'daemon of   10 minutes ago  

docker stop f71
docker rm f71
boot2docker stop`




