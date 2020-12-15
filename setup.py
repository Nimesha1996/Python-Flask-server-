# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0",
    "typing>=3.5.2.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Swagger Petstore - OpenAPI 3.0",
    author_email="apiteam@swagger.io",
    url="",
    keywords=["OpenAPI", "Swagger Petstore - OpenAPI 3.0"],
    install_requires=REQUIRES,
    packages=find_packages(""),
    package_dir={"": ""},
    package_data={'': ['/openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about Swagger at [http://swagger.io](http://swagger.io). In the third iteration of the pet store, we&#39;ve switched to the design first approach! You can now help us improve the API whether it&#39;s by making changes to the definition itself or to the code. That way, with time, we can improve the API in general, and expose some of the new features in OAS3. Some useful links: - [The Pet Store repository](https://github.com/swagger-api/swagger-petstore) - [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)
    """
)

