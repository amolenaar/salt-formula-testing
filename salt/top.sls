base:
  'salt-dev':
    - docker
    - testinfra

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
