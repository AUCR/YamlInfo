"""YamlInfo Install Script"""
# coding=utf-8
from setuptools import setup, find_packages
from yaml_info.yamlinfo import YamlInfo


project_data = YamlInfo("projectinfo.yml", "projectinfo", "LICENSE").get()
project_info_data = project_data["info"]
project_version_data = project_data["version"]
__version__ = "%(major)s.%(minor)s.%(revision)s.%(release)s" % project_version_data

setup(
    name=project_data["info"]["name"],
    version=__version__,
    include_package_data=True,
    install_requires=["PyYAML"],
    packages=find_packages(exclude=["docs", "tests*"]),
    url=project_data["info"]["url"],
    license=project_data["info"]["license"],
    author=project_data["info"]["authors"],
    author_email=project_data["info"]["authors_email"],
    description=project_data["info"]["description"],
    classifiers=project_data["info"]["classifiers"],
)
