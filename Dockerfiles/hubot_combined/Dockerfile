#Hubot Centos Build
#
# VERSION 0.1

FROM centos
MAINTAINER Daniel Kenner <daniel@expresstek.us>

#install basics
#much of this first part was shamelessly "borrowed" from http://www.fullybaked.co.uk/articles/install-hubot-on-centos-6-4-64bit
#I know the || true isn't great to have in here but it fixes a problem with systemd not being installed because it's docker.
RUN yum -y update || true

RUN yum -y groupinstall 'Development tools' || true

#wget is required(ish), nano is just nice.

RUN yum -y install nano wget git

#grab node.js

RUN wget -O /usr/local/src/node-js.tar.gz http://nodejs.org/dist/v0.10.31/node-v0.10.31.tar.gz

RUN tar -xzf /usr/local/src/node-js.tar.gz -C /usr/local/src

RUN cd /usr/local/src/node-v0.10.31 && ./configure && make && make install

RUN npm install -g coffee-script hubot

#here is where Redis would have to be installed. However, I could not easily get redis to install/startup because docker doesn't use the service daemon. To get around this I decided it would probably be best just to use a redis docker image, which works well. This is included at the end.

RUN cd && hubot --create hubot && cd hubot && npm install

#now we need to install hubot IRC
#from https://github.com/nandub/hubot-irc

RUN cd && cd hubot && npm install hubot-irc --save && npm install

#hubot is now installed, what follows is support structures for requested modules

#now we need to install the python stuff for snmp and the juniper dhcp update
#let's do the juniper first

RUN yum -y install python-setuptools python-devel libxml2-devel libxslt-devel gcc openssl

RUN easy_install pip

RUN pip install junos-eznc

#That's the juniper part set up, now for snmp

RUN pip install pysnmp

#alright, background setup is complete. Now we can get the updated scripts (which should be in a github repo by this point) and move them into place

RUN cd && git clone https://github.com/eXpressTek/xt_hubot_scripts.git && cp /xt_hubot_scripts/start_hubot.sh /start_hubot.sh && cp -R /xt_hubot_scripts/* /hubot/scripts

#now that the scripts are in place, they should load when hubot loads

ENTRYPOINT /start_hubot.sh