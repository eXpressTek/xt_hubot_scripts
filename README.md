eXpressTek Hubot Scripts
==========================

This is a collection of scripts for use with a hubot installation to automate a
collection of processes around the lab. At the time of the writing of this readme,
these files are in active development.

This project includes a dockerfile that will generate a centos 7-based hubot server
but does have a couple of requirements and notes:

Building the image
==================

The dockerfile should take care of most of the work, you just have to run it by navigating to the relavant dockerfile (at the time of this writing, the only dockerfile is located in Dockerfiles/hubot_combined) and then run:

sudo docker build .

or 

sudo docker build -t username/repo:tag . (If you wish to specify the name of the new image)

Running the Image
=================

Just a note about actually running the image, there are some environment variables that should be set. Because of how our particular method works, we use IRC, which requires (for the hubot IRC adapter) these environment variables. These can be set when the container is run by calling the -e '<KEY=VAL>'

HUBOT\_IRC\_SERVER - The hostname/ip address of the IRC server you wish to connect to 
HUBOT\_IRC\_ROOMS - The rooms for the bot to join (may or may not require a # at the beginning)
HUBOT\_IRC\_NICK - The nickname that should be used for the bot
HUBOT\_IRC\_PASSWORD - The password for the bot
HUBOT\_IRC\_USESSL - Whether or not to use SSL, if anything is put in this, it will enable ssl

A full list of the IRC environment variable options is available at https://github.com/nandub/hubot-irc

One additional one, if using Hubot with Redis, (using the code below) set the following

REDIS_URL=redis://redis:6379

A Note on Redis
===============

While this can run without a redis database as its brain, it is recommended that it
is used, as such, it is recommended that a redis docker container is used and will be
reflected in the recommended start command listed below. To setup a redis
image/container see https://registry.hub.docker.com/_/redis/ or just run:

docker run --name redis-brain -d redis:latest

With Redis setup

Super-Simple Cut and Paste Example
==========================

Assuming the name of the docker image is hubot\_image

Installation:

(from this folder)

cd Dockerfiles/hubot_combined && sudo docker build . && docker pull redis:latest

Running:

docker run --name redis-brain -d redis:latest && docker run -d --name hubot\_app --link redis-brain:redis -e 'HUBOT\_IRC\_SERVER=irc.example.com' -e 'HUBOT\_IRC\_ROOMS=#general' -e 'HUBOT\_IRC\_NICK=hubot' -e 'HUBOT\_IRC\_PASSWORD=pass' -e 'HUBOT\_IRC\_USESSL=True' -e 'REDIS_URL=redis://redis:6379' hubot\_image
