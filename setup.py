from setuptools import setup, find_packages
import sys, os

version = '0.1'

requires = [
   'Django',
   'django-contact-form',
   'django-markdown',
   'setuptools',
   'gmi.django.avatar',
]

setup(name='gmi.django.profile',
      version=version,
      description="Manage crew profiles.",
      long_description="""\
XXX long description""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django profile',
      author='Stefan Walluhn',
      author_email='stefan@neuland.io',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['gmi', 'gmi.django'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
