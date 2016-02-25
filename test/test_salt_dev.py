"""
Self-test.
Test the configuration of our own salt-dev machine. The salt-dev box is Ubuntu.
"""

import pytest

HOST_ID = "salt-dev"


@pytest.fixture(scope="module", autouse=True)
def provision(Docker):
    Docker.provision_as(HOST_ID)


@pytest.fixture(scope="module")
def image_name():
    """
    Override images to support: only Ubuntu.
    """
    return "ubuntu15-salt"


def test_docker_installed(Docker):
    File = Docker.get_module("File")
    docker = File("/usr/bin/docker")
    assert docker.exists
    assert docker.mode & 0555


def test_docker_running(Docker):
    File = Docker.get_module("File")
    sock = File("/var/run/docker.sock")
    assert sock.exists
    assert sock.group == "docker"
    assert sock.mode == 0660


def test_testinfra_installed(Docker):
    File = Docker.get_module("File")
    testinfra = File("/usr/local/bin/testinfra")
    assert testinfra.exists
    assert testinfra.mode & 0555

# vim: sw=4:et:ai
