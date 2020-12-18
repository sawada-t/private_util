from setuptools import setup

install_requires = [
     mysqlclient,
     requests
]

packages = [
    'private_utils',
]

console_scripts = [
]


setup(
    name='privutils',
    version='0.0.4',
    packages=packages,
    install_requires=install_requires,
)
