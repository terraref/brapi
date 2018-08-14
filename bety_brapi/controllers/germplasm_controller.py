import connexion
import six
#from bety_brapi.controllers_impl import GermplasmController_impl

from bety_brapi.models.breeding_method_response import BreedingMethodResponse  # noqa: E501
from bety_brapi.models.breeding_methods_response import BreedingMethodsResponse  # noqa: E501
from bety_brapi.models.germplasm_attribute_list_response import GermplasmAttributeListResponse  # noqa: E501
from bety_brapi.models.germplasm_markerprofiles_list_response import GermplasmMarkerprofilesListResponse  # noqa: E501
from bety_brapi.models.germplasm_response import GermplasmResponse  # noqa: E501
from bety_brapi.models.germplasm_response1 import GermplasmResponse1  # noqa: E501
from bety_brapi.models.germplasm_search_request import GermplasmSearchRequest  # noqa: E501
from bety_brapi.models.germplasm_summary_list_response import GermplasmSummaryListResponse  # noqa: E501
from bety_brapi.models.pedigree_response import PedigreeResponse  # noqa: E501
from bety_brapi.models.progeny_response import ProgenyResponse  # noqa: E501
from bety_brapi import util


def breedingmethods_breeding_method_db_id_get(breedingMethodDbId):  # noqa: E501
    """GET specific breeding method details

      &lt;a&gt;example.com/brapi/v1/breedingmethods/{breedingMethodDbId}&lt;/a&gt; # noqa: E501

    :param breedingMethodDbId: Internal database identifier for a breeding method
    :type breedingMethodDbId: str

    :rtype: BreedingMethodResponse
    """

#    return GermplasmController_impl.breedingmethods_breeding_method_db_id_get(breedingMethodDbId)
    return "Not implemented"


def breedingmethods_get(pageSize=None, page=None):  # noqa: E501
    """GET List of Breeding Methods

     Scope: Germplasm Get the list of germplasm breeding methods available in a system. &lt;a&gt;example.com/brapi/v1/breedingmethods&lt;/a&gt; # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: BreedingMethodsResponse
    """

#    return GermplasmController_impl.breedingmethods_get(pageSize=None, page=None)
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

#    return GermplasmController_impl.germplasm_germplasm_db_id_attributes_get(germplasmDbId, attributeDbIds=None, attributeList=None, pageSize=None, page=None)
    return "Not implemented"


def germplasm_germplasm_db_id_get(germplasmDbId):  # noqa: E501
    """Germplasm search by germplasmDbId

     Scope: CORE. Status: ACCEPTED. Implementation target date: PAG2016 Implemented by: Tripal Brapi module, Germinate, Cassavabase Note: Germplasm Details by germplasmDbId was merged with Germplasm Multi Crop Passport Data. The MCPD fields are optional and marked with the prefix [MCPD]. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/germplasm\&quot;&gt; test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}&lt;/a&gt;  # noqa: E501

    :param germplasmDbId: The internal id of the germplasm
    :type germplasmDbId: str

    :rtype: GermplasmResponse1
    """

#    return GermplasmController_impl.germplasm_germplasm_db_id_get(germplasmDbId)
    return "Not implemented"


def germplasm_germplasm_db_id_markerprofiles_get(germplasmDbId):  # noqa: E501
    """Markerprofiles by germplasmDbId

     Retrieve the markerProfileDbIds for a given Germplasm ID Scope: GENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016 Implemented by: Germinate, Cassavabase &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/germplasm\&quot;&gt; test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}/markerprofiles&lt;/a&gt;  # noqa: E501

    :param germplasmDbId: the internal id of the germplasm
    :type germplasmDbId: str

    :rtype: GermplasmMarkerprofilesListResponse
    """

#    return GermplasmController_impl.germplasm_germplasm_db_id_markerprofiles_get(germplasmDbId)
    return "Not implemented"


