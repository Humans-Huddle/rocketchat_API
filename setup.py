# -*-coding:utf-8-*-

from setuptools import setup

setup(
    name='rocketchat_API',
    version='0.6.11',
    packages=['rocketchat_API', 'rocketchat_API.APIExceptions'],
    url='https://github.com/jadolg/rocketchat_API',
    license='MIT',
    author='Jorge Alberto Díaz Orozco',
    author_email='diazorozcoj@gmail.com',
    description='Python API wrapper for Rocket.Chat',
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=(
        'requests',
    )
)
