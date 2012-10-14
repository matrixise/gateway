.. _quickstart:

Quickstart
==========

Eager to get started?  This page gives a good introduction to Gateway.  It
assumes you already have Gateway installed.  If you do not, head over to the
:ref:`installation` section.


A Minimal Application
---------------------

A minimal Gateway application looks something like this

.. sourcecode:: bash
    
    cd examples/json

.. literalinclude:: ../examples/json/main.py
    :language: python


Just save it as `main.py` (or something similar) and run it with your Python
interpreter.  

::

    $ gateway db_create --app=main:application
    $ gateway run --app=main:application
     * Running on http://127.0.0.1:5000/

Now head over to `http://127.0.0.1:5000/ <http://127.0.0.1:5000/>`_, and you
should see your Gateway app.

The Client
~~~~~~~~~~

For the simulation of the client, there is a script in the examples directory::

    $ python client.py

.. literalinclude:: ../examples/json/client.py
    :language: python

The Worker
~~~~~~~~~~

Now if you want to execute the worker, you can use the Worker example in
the examples directory

.. literalinclude:: ../examples/json/worker.py
    :language: python


To execute it, just run it with the command::

    $ python worker


But you can check the status of the Queue or the Worker with the `rqinfo`
command distributed by python-rq::

    $ rqinfo


Native Converter
----------------
Now you can use the default format (native) for the converter. 
Here is an example

.. literalinclude:: ../examples/native/main.py
    :language: python
    