FROM ubuntu:15.10

RUN echo 'deb http://repo.saltstack.com/apt/ubuntu/14.04/amd64/latest trusty main' >> /etc/apt/sources.list.d/saltstack.list
COPY SALTSTACK-GPG-KEY.pub /tmp/
RUN apt-key add /tmp/SALTSTACK-GPG-KEY.pub
RUN apt-get update && apt-get install -y salt-minion
COPY minion /etc/salt/

ENTRYPOINT ["/sbin/init"]
