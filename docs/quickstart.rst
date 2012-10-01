.. _quickstart:

Quickstart
==========

Eager to get started?  This page gives a good introduction to Gateway.  It
assumes you already have Gateway installed.  If you do not, head over to the
:ref:`installation` section.


A Minimal Application
---------------------

A minimal Gateway application looks something like this

.. literalinclude:: ../examples/main.py
    :language: python


Just save it as `hello.py` (or something similar) and run it with your Python
interpreter.  Make sure to not call your application `flask.py` because this
would conflict with Flask itself.

::

    $ gateway db_create --app=hello:application
    $ gateway run --app=hello:application
     * Running on http://127.0.0.1:5000/

Now head over to `http://127.0.0.1:5000/ <http://127.0.0.1:5000/>`_, and you
should see your Gateway app.