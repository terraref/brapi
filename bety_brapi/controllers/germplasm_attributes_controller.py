import connexion
import six
#from bety_brapi.controllers_impl import GermplasmAttributesController_impl

from bety_brapi.models.germplasm_attribute_categories_response import GermplasmAttributeCategoriesResponse  # noqa: E501
from bety_brapi.models.germplasm_attribute_defs_response import GermplasmAttributeDefsResponse  # noqa: E501
from bety_brapi.models.germplasm_attribute_list_response import GermplasmAttributeListResponse  # noqa: E501
from bety_brapi import util


def attributes_categories_get(pageSize=None, page=None):  # noqa: E501
    """Germplasm attribute categories

     Scope: OTHER. Status: ACCEPTED. Implementation target date: PAG2016 List all available attribute categories. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/attributes\&quot;&gt; test-server.brapi.org/brapi/v1/attributes/categories&lt;/a&gt; # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: GermplasmAttributeCategoriesResponse
    """

#    return GermplasmAttributesController_impl.attributes_categories_get(pageSize=None, page=None)
    return "Not implemented"


def attributes_get(attributeCategoryDbId=None, pageSize=None, page=None):  # noqa: E501
    """Attributes by attributeCategoryDbId

     List available attributes. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/attributes\&quot;&gt; test-server.brapi.org/brapi/v1/attributes&lt;/a&gt;  # noqa: E501

    :param attributeCategoryDbId: filter for kind of attributes
    :type attributeCategoryDbId: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: GermplasmAttributeDefsResponse
    """

#    return GermplasmAttributesController_impl.attributes_get(attributeCategoryDbId=None, pageSize=None, page=None)
    return "Not implemented"


def germplasm_germplasm_db_id_attributes_get(germplasmDbId, attributeDbIds=None, attributeList=None, pageSize=None, page=None):  # noqa: E501
    """Germplasm attribute values

    Values for all attributes by default.  &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/germplasm\&quot;&gt; test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}/attributes&lt;/a&gt; # noqa: E501

    :param germplasmDbId: The germplasm characterized
    :type germplasmDbId: str
    :param attributeDbIds: Restrict the response to only the listed attributeDbIds.
    :type attributeDbIds: List[str]
    :param attributeList: **Deprecated** Use \&quot;attributeDbIds\&quot; instead
    :type attributeList: List[str]
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: GermplasmAttributeListResponse
    """

#    return GermplasmAttributesController_impl.germplasm_germplasm_db_id_attributes_get(germplasmDbId, attributeDbIds=None, attributeList=None, pageSize=None, page=None)
    return "Not implemented"

