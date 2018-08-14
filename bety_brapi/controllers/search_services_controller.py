import connexion
import six
#from bety_brapi.controllers_impl import SearchServicesController_impl

from bety_brapi.models.germplasm_response import GermplasmResponse  # noqa: E501
from bety_brapi.models.germplasm_search_request import GermplasmSearchRequest  # noqa: E501
from bety_brapi.models.observation_units_response import ObservationUnitsResponse  # noqa: E501
from bety_brapi.models.observation_units_table_response1 import ObservationUnitsTableResponse1  # noqa: E501
from bety_brapi.models.phenotypes_search_request import PhenotypesSearchRequest  # noqa: E501
from bety_brapi.models.programs_response import ProgramsResponse  # noqa: E501
from bety_brapi.models.programs_search_request import ProgramsSearchRequest  # noqa: E501
from bety_brapi.models.sample_search_request import SampleSearchRequest  # noqa: E501
from bety_brapi.models.samples_response import SamplesResponse  # noqa: E501
from bety_brapi.models.studies_response import StudiesResponse  # noqa: E501
from bety_brapi.models.study_search_request import StudySearchRequest  # noqa: E501
from bety_brapi.models.vendor_plate_search_request import VendorPlateSearchRequest  # noqa: E501
from bety_brapi.models.vendor_plates_response import VendorPlatesResponse  # noqa: E501
from bety_brapi.models.vendor_plates_response1 import VendorPlatesResponse1  # noqa: E501
from bety_brapi import util


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

#    return SearchServicesController_impl.germplasm_search_get(germplasmPUI=None, germplasmDbId=None, germplasmName=None, commonCropName=None, pageSize=None, page=None)
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

#    return SearchServicesController_impl.germplasm_search_post(body=None)
    return "Not implemented"


