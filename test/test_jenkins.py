
import pytest

HOST_ID = "jenkins"


@pytest.fixture(scope="module", autouse=True)
def provision(Docker):
    Docker.provision_as(HOST_ID)


def test_service_running(Docker):
    Service = Docker.get_module("Service")
    assert Service('jenkins').is_running


def wait_for(check, timeout=30):
    import time
    timeout_at = time.time() + timeout
    while True:
        try:
            assert check()
        except AssertionError, e:
            if timeout_at < time.time():
                time.sleep(1)
            else:
                raise e
        else:
            return


def test_service_listening_on_port_8080(Docker):
    import time
    Socket = Docker.get_module("Socket")
    wait_for(lambda: Socket("tcp://:::8080").is_listening)


# vim:sw=4:et:ai
