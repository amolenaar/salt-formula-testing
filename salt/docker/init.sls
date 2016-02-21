docker:
  pkg:
    - installed
  group.present:
    - addusers:
       - vagrant
  service.running:
    - enable: True

