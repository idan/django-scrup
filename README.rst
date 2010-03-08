##############
 django-scrup
##############

A django-based web receiver for Scrup_ which stores screencaptures on S3.

.. _Scrup: http://github.com/rsms/scrup/

Features
========

* Receives POST'ed images from scrup and uploads them to S3, and returns a valid URL
  for the image.

There are a few things on the roadmap:

* Giving some consideration to security matters -- right now it's either HTTPS or
  nothing.
* Exception handling.
* Thumbnail generation and storage on S3
* A web-based timeline showing your history of screenshot uploads so you can easily
  find an old screenshot you've uploaded.

Requirements
============

#. Django_ (obviously).
#. Boto_, the python frontend to AWS

.. _Django: http://www.djangoproject.com
.. _Boto: http://code.google.com/p/boto/

Installation
============

Getting django-scrup can be as easy as::
	
	$ pip install django-scrup

in your favorite shell.

If you prefer to pull down and install the package yourself, you can always download or
checkout the `latest release`_ and install via the usual ``python setup.py install``.

.. _`latest release`: http://github.com/idangazit/django-scrup

Configuration and Usage
=======================

First, add ``'scrup'`` to your ``INSTALLED_APPS``. Don't forget to ``./manage.py syncdb``!

You'll also need to define a few values in your ``settings.py``:

``SCRUP_AWS_ACCESS_KEY``
	Your AWS access key.

``SCRUP_AWS_SECRET_KEY``
	Your AWS secret key.

``SCRUP_AWS_BUCKET``
	The bucket in which django-scrup should store the uploaded screenshots. This must
	be a bucket which is writeable by the AWS user identified by the above credentials.
	This bucket should be **solely devoted to the use of django-scrup**, as the app will
	likely barf if it tries to upload a file with the same name as an existing file.
	By default, the uploaded files are stored in the root of the bucket, unless
	``SCRUP_AWS_PREFIX`` is specified.

``SCRUP_AWS_PREFIX``
	**Optional.**
	A relative pathname to a folder within the bucket. If this value is specified,
	uploads will be copied to ``http://yourbucket.s3.amazonaws.com/<SCRUP_AWS_PREFIX>``

``SCRUP_AWS_CNAME``
	**Optional.**
	A boolean value indicating whether to use the bucketname as the domain of the
	returned screenshot URL. If you've created a CNAME for your bucket, set this to
	``True`` and the returned URLs will be of the form ``http://<BUCKETNAME>/foo`` vs.
	``http://<BUCKETNAME>.s3.amazonaws.com/foo``.

Next, make sure to import ``django-scrup``'s urls. A line like the following in your
``urls.py`` should do the trick::

    (r'^scrup/', include('scrup.urls')),

Finally, plug the URL into Scrup's configuration. Obviously, this depends on your
server's domain and how you've chosen to setup ``django-scrup``'s urls. By default,
``django-scrup`` accepts uploads at ``upload/<FILENAME>``, where ``<FILENAME>`` is
optional. Here's an example of the default URL scheme for ``mydomain.com``::

	http://mydomain.com/scrup/upload/{filename}

License
=======

django-scrup is made available under the terms of the `new BSD license`_. For the full
legal text, please consult the ``LICENSE.txt`` file included in the root of the source
tree.

.. _`new BSD license`: http://www.opensource.org/licenses/bsd-license.php