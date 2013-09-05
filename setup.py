from setuptools import setup

setup(name='fontview', version='0.1',
    description='Font Previewer',
    author='Miguel Turner', author_email='cymrow at gmail.com',
    url='http://fontview-dhagrow.rhcloud.com',
    
    install_requires=[
        'bottle==11.6',
        'waitress==0.8.7',
        'pygments==1.6',
        ],
    )
