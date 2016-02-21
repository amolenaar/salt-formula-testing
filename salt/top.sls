base:
  'salt-dev':
    - docker
    - testinfra
    - docker.centos7-salt
    - docker.ubuntu15-salt

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
