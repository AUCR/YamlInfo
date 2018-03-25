"""YamlInfo Install Script"""
# coding=utf-8
from yaml_info.yamlinfo import YamlInfo
from setuptools import setup, find_packages

project_data = YamlInfo("projectinfo.yml", "projectinfo", "LICENSE").get()
project_info_data = project_data["info"]
project_version_data = project_data["version"]
__version__ = "%(major)s.%(minor)s.%(revision)s" % project_version_data

setup(
    name=project_data["info"]["name"],
    version=__version__,
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['PyYAML'],
    url='https://github.com/AUCR/YamlInfo',
    license='GPL-3.0',
    author=project_data["info"]["authors"],
    author_email=project_data["info"]["authors_email"],
    description=project_data["info"]["description"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6',
    ],
)
