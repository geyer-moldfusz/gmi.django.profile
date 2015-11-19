.. _setup

Setup
=====

Installed apps
--------------

To use gmi.django.profile you have to add some applications to
your Django settings.

.. code-block:: none

    INSTALLED_APPS = (
        [...]
        'django_markdown',
        'gmi.django.avatar',
        'gmi.django.profile.ProfileApp',
    )


URL Patterns
------------

Add the gmi.django.profile and django_markdown urls to your
urlpatterns.


.. code-block:: none

    urlpatterns = [
        [...]
        url(r'^profile/', include('gmi.django.profile.urls', namespace='profile')),
        url(r'^markdown/', include('django_markdown.urls')),
    ]


Templates
---------

There are several templates that can be overrided.

XXX


Avatar images
-------------

To fetch Avatars for your users from Gravatar you have to run the
``collectstatic`` command for your manage.py as described in the
gmi.django.avatar documentation. XXX

It is recommendet to run this command as a cron job to regularely
update the Avatar images and follow changes on the Gravatar
source.
