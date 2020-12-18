from setuptools import setup

install_requires = [
     'mysqlclient',
     'requests'
]

packages = [
    'privutils',
    'privutils.api_util',
    'privutils.batch_util',
    'privutils.mysql_util',
    'privutils.self_scheduling_job'
]

console_scripts = [
]


setup(
    name='privutils',
    version='0.0.8',
    packages=packages,
    install_requires=install_requires,
)
