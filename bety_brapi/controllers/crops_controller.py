import connexion
import six
from bety_brapi.controllers_impl import CropsController_impl

from bety_brapi.models.common_crop_names_response import CommonCropNamesResponse  # noqa: E501
from bety_brapi import util


def common_crop_names_get(pageSize=None, page=None):  # noqa: E501
    """List supported crops

    List the common crop names for the crops available in a database server.   This call is **required** for multi-crop systems where data from multiple crops may be stored in the same database server. A distinct database server is defined by everything in the URL before \&quot;/brapi/v1\&quot;, including host name and base path.    This call is recommended for single crop systems to be compatible with multi-crop clients. For a single crop system the response should contain an array with exactly 1 element.   The common crop name can be used as a search parameter for Programs, Studies, and Germplasm.  &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/commonCropNames\&quot;&gt; test-server.brapi.org/brapi/v1/commonCropNames&lt;/a&gt; # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: CommonCropNamesResponse
    """

    return CropsController_impl.common_crop_names_get(pageSize=None, page=None)


def crops_get(pageSize=None, page=None):  # noqa: E501
    """List supported crops

    For multi crop systems this is a useful call to list all the supported crops.  &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/crops\&quot;&gt; test-server.brapi.org/brapi/v1/crops&lt;/a&gt; # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: CommonCropNamesResponse
    """

    return CropsController_impl.crops_get(pageSize=None, page=None)

