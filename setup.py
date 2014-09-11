from setuptools import setup, find_packages

from nested_inline import __version__

github_url = 'https://github.com/s-block/django-nested-inline'
long_desc = open('README').read()

setup(
    name='django-nested-inline',
    version='.'.join(str(v) for v in __version__),
    description='Recursive nesting of inline forms for Django Admin',
    long_description=long_desc,
    url=github_url,
    author='Josh Rowe',
    author_email='josh@s-block.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
