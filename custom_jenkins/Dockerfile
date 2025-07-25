# use the jenkins image as the base image
FROM jenkins/jenkins:lts

# switch to root user to install dependencies
USER root

# install prerequisites and dependencies
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean


# add jenkins user to the docker group( create the group if it doesn't exist)
RUN groupadd -f docker && \
    usermod -aG docker jenkins


# create the docker directory and volume for DinD
RUN mkdir -p /var/lib/docker 
VOLUME /var/lib/docker

# switch back to jenkins user
USER jenkins
