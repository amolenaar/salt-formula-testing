
jenkins:
  group:
    - present
  user:
    - present
    - home: /var/lib/jenkins
    - shell: /bin/bash
    - groups:
      - jenkins
    - require:
      - group: jenkins

jenkins-master-key:
  ssh_auth.present:
    - name: {{ pillar['jenkins']['pub-key'] }}
    - makedirs: True
    - mode: 600
    - user: jenkins
    - group: jenkins

jenkins_known_hosts_github:
  ssh_known_hosts.present:
    - name: github.com
    - user: jenkins
    - fingerprint: 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48

