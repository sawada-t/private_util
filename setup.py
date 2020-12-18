from setuptools import setup

install_requires = [
     'mysqlclient',
     'requests'
]

packages = [
    'privutils',
]

console_scripts = [
]


setup(
    name='privutils',
    version='0.0.6',
    packages=packages,
    install_requires=install_requires,
)
