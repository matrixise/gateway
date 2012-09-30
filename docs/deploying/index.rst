.. _deployment:

Deployment Options
==================

Depending on what you have available there are multiple ways to run
Gateway applications. You can use the builtin server during development,
but you should use a full deployment option for production applications.

(Do not use the builtin development server in production.) Several options
are available and documented here

If you have a different WSGI server look up the server documentation about
how to use a WDGI app with it. Just remember that you :class:`GatewayApp` 
application object is the actual WSGI application.

.. toctree::
    :maxdepth: 2

    wsgi-standalone
