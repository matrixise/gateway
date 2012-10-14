=======
Gateway
=======

Gateway is a program that runs over the Redis Queue with a WSGI layer.

Gateway can be used as a library or through the command line.

For the documentation:

Create a virtualenv
-------------------

.. sourcecode:: bash

    # pip install virtualenv
    $ virtualenv ~/.virtualenvs/gateway
    $ source ~/.virtualenvs/gateway
    $ cd gateway/

Install the requirements
------------------------

.. sourcecode:: bash

    $ pip install -r pip-requirements.txt
    $ pip install -r dev-requirements.txt

Fetch the default theme for the documentation
---------------------------------------------

.. sourcecode:: bash

    $ git submodule init
    $ git submodule update

Generate the documentation
--------------------------

.. sourcecode:: bash

    $ python setup.py develop
    $ make docs
