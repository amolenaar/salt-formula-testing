java-jdk-1.8:
  pkg.installed:
    - pkgs:
    {% if grains['os_family'] == 'RedHat' %}
       - java-1.8.0-openjdk-devel
    {% elif grains['os_family'] == 'Debian' %}
       - openjdk-8-jdk
    {% endif %}
