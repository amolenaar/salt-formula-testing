#!/usr/bin/bash
#
# Run our test container for manual testing.
#

image=centos7-salt
echo "Launching docker container for $image..."
container_id=`docker run --privileged -d -v /srv/salt/:/srv/salt -v /srv/pillar/:/srv/pillar/ -v /srv/binaries/:/srv/binaries/ $image`

echo "To start the provisioning by hand, invoke:"
echo "salt-call --local --id=<mymachine>.testenv state.highstate"

docker exec -ti $container_id bash

echo -n "Shutting down the container..."
docker kill $container_id > /dev/null
docker rm $container_id > /dev/null
echo " done."
