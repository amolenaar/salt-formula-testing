import sys
import pytest
import testinfra

# docker run -i -t -v /srv/salt/:/srv/salt -v /srv/pillar/:/srv/pillar/ -v /srv/files/:/srv/files/ salt-test-base /bin/bash

@pytest.fixture(scope='module', params=['centos7-salt', 'ubuntu15-salt'])
def Docker(request, LocalCommand):
    """
    Boot and stop a docker image. The image is primed with salt-minion.
    """
    # Run a new container. Run in privileged mode, so systemd will start
    docker_id = LocalCommand.check_output("docker run --privileged -d -v /srv/salt/:/srv/salt -v /srv/pillar/:/srv/pillar/ %s", request.param)

    def teardown():
        LocalCommand.check_output("docker kill %s", docker_id)
        LocalCommand.check_output("docker rm %s", docker_id)

    # At the end of each test, we destroy the container
    request.addfinalizer(teardown)

    return testinfra.get_backend("docker://%s" % (docker_id,))


def docker_backend_provision_as(self, minion_id):
    """
    Provision the image with Salt. The image is provisioned as if it were a minion with name `minion_id`.
    """
    Command = self.get_module("Command")
    print 'Executing salt-call locally for id', minion_id
    cmd = Command("salt-call --local --force-color --retcode-passthrough --id=%s.testenv state.highstate", minion_id)
    sys.stdout.write(cmd.stdout)
    #sys.stderr.write(cmd.stderr)
    assert cmd.rc == 0
    return cmd


testinfra.backend.docker.DockerBackend.provision_as = docker_backend_provision_as


@pytest.fixture
def Slow():
    """
    Run a slow check, check if the state is correct for `timeout` seconds.
    """
    import time
    def slow(check, timeout=30):
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
    return  slow

# vim:sw=4:et:ai
