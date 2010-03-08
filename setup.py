from setuptools import setup, find_packages
 
f = open('README.rst')
readme = f.read()
f.close()
 
setup(
    name = 'django-scrup',
    version = '0.1',
    description = 'A django-based web receiver for Scrup which stores screencaptures on S3.',
    packages = find_packages(),
    long_description = readme,
    author = 'Idan Gazit',
    author_email = 'idan@pixane.com',
    url = 'http://github.com/idangazit/django-scrup',
    install_requires = ('boto>=1.9b',),
    classifiers = (
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ),
)
