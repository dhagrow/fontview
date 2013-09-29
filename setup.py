from setuptools import setup

setup(name='fontview', version='0.1.4',
    description='A font and styling previewer for programmers.',
    author='Miguel Turner', author_email='cymrow at gmail.com',
    url='http://fonts.dhagrow.org/',
    
    install_requires=[
        'bottle==0.11.6',
        'waitress==0.8.7',
        'pygments==1.6',
        'hiredis==0.1.1',
        'msgpack-python==0.3.0',
        'redis==2.8.0',
        ],
    )
