FROM debian:stretch
MAINTAINER dustyfresh, https://github.com/dustyfresh

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install system package updates & system dependencies
RUN apt-get update && \
  apt-get dist-upgrade -y && \
  apt-get install --yes build-essential python3-setuptools python3-pip \
    python3-dev supervisor curl byobu nginx libxml2 libxml2-dev net-tools apache2-utils

# Remove default nginx page
RUN rm /var/www/html/index.nginx-debian.html && rm /etc/nginx/sites-enabled/default

# Create directory structure and add application code to container
RUN mkdir /opt/{python3,app} /opt/app/logs && chown www-data. /opt/app/logs
ADD code/requirements.txt /opt/app/requirements.txt

# We setup a virtual python environment in /opt/python3 and install app modules
RUN cd /opt/python3 && pip3 install virtualenv && \
  virtualenv venv -p python3 && \
  source /opt/python3/venv/bin/activate && \
  pip3 install -r /opt/app/requirements.txt

# Generate self-signed SSL
RUN \
  mkdir /opt/ssl && \
	openssl genrsa -out /opt/ssl/key.pem 4096 && \
	openssl req -new -key /opt/ssl/key.pem -out /opt/ssl/server.csr -subj '/CN=localhost' && \
	openssl x509 -req -days 365 -in /opt/ssl/server.csr -signkey /opt/ssl/key.pem -out /opt/ssl/cert.pem

# add nginx vhost file
ADD conf/vhost.conf /etc/nginx/sites-enabled/default

# Auth file. Default auth is changeme:changeme
ADD conf/.htpasswd /etc/nginx/.htpasswd

# Add supervisord process management configs
ADD conf/supervise-*.conf /etc/supervisor/conf.d/

# Symlink logs to /opt/app/logs
RUN ln -s /var/log/nginx/access.log /opt/app/logs/nginx_access.log && \
  ln -s /var/log/nginx/error.log /opt/app/logs/nginx_error.log

# Add our application code into the container
ADD code/routes /opt/app/routes
ADD code/app.py /opt/app/app.py
ADD code/templates /opt/app/templates
ADD code/static /opt/app/static

RUN chown -R www-data. /opt/app

CMD ["/usr/bin/supervisord", "-n"]
