import os
from setuptools import find_packages, setup
from djangocms_ga_optout import __version__

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


REQUIREMENTS = [
    'django>=1.8,<2.0',
    'django-cms>=3.2',
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Framework :: Django',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='djangocms-ga-optout',
    version=__version__,
    packages=['djangocms_ga_optout'],
    description='A djangoCMS Plugin that creates an Opt-Out link for Google Analytics.',
    long_description=read('README.rst'),
    license=read('LICENSE.txt'),
    author='Maximilian Muth',
    author_email='max@blueshoe.de',
    url='https://github.com/Blueshoe/djangocms-ga-optout',
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    keywords=['django', 'Django CMS', 'ga', 'google analytics', 'GDPR', 'CMS', 'Blueshoe'],
    include_package_data=True,
    zip_safe=False,
)
