
import pytest

HOST_ID = "jenkins.test"


@pytest.fixture(scope="module", autouse=True)
def provision(Docker):
    Docker.provision_as(HOST_ID)


def test_service_running(Docker):
    Service = Docker.get_module("Service")
    assert Service("jenkins").is_running


def test_service_listening_on_port_8080(Docker, Slow):
    import time
    Socket = Docker.get_module("Socket")
    Slow(lambda: Socket("tcp://:::8080").is_listening)


# vim:sw=4:et:ai
