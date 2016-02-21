include:
  - docker.docker-py

ubuntu15-salt:
  dockerng.image_present:
    - build: /srv/test/ubuntu15-salt
    - require:
      - sls: docker.docker-py

