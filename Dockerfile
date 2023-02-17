FROM jenkins/jenkins:lts-jdk11

# Running as root to have an easy support for Docker
USER root
 
# Jenkins init scripts
COPY init.groovy.d /usr/share/jenkins/ref/init.groovy.d

# Install Jenkins plugins
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/plugins.txt

RUN curl -fsSL https://get.docker.com -o get-docker.sh
RUN sh get-docker.sh