def phenotypes_search_csv_post(body=None):  # noqa: E501
    """Phenotype Search CSV

    Scope: PHENOTYPING. Status: ACCEPTED.  Returns a list of observationUnit with the observed Phenotypes.        observationTimeStamp : Iso Standard 8601.  observationValue data type inferred from the ontology # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = PhenotypesSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return SearchServicesController_impl.phenotypes_search_csv_post(body=None)
    return "Not implemented"


def phenotypes_search_get(germplasmDbId=None, observationVariableDbId=None, studyDbId=None, locationDbId=None, trialDbId=None, programDbId=None, seasonDbId=None, observationLevel=None, observationTimeStampRangeStart=None, observationTimeStampRangeEnd=None, pageSize=None, page=None):  # noqa: E501
    """Phenotype Search

    Scope: PHENOTYPING. Status: ACCEPTED.  Returns a list of observationUnit with the observed Phenotypes.  See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details.  Implemented for GnpIS and PHIS data (https://urgi.versailles.inra.fr/ws/webresources/brapi/v1/phenotypes).  Use case: this section allows to get a dataset from multiple studies. It allows to integrate data from several databases. Refactor note : This call allows to get and integrate portions of multiple phenotyping data matrixes. A proposed evolution allowed to get a list of single observations, this functionality is still possible with this call by specifybing the observation variable, see below. Example Use cases: - Study a panel of germplasm accross multiple studies, search parameters : {\&quot;germplasmDbIds\&quot; : [ \&quot;Syrah\&quot;, \&quot;34Mtp362\&quot; ]} - Get all data for a specific study : {\&quot;studyDbIds\&quot; : [ \&quot;383\&quot; ]} - Get simple atomic phenotyping values : {\&quot;germplasmDbIds\&quot; : [ \&quot;Syrah\&quot;, \&quot;34Mtp362\&quot; ], \&quot;observationVariableDbIds\&quot; : [ \&quot;CO_345:0000043\&quot;]} - Study Locations for adaptation to climat change : {\&quot;locationDbIds\&quot; : [ \&quot;383838\&quot;, \&quot;MONTPELLIER\&quot; ], \&quot;germplasmDbIds\&quot; : [ \&quot;all ids for a given species\&quot;]} - Find phenotypes that are from after a certain timestamp  observationTimeStamp : Iso Standard 8601.  observationValue data type inferred from the ontology # noqa: E501

    :param germplasmDbId: The name or synonym of external genebank accession identifiers
    :type germplasmDbId: str
    :param observationVariableDbId: The ID of traits, could be ontology ID, database ID or PUI
    :type observationVariableDbId: str
    :param studyDbId: The database ID / PK of the studies search parameter
    :type studyDbId: str
    :param locationDbId: locations these traits were collected
    :type locationDbId: str
    :param trialDbId: trial to search across
    :type trialDbId: str
    :param programDbId: program that have phenotyped this trait
    :type programDbId: str
    :param seasonDbId: The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    :type seasonDbId: str
    :param observationLevel: The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    :type observationLevel: str
    :param observationTimeStampRangeStart: Timestamp range start
    :type observationTimeStampRangeStart: str
    :param observationTimeStampRangeEnd: Timestamp range end
    :type observationTimeStampRangeEnd: str
    :param pageSize: The size of the pages to be returned. Default is 1000.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is 0.
    :type page: int

    :rtype: ObservationUnitsResponse
    """
    observationTimeStampRangeStart = util.deserialize_datetime(observationTimeStampRangeStart)
    observationTimeStampRangeEnd = util.deserialize_datetime(observationTimeStampRangeEnd)

#    return SearchServicesController_impl.phenotypes_search_get(germplasmDbId=None, observationVariableDbId=None, studyDbId=None, locationDbId=None, trialDbId=None, programDbId=None, seasonDbId=None, observationLevel=None, observationTimeStampRangeStart=None, observationTimeStampRangeEnd=None, pageSize=None, page=None)
    return "Not implemented"


def phenotypes_search_post(body=None):  # noqa: E501
    """Phenotype Search

    Scope: PHENOTYPING. Status: ACCEPTED.  Returns a list of observationUnit with the observed Phenotypes.  See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details.  Implemented for GnpIS and PHIS data (https://urgi.versailles.inra.fr/ws/webresources/brapi/v1/phenotypes).  Use case: this section allows to get a dataset from multiple studies. It allows to integrate data from several databases. Refactor note : This call allows to get and integrate portions of multiple phenotyping data matrixes. A proposed evolution allowed to get a list of single observations, this functionality is still possible with this call by specifybing the observation variable, see below. Example Use cases: - Study a panel of germplasm accross multiple studies, search parameters : {\&quot;germplasmDbIds\&quot; : [ \&quot;Syrah\&quot;, \&quot;34Mtp362\&quot; ]} - Get all data for a specific study : {\&quot;studyDbIds\&quot; : [ \&quot;383\&quot; ]} - Get simple atomic phenotyping values : {\&quot;germplasmDbIds\&quot; : [ \&quot;Syrah\&quot;, \&quot;34Mtp362\&quot; ], \&quot;observationVariableDbIds\&quot; : [ \&quot;CO_345:0000043\&quot;]} - Study Locations for adaptation to climat change : {\&quot;locationDbIds\&quot; : [ \&quot;383838\&quot;, \&quot;MONTPELLIER\&quot; ], \&quot;germplasmDbIds\&quot; : [ \&quot;all ids for a given species\&quot;]} - Find phenotypes that are from after a certain timestamp  observationTimeStamp : Iso Standard 8601.  observationValue data type inferred from the ontology # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ObservationUnitsResponse
    """
    if connexion.request.is_json:
        body = PhenotypesSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return SearchServicesController_impl.phenotypes_search_post(body=None)
    return "Not implemented"


def phenotypes_search_table_post(body=None):  # noqa: E501
    """Phenotype Search Table

    Scope: PHENOTYPING. Status: ACCEPTED.  Returns a list of observationUnit with the observed Phenotypes.        observationTimeStamp : Iso Standard 8601.  observationValue data type inferred from the ontology # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ObservationUnitsTableResponse1
    """
    if connexion.request.is_json:
        body = PhenotypesSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return SearchServicesController_impl.phenotypes_search_table_post(body=None)
    return "Not implemented"


def phenotypes_search_tsv_post(body=None):  # noqa: E501
    """Phenotype Search TSV

    Scope: PHENOTYPING. Status: ACCEPTED.  Returns a list of observationUnit with the observed Phenotypes.        observationTimeStamp : Iso Standard 8601.  observationValue data type inferred from the ontology # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = PhenotypesSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return SearchServicesController_impl.phenotypes_search_tsv_post(body=None)
    return "Not implemented"


def programs_search_post(body=None):  # noqa: E501
    """Search Programs

     Advanced searching for the programs resource. Status: ACCEPTED. See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ProgramsResponse
    """
    if connexion.request.is_json:
        body = ProgramsSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return SearchServicesController_impl.programs_search_post(body=None)
    return "Not implemented"


def samples_search_get(sampleDbId=None, observationUnitDbId=None, plateDbId=None, germplasmDbId=None, pageSize=None, page=None):  # noqa: E501
    """Get Sample Search

     Used to retrieve list of Samples from a Sample Tracking system based on some search criteria. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/samples\&quot;&gt; test-server.brapi.org/brapi/v1/samples-search&lt;/a&gt; # noqa: E501

    :param sampleDbId: the internal DB id for a sample
    :type sampleDbId: str
    :param observationUnitDbId: the internal DB id for an observation unit where a sample was taken from
    :type observationUnitDbId: str
    :param plateDbId: the internal DB id for a plate of samples
    :type plateDbId: str
    :param germplasmDbId: the internal DB id for a germplasm
    :type germplasmDbId: str
    :param pageSize: The size of the pages to be returned. Default is 1000.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is 0.
    :type page: int

    :rtype: SamplesResponse
    """

#    return SearchServicesController_impl.samples_search_get(sampleDbId=None, observationUnitDbId=None, plateDbId=None, germplasmDbId=None, pageSize=None, page=None)
    return "Not implemented"


def samples_search_post(sampleSearch=None):  # noqa: E501
    """Post Sample Search

     Used to retrieve list of Samples from a Sample Tracking system based on some search criteria. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/samples\&quot;&gt; test-server.brapi.org/brapi/v1/samples-search&lt;/a&gt; # noqa: E501

    :param sampleSearch: 
    :type sampleSearch: dict | bytes

    :rtype: SamplesResponse
    """
    if connexion.request.is_json:
        sampleSearch = SampleSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return SearchServicesController_impl.samples_search_post(sampleSearch=None)
    return "Not implemented"


def studies_search_get(studyType=None, programDbId=None, locationDbId=None, seasonDbId=None, trialDbId=None, studyDbId=None, germplasmDbIds=None, observationVariableDbIds=None, pageSize=None, page=None, active=None, sortBy=None, sortOrder=None):  # noqa: E501
    """Search Studies (GET)

     Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016. Implemented by: Germinate Used by: Flapjack, Cassavabase See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details. Get list of studies StartDate and endDate should be ISO8601 format for dates: YYYY-MM-DD &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies-search&lt;/a&gt; # noqa: E501

    :param studyType: Filter based on study type e.g. Nursery, Trial or Genotype.
    :type studyType: str
    :param programDbId: Program filter to only return studies associated with given program id.
    :type programDbId: str
    :param locationDbId: Filter by location
    :type locationDbId: str
    :param seasonDbId: Filter by season or year
    :type seasonDbId: str
    :param trialDbId: Filter by trial
    :type trialDbId: str
    :param studyDbId: Filter by study DbId
    :type studyDbId: str
    :param germplasmDbIds: Filter studies where specified germplasm have been used/tested
    :type germplasmDbIds: List[str]
    :param observationVariableDbIds: Filter studies where specified observation variables have been measured
    :type observationVariableDbIds: List[str]
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int
    :param active: Filter active status true/false.
    :type active: bool
    :param sortBy: Sort order. Name of the field to sort by.
    :type sortBy: str
    :param sortOrder: Sort order direction. Ascending/Descending.
    :type sortOrder: str

    :rtype: StudiesResponse
    """

#    return SearchServicesController_impl.studies_search_get(studyType=None, programDbId=None, locationDbId=None, seasonDbId=None, trialDbId=None, studyDbId=None, germplasmDbIds=None, observationVariableDbIds=None, pageSize=None, page=None, active=None, sortBy=None, sortOrder=None)
    return "Not implemented"


def studies_search_post(studySearchRequest=None):  # noqa: E501
    """Search Studies (GET)

     Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016. Implemented by: Germinate Used by: Flapjack, Cassavabase See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details. Get list of studies StartDate and endDate should be ISO8601 format for dates: YYYY-MM-DD &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies-search&lt;/a&gt; # noqa: E501

    :param studySearchRequest: Study Search request
    :type studySearchRequest: dict | bytes

    :rtype: StudiesResponse
    """
    if connexion.request.is_json:
        studySearchRequest = StudySearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return SearchServicesController_impl.studies_search_post(studySearchRequest=None)
    return "Not implemented"


def vendor_plates_search_get(vendorProjectDbId=None, vendorPlateDbId=None, clientPlateDbId=None, sampleInfo=None, pageSize=None, page=None):  # noqa: E501
    """Search for plates

    Search for plates in the database.  &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/vendor/plates-search\&quot;&gt; test-server.brapi.org/brapi/v1/vendor/plates-search&lt;/a&gt; # noqa: E501

    :param vendorProjectDbId: 
    :type vendorProjectDbId: str
    :param vendorPlateDbId: 
    :type vendorPlateDbId: str
    :param clientPlateDbId: 
    :type clientPlateDbId: str
    :param sampleInfo: 
    :type sampleInfo: bool
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: VendorPlatesResponse1
    """

#    return SearchServicesController_impl.vendor_plates_search_get(vendorProjectDbId=None, vendorPlateDbId=None, clientPlateDbId=None, sampleInfo=None, pageSize=None, page=None)
    return "Not implemented"


def vendor_plates_search_post(body=None):  # noqa: E501
    """Search for plates

    Search for plates in the database.  &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/vendor\&quot;&gt; test-server.brapi.org/brapi/v1/vendor/plate-search&lt;/a&gt; # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: VendorPlatesResponse
    """
    if connexion.request.is_json:
        body = VendorPlateSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return SearchServicesController_impl.vendor_plates_search_post(body=None)
    return "Not implemented"

