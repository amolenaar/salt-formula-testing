include:
  - python.pip

docker-py:
  pip.installed:
    - require:
      - sls: python.pip
