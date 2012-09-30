.. _installation:

Installation
============

GatewayApp depends on external libraries, 
`Flask <http://flask.pocoo.org>`_, `Python-RQ <http://python-rq.org>`_ and 
`Werkzeug <http://werkzeug.pocoo.org>`_.

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good 
intentions.

RQ (Redis Queue) is a simple Python library for queueing jobs and processing 
them in the background with workers. It is backed by Redis and it is designed 
to have a low barrier to entry. It should be integrated in your web stack
easily.

You will need Python 2.5 or higher to get started, so be sure to have an
up-to-date Python 2.x installation. At the time of writing, the WSGI 
specification has not yet been finalized for Python 3, so Gateway cannot support
the 3.x series of Python.

.. _virtualenv:

virtualenv
----------

Virtualenv is probably what you want to use during development, and if you have
shell access to your production machines, you'll probably want to use it there,
too.

What problem does virtualenv solve?  If you like Python as much as I do,
chances are you want to use it for other projects besides Flask-based web
applications.  But the more projects you have, the more likely it is that you
will be working with different versions of Python itself, or at least different
versions of Python libraries.  Let's face it: quite often libraries break
backwards compatibility, and it's unlikely that any serious application will
have zero dependencies.  So what do you do if two or more of your projects have
conflicting dependencies?

Virtualenv to the rescue!  Virtualenv enables multiple side-by-side
installations of Python, one for each project.  It doesn't actually install
separate copies of Python, but it does provide a clever way to keep different
project environments isolated.  Let's see how virtualenv works.

If you are on Mac OS X or Linux, chances are that one of the following two
commands will work for you::

    $ sudo easy_install virtualenv

or even better::

    $ sudo pip install virtualenv

One of these will probably install virtualenv on your system.  Maybe it's even
in your package manager.  If you use Ubuntu, try::

    $ sudo apt-get install python-virtualenv

Once you have virtualenv installed, just fire up a shell and create
your own environment.  I usually create a project folder and a `venv`
folder within::

    $ mkdir myproject
    $ cd myproject
    $ virtualenv venv
    New python executable in venv/bin/python
    Installing distribute............done.

Now, whenever you want to work on a project, you only have to activate the
corresponding environment.  On OS X and Linux, do the following::

    $ . venv/bin/activate

If you are a Windows user, the following command is for you::

    $ venv\scripts\activate

Either way, you should now be using your virtualenv (notice how the prompt of
your shell has changed to show the active environment).

Now you can just enter the following command to get Gateway activated in your
virtualenv::

    $ pip install Gateway

A few seconds later and you are good to go.


System-Wide Installation
------------------------

This is possible as well, though I do not recommend it.  Just run
`pip` with root privileges::

    $ sudo pip install Gateway

(On Windows systems, run it in a command-prompt window with administrator
privileges, and leave out `sudo`.)


Living on the Edge
------------------

If you want to work with the latest version of Gateway, there are two ways: you
can either let `pip` pull in the development version, or you can tell
it to operate on a git checkout.  Either way, virtualenv is recommended.

Get the git checkout in a new virtualenv and run in development mode::

    $ git clone http://github.com/matrixise/gateway.git
    Initialized empty Git repository in ~/dev/gateway/.git/
    $ cd gateway
    $ virtualenv venv --distribute
    New python executable in venv/bin/python
    Installing distribute............done.
    $ . venv/bin/activate
    $ python setup.py develop
    ...
    Finished processing dependencies for Gateway

This will pull in the dependencies and activate the git head as the current
version inside the virtualenv.  Then all you have to do is run ``git pull
origin`` to update to the latest version.

To just get the development version without git, do this instead::

    $ mkdir gateway
    $ cd gateway
    $ virtualenv venv --distribute
    $ . venv/bin/activate
    New python executable in venv/bin/python
    Installing distribute............done.
    $ pip install Gateway==dev
    ...
    Finished processing dependencies for Gateway==dev
