include:
  - python.pip

testinfra:
  pip.installed:
    - require:
      - sls: python.pip