def germplasm_germplasm_db_id_pedigree_get(germplasmDbId, notation=None, includeSiblings=None):  # noqa: E501
    """Germplasm pedigree by id

     Scope: CORE. Status: ACCEPTED. Implementation target date: PAG2016 Implemented by: Germinate, Tripal Brapi Module, Cassavabase (without notation option) (http://wheat.pw.usda.gov/ggpages/gopher/administration/Template%20for%20Germplasm%20records.html) or [Lamacraft] (http://link.springer.com/article/10.1007%2FBF00021556). &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/germplasm\&quot;&gt; test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}/pedigree&lt;/a&gt;  # noqa: E501

    :param germplasmDbId: the internal id of the germplasm
    :type germplasmDbId: str
    :param notation: text representation of the pedigree
    :type notation: str
    :param includeSiblings: include array of siblings in response
    :type includeSiblings: bool

    :rtype: PedigreeResponse
    """

#    return GermplasmController_impl.germplasm_germplasm_db_id_pedigree_get(germplasmDbId, notation=None, includeSiblings=None)
    return "Not implemented"


def germplasm_germplasm_db_id_progeny_get(germplasmDbId):  # noqa: E501
    """Germplasm pedigree by id

     Scope: Germplasm Get the germplasmDbIds for all the Progeny of a particular germplasm. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/germplasm\&quot;&gt; test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}/progeny&lt;/a&gt;  # noqa: E501

    :param germplasmDbId: the internal id of the germplasm
    :type germplasmDbId: str

    :rtype: ProgenyResponse
    """

#    return GermplasmController_impl.germplasm_germplasm_db_id_progeny_get(germplasmDbId)
    return "Not implemented"


def germplasm_search_get(germplasmPUI=None, germplasmDbId=None, germplasmName=None, commonCropName=None, pageSize=None, page=None):  # noqa: E501
    """Germplasm search through GET

     Implemented by: GnpIS, Germinate (GET only) See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details. Notes: The germplasm and germplasm MCPD calls were merged.  The MCPD fields are optional and indicated as such with the [MCPD] prefix in the description field of the \&quot;Response data types\&quot; table. Please use the \&quot;features\&quot; hash of the \&quot;calls\&quot; call to communicate with clients as to whether MCPD is supported by your implementation. Addresses these needs: 1. General germplasm search mechanism that accepts POST for complex queries 2. possibility to search germplasm by more parameters than those allowed by the existing germplasm search 3. possibility to get MCPD details by PUID rather than dbId Use GET when parameter size is less than 2K bytes. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/germplasm\&quot;&gt; test-server.brapi.org/brapi/v1/germplasm-search&lt;/a&gt;  # noqa: E501

    :param germplasmPUI: Permanent unique identifier (DOI, URI, etc.)
    :type germplasmPUI: str
    :param germplasmDbId: Internal database identifier
    :type germplasmDbId: str
    :param germplasmName: Name of the germplasm
    :type germplasmName: str
    :param commonCropName: The common crop name related to this germplasm
    :type commonCropName: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: GermplasmResponse
    """

#    return GermplasmController_impl.germplasm_search_get(germplasmPUI=None, germplasmDbId=None, germplasmName=None, commonCropName=None, pageSize=None, page=None)
    return "Not implemented"


def germplasm_search_post(body=None):  # noqa: E501
    """Germplasm search through POST

     Implemented by: GnpIS, Germinate (GET only) See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details. Notes: The germplasm and germplasm MCPD calls were merged.  The MCPD fields are optional and indicated as such with the [MCPD] prefix in the description field of the \&quot;Response data types\&quot; table. Please use the \&quot;features\&quot; hash of the \&quot;calls\&quot; call to communicate with clients as to whether MCPD is supported by your implementation. Addresses these needs: 1. General germplasm search mechanism that accepts POST for complex queries 2. possibility to search germplasm by more parameters than those allowed by the existing germplasm search 3. possibility to get MCPD details by PUID rather than dbId Use POST for large queries (&gt;2K bytes).  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: GermplasmResponse
    """
    if connexion.request.is_json:
        body = GermplasmSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return GermplasmController_impl.germplasm_search_post(body=None)
    return "Not implemented"


def studies_study_db_id_germplasm_get(studyDbId, pageSize=None, page=None):  # noqa: E501
    """Study Germplasm Details

     Scope: PHENOTYPING &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/germplasm&lt;/a&gt; # noqa: E501

    :param studyDbId: Identifier of the study. Usually a number, could be alphanumeric.
    :type studyDbId: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: GermplasmSummaryListResponse
    """

#    return GermplasmController_impl.studies_study_db_id_germplasm_get(studyDbId, pageSize=None, page=None)
    return "Not implemented"

