# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "bety_brapi"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="BrAPI",
    author_email="",
    url="",
    keywords=["Swagger", "BrAPI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['bety_brapi=bety_brapi.__main__:main']},
    long_description="""\
    The Breeding API (BrAPI) is a Standardized RESTful Web Service API Specification for communicating Plant Breeding Data. BrAPI allows for easy data sharing between databases and tools involved in plant breeding.  &lt;strong&gt;General Reference Documentation&lt;/strong&gt; &lt;a href&#x3D;\&quot;https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/URL_Structure.md\&quot;&gt;URL Structure&lt;/a&gt; &lt;a href&#x3D;\&quot;https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Response_Structure.md\&quot;&gt;Response Structure&lt;/a&gt; &lt;a href&#x3D;\&quot;https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Date_Time_Encoding.md\&quot;&gt;Date/Time Encoding&lt;/a&gt; &lt;a href&#x3D;\&quot;https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Location_Encoding.md\&quot;&gt;Location Encoding&lt;/a&gt; &lt;a href&#x3D;\&quot;https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Error_Handling.md\&quot;&gt;Error Handling&lt;/a&gt; &lt;a href&#x3D;\&quot;https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Search_Services.md\&quot;&gt;Search Services&lt;/a&gt; &lt;a href&#x3D;\&quot;https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Asychronous_Processing.md\&quot;&gt;Asynchronous Processing&lt;/a&gt;
    """
)

