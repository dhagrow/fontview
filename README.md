fontview
========

A font and styling previewer for programmers.

Hosted at: http://fonts.dhagrow.org/
by [OpenShift](https://www.openshift.com/).

Requirements
------------

fontview is written for [Python 3](http://www.python.org/) using [Bottle](http://bottlepy.org/),
[Waitress](http://docs.pylonsproject.org/projects/waitress/), and
[Pygments](http://pygments.org/).

On the client-side are [jQuery](http://jquery.com/), [Bootstrap 3](http://getbootstrap.com/),
and [WebFont Loader](https://github.com/typekit/webfontloader).

Getting Started
---------------

To use fontview, first setup and activate a virtual environment::

    $ virtualenv env -p /usr/bin/python3
    $ . env/bin/activate

Install the requirements::

    pip install -r requirements.txt

Then, start the server (currently starts on port 22344)::

    python wsgi/app.py

