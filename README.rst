=======
Gateway
=======

Gateway is a program that runs over the Redis Queue with a WSGI layer.

Gateway can be used as a library or through the command line.

For the documentation:

1. Create a virtualenv
# pip install virtualenv
$ virtualenv ~/.virtualenvs/gateway
$ source ~/.virtualenvs/gateway
$ cd gateway/

2. Install the requirements
$ pip install -r pip-requirements.txt
$ pip install -r dev-requirements.txt

3. Fetch the default theme for the documentation
$ git submodule init
$ git submodule update

4. Generate the documentation
$ python setup.py develop
$ make docs
