jenkins:
  {% if grains['os_family'] in ['RedHat', 'Debian'] %}
  pkgrepo.managed:
    - humanname: Jenkins upstream package repository
    {% if grains['os_family'] == 'RedHat' %}
    - baseurl: http://pkg.jenkins-ci.org/redhat
    - gpgkey: http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key
    {% elif grains['os_family'] == 'Debian' %}
    - file: /etc/apt/sources.list.d/jenkins-ci.list
    - name: deb http://pkg.jenkins-ci.org/debian binary/
    - key_url: http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key
    {% endif %}
    - require_in:
      - pkg: jenkins
  {% endif %}
  pkg.installed:
    - pkgs:
      - jenkins
  service.running:
    - enable: True
    - watch:
      - pkg: jenkins

/var/lib/jenkins/plugins/git.hpi:
  file.managed:
    - source: http://updates.jenkins-ci.org/download/plugins/git/2.3.4/git.hpi
    - source_hash: md5=e3ead2aa0ba8b7666566e0e3dea964e3
    - makedirs: True
    - mode: 640
    - user: jenkins
    - group: jenkins
