
from setuptools import setup, find_packages

setup(
    name ='FbSecure',
    version ='1.0',
    description = 'Change your facebook password from the cli',
    author = 'Dibya Ranjan Jena',
    author_email = 'dibyajena917@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    install_requires=[
        'bs4',
        'selenium',
        'click',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        fbs=fbsecure:cli
    ''',
)