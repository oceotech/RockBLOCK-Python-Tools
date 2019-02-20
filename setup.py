
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rockblock-tools',
    version='0.0.3',

    description='RockBLOCK message sending and receiving tools',
    long_description=long_description,
    long_description_content_type = 'text/markdown',

    url='https://github.com/oceotech/RockBLOCK-Python-Tools',

    author='Andrew Carter',
    author_email='andrewcarter1992@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='rockblock 9603 iridium sbd tools',

    packages=['rockblock_tools', 'rockblock_tools.formatter'],

    include_package_data=True,

    install_requires=['requests', 'flask', 'paho-mqtt'],

    entry_points={
        'console_scripts': ['rockblock=rockblock_tools.command:main'],
    },
)
