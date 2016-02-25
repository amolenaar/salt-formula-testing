import pytest
import testinfra


target_boxes = ['centos7-salt', 'ubuntu15-salt']


def root_dir():
    """
    Figure out the project base dir (parent folder of file)
    """
    from os.path import dirname
    return dirname(dirname(__file__))


@pytest.fixture(scope='module', params=target_boxes)
def image_name(request):
    """
    This fixture returns the image names to test against.
    Override this fixture in your module if you need to test with different images.
    """
    return request.param


@pytest.fixture(scope='module')
def docker_image(image_name, LocalCommand):
    cmd = LocalCommand("docker build -t %s %s", image_name, image_name)
    assert cmd.rc == 0
    return image_name
    

@pytest.fixture(scope='module')
def Docker(request, docker_image, LocalCommand):
    """
    Boot and stop a docker image. The image is primed with salt-minion.
    """
    base = root_dir()
    print 'Project base dir is:', base

    # Run a new container. Run in privileged mode, so systemd will start
    docker_id = LocalCommand.check_output("docker run --privileged -d -v %s/salt/:/srv/salt -v %s/pillar/:/srv/pillar/ %s", base, base, docker_image)

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
    print cmd.stdout
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
