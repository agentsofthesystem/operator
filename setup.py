import pathlib
import pkg_resources
import sysconfig

from setuptools import setup, find_packages

PACKAGE_NAME = 'operator'
PACKAGE_DIRECTORY = 'operator_client'
SITE_PACKAGES_DIR = sysconfig.get_paths()["purelib"]

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name=PACKAGE_NAME,
    version='0.1.0',
    description='Python Client to AgentSmith',
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True
)