#!/usr/bin/env bash
# set up web server for deployment
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

sudo echo "<!DOCTYPE html>" >> /data/web_static/releases/test/index.html
sudo echo "<html>" >> /data/web_static/releases/test/index.html
sudo echo "  <head>" >> /data/web_static/releases/test/index.html
sudo echo "  </head>" >> /data/web_static/releases/test/index.html
sudo echo "  <body>" >> /data/web_static/releases/test/index.html
sudo echo "    Web Static" >> /data/web_static/releases/test/index.html
sudo echo "  </body>" >> /data/web_static/releases/test/index.html
sudo echo "</html>" >> /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chmod -R u+g /data/

sudo sed -i "s/location \//location \/hbnb_static\//g" /etc/nginx/sites-available/default
sudo sed -i "36 i \            alias /data/web_static/current/;" /etc/nginx/sites-available/default

sudo service nginx restart
