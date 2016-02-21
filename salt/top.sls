base:
  'salt-dev':
    - docker
    - testinfra
    - docker.centos7-salt

  'jenkins.*':
    - git
    - java
    - jenkins
    - node

  'jenkins-slave*.*':
    - git
    - java
    - jenkins.client
    - node
