# Test Salt Formulas and States with ease

This is an example repo, showing how salt configuration can be (regression) tested with use of [Testinfra](http://testinfra.readthedocs.org/).

## Directory layout

 - `salt` - The Salt states and formula
 - `pillar` - Salt pillar data
 - `test` - The actual tests
 - `vagrant` - Contains Vagrant configuration for easy testing (our development machine, so to speak).

## Getting started
 
First make sure you have Vagrant (1.8.1+) installed. From a terminal, enter the `vagrant` folder and launch the Vagrant box:

    $ vagrant up
    
This will prepare a test machine, Don't worry, you can still change your salt formulas and tests locally.

One the machine is booted, log in to the machine and go to the folder containing the tests. From there you can run the tests:

    $ vagrant ssh
    ...
    $ cd /srv/test
    $ testinfra -v
    
This (demo) setup contains two setups: one for CentOS 7 and one for Ubuntu 15.

The Salt states are tested against both configurations.



    
