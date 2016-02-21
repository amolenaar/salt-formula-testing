include:
  - python.pip

docker-py:
  pip.installed:
    - require:
      - sls: python.pip

centos7-salt:
  dockerng.image_present:
    - build: /srv/test/centos7-salt


