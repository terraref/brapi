import connexion
import six
#from bety_brapi.controllers_impl import StudiesController_impl

from bety_brapi.models.germplasm_summary_list_response import GermplasmSummaryListResponse  # noqa: E501
from bety_brapi.models.new_observation_db_ids_response import NewObservationDbIdsResponse  # noqa: E501
from bety_brapi.models.new_observation_unit_db_ids_response import NewObservationUnitDbIdsResponse  # noqa: E501
from bety_brapi.models.new_observation_unit_request import NewObservationUnitRequest  # noqa: E501
from bety_brapi.models.new_observations_request import NewObservationsRequest  # noqa: E501
from bety_brapi.models.new_observations_request_wrapper_deprecated import NewObservationsRequestWrapperDeprecated  # noqa: E501
from bety_brapi.models.new_observations_table_request import NewObservationsTableRequest  # noqa: E501
from bety_brapi.models.observation_unit_positions_response import ObservationUnitPositionsResponse  # noqa: E501
from bety_brapi.models.observation_units_response1 import ObservationUnitsResponse1  # noqa: E501
from bety_brapi.models.observations_response import ObservationsResponse  # noqa: E501
from bety_brapi.models.seasons_response import SeasonsResponse  # noqa: E501
from bety_brapi.models.studies_response import StudiesResponse  # noqa: E501
from bety_brapi.models.study_layout_request import StudyLayoutRequest  # noqa: E501
from bety_brapi.models.study_observation_variables_response import StudyObservationVariablesResponse  # noqa: E501
from bety_brapi.models.study_response import StudyResponse  # noqa: E501
from bety_brapi.models.study_search_request import StudySearchRequest  # noqa: E501
from bety_brapi.models.study_types_response import StudyTypesResponse  # noqa: E501
from bety_brapi.models.studyobservations_table_response import StudyobservationsTableResponse  # noqa: E501
from bety_brapi import util


def seasons_get(year=None, pageSize=None, page=None):  # noqa: E501
    """List seasons or years

     Call to retrive all seasons (or years) in the database. (Added by Jan-Erik and Lukas 5/26/2016) Scope: PHENOTYPING. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/seasons\&quot;&gt; test-server.brapi.org/brapi/v1/seasons&lt;/a&gt; # noqa: E501

    :param year: 
    :type year: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: SeasonsResponse
    """

#    return StudiesController_impl.seasons_get(year=None, pageSize=None, page=None)
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

#    return StudiesController_impl.studies_search_get(studyType=None, programDbId=None, locationDbId=None, seasonDbId=None, trialDbId=None, studyDbId=None, germplasmDbIds=None, observationVariableDbIds=None, pageSize=None, page=None, active=None, sortBy=None, sortOrder=None)
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

#    return StudiesController_impl.studies_search_post(studySearchRequest=None)
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

#    return StudiesController_impl.studies_study_db_id_germplasm_get(studyDbId, pageSize=None, page=None)
    return "Not implemented"


def studies_study_db_id_get(studyDbId):  # noqa: E501
    """Retrieve study details

     Scope: PHENOTYPING. Status: ACCEPTED. Implemented by: Germinate, GnpIS Notes: an additionalInfo field was added to provide a controlled vocabulary for less common data fields. Retrieve the information of the study required for field data collection More linked data: * observation variables: &#x60;&#x60;&#x60;/brapi/v1/studies/{studyDbId}/observationVariables&#x60;&#x60;&#x60; * germplasm: &#x60;&#x60;&#x60;/brapi/v1/studies/{studyDbId}/germplasm&#x60;&#x60;&#x60; * observation units: &#x60;&#x60;&#x60;/brapi/v1/studies/{studyDbId}/observationUnits&#x60;&#x60;&#x60; * layout: &#x60;&#x60;&#x60;brapi/v1/studies/{studyDbId}/layout&#x60;&#x60;&#x60; &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}&lt;/a&gt; # noqa: E501

    :param studyDbId: Identifier of the study. Usually a number, could be alphanumeric.
    :type studyDbId: str

    :rtype: StudyResponse
    """

#    return StudiesController_impl.studies_study_db_id_get(studyDbId)
    return "Not implemented"


def studies_study_db_id_layout_get(studyDbId, pageSize=None, page=None):  # noqa: E501
    """Retrieve plot layout details

     Retrive the layout details for a study. Returns an array of observation unit position data which describes where each unit and germplasm is located within the study layout Retrieve the plot layout of the study with id {id}. For each observationUnit within a study, return the &#x60;block&#x60;, &#x60;replicate&#x60;, and &#x60;entryType&#x60; values as well as the &#x60;X&#x60; and &#x60;Y&#x60; coordinates. &#x60;entryType&#x60; can be \&quot;check\&quot;, \&quot;test\&quot;, or \&quot;filler\&quot;. Also return some human readable meta data about the observationUnit and germplasm. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/layout&lt;/a&gt;  # noqa: E501

    :param studyDbId: Identifier of the study. Usually a number, could be alphanumeric.
    :type studyDbId: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: ObservationUnitPositionsResponse
    """

#    return StudiesController_impl.studies_study_db_id_layout_get(studyDbId, pageSize=None, page=None)
    return "Not implemented"


def studies_study_db_id_layout_put(studyDbId, studyLayoutRequest=None):  # noqa: E501
    """Retrieve plot layout details

     Modify a study layout Update the layout data for a set of observation units within a study. Each layout object is a subset of fields within an observationUnit, so it doesnt make sense to create a new layout object by itself. Implementation Notes: + If any of the fields in the request object is missing, that piece of data will not be updated. + If an observationUnitDbId can not be found within the given study, an error will be returned. + &#x60;entryType&#x60; can have the values \&quot;check\&quot;, \&quot;test\&quot;, or \&quot;filler\&quot;. + The response should match the structure of the response from &#x60;GET studies/{studyDbId}/layout&#x60;, but it should only contain the layout objects which have been updated by the PUT request. Also, pagination is not available in the response. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/layout&lt;/a&gt;  # noqa: E501

    :param studyDbId: Identifier of the study. Usually a number, could be alphanumeric.
    :type studyDbId: str
    :param studyLayoutRequest: The request body for updateing a study layout
    :type studyLayoutRequest: dict | bytes

    :rtype: ObservationUnitPositionsResponse
    """
    if connexion.request.is_json:
        studyLayoutRequest = StudyLayoutRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return StudiesController_impl.studies_study_db_id_layout_put(studyDbId, studyLayoutRequest=None)
    return "Not implemented"


def studies_study_db_id_observation_variables_get(studyDbId):  # noqa: E501
    """&lt;strong&gt;Deprecated&lt;/strong&gt; Retrieve study observation variables

      &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationVariables&lt;/a&gt; # noqa: E501

    :param studyDbId: string database unique identifier
    :type studyDbId: str

    :rtype: StudyObservationVariablesResponse
    """

#    return StudiesController_impl.studies_study_db_id_observation_variables_get(studyDbId)
    return "Not implemented"


def studies_study_db_id_observations_get(studyDbId, observationVariableDbIds=None, pageSize=None, page=None):  # noqa: E501
    """Get Observation Units by observation variable ids

     Retrieve all observations where there are measurements for the given observation variables. observationTimestamp should be ISO8601 format with timezone: YYYY-MM-DDThh:mm:ss+hhmm &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/observations&lt;/a&gt; # noqa: E501

    :param studyDbId: Identifier of the study. Usually a number, could be alphanumeric.
    :type studyDbId: str
    :param observationVariableDbIds: Numeric &#x60;id&#x60; of that variable (combination of trait, unit and method)
    :type observationVariableDbIds: List[str]
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: ObservationsResponse
    """

#    return StudiesController_impl.studies_study_db_id_observations_get(studyDbId, observationVariableDbIds=None, pageSize=None, page=None)
    return "Not implemented"


def studies_study_db_id_observations_put(studyDbId, newObservations=None):  # noqa: E501
    """Get Observation Units by observation variable ids

     Implementation Guidelines: + If an &#x60;observationDbId&#x60; is \&quot;null\&quot; or an empty string in the request, a NEW observation should be created for the given study and observationUnit + If an &#x60;observationDbId&#x60; is populated but not found in the database, a NEW observation should be created for the given study and observationUnit AND an NEW &#x60;observationDbId&#x60; should be assigned to it. A warning should be returned to the client. + If an &#x60;observationDbId&#x60; is populated and found in the database, but the existing entry is not associated with the given study or observationUnit, a NEW observation should be created for the given study and observationUnit AND an NEW &#x60;observationDbId&#x60; should be assigned to it. A warning should be returned to the client. + If an &#x60;observationDbId&#x60; is populated and found in the database and is associated with the given study and observationUnit, then it should be updated with the new data given. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/observations&lt;/a&gt; # noqa: E501

    :param studyDbId: Identifier of the study. Usually a number, could be alphanumeric.
    :type studyDbId: str
    :param newObservations: 
    :type newObservations: dict | bytes

    :rtype: NewObservationDbIdsResponse
    """
    if connexion.request.is_json:
        newObservations = NewObservationsRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return StudiesController_impl.studies_study_db_id_observations_put(studyDbId, newObservations=None)
    return "Not implemented"


def studies_study_db_id_observationunits_get(studyDbId, observationLevel=None, pageSize=None, page=None):  # noqa: E501
    """Get all observation units

     The main API call for field data collection, to retrieve all the observation units within a study. Scope: PHENOTYPING &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationunits&lt;/a&gt; # noqa: E501

    :param studyDbId: The study these observation units are related to.
    :type studyDbId: str
    :param observationLevel: The granularity level of observation units. Either &#x60;plotNumber&#x60; or &#x60;plantNumber&#x60; fields will be relavant depending on whether granularity is plot or plant respectively.
    :type observationLevel: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: ObservationUnitsResponse1
    """

#    return StudiesController_impl.studies_study_db_id_observationunits_get(studyDbId, observationLevel=None, pageSize=None, page=None)
    return "Not implemented"


def studies_study_db_id_observationunits_post(studyDbId, format, body=None):  # noqa: E501
    """&lt;strong&gt;Deprecated&lt;/strong&gt; Save Observation Unit Phenotypes

    This call has been deprecated in V1.1. Use instead: \&quot;PUT /studies/{studyDbId}/observationunits\&quot; and \&quot;PUT /studies/{studyDbId}/observationunits/zip\&quot; # noqa: E501

    :param studyDbId: The study these observation units are related to.
    :type studyDbId: str
    :param format: (default is JSON, but can be zip) In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
    :type format: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NewObservationsRequestWrapperDeprecated.from_dict(connexion.request.get_json())  # noqa: E501

#    return StudiesController_impl.studies_study_db_id_observationunits_post(studyDbId, format, body=None)
    return "Not implemented"


def studies_study_db_id_observationunits_put(studyDbId, newObservationUnitRequest=None):  # noqa: E501
    """Save Observation Unit Phenotypes

    Use this call for uploading new Observations as JSON to a system.  Note: If &#39;observationUnitDbId&#39; or &#39;observationDbId&#39; is populated, they should be considered updates to existing records. If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. If &#39;observationUnitDbId&#39; or &#39;observationDbId&#39; is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds. # noqa: E501

    :param studyDbId: The study these observation units are related to.
    :type studyDbId: str
    :param newObservationUnitRequest: 
    :type newObservationUnitRequest: list | bytes

    :rtype: NewObservationUnitDbIdsResponse
    """
    if connexion.request.is_json:
        newObservationUnitRequest = [NewObservationUnitRequest.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501

#    return StudiesController_impl.studies_study_db_id_observationunits_put(studyDbId, newObservationUnitRequest=None)
    return "Not implemented"


def studies_study_db_id_observationunits_zip_post(studyDbId, zipRequest=None):  # noqa: E501
    """Use this call for uploading new Observations as a Batched Zip File to a system.

    Note: If &#39;observationUnitDbId&#39; or &#39;observationDbId&#39; is populated, they should be considered updates to existing records. If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. If &#39;observationUnitDbId&#39; or &#39;observationDbId&#39; is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds. # noqa: E501

    :param studyDbId: The study these observation units are related to.
    :type studyDbId: str
    :param zipRequest: 
    :type zipRequest: str

    :rtype: NewObservationUnitDbIdsResponse
    """

#    return StudiesController_impl.studies_study_db_id_observationunits_zip_post(studyDbId, zipRequest=None)
    return "Not implemented"


def studies_study_db_id_observationvariables_get(studyDbId, pageSize=None, page=None):  # noqa: E501
    """Get Observation Variables By Study

     Scope: PHENOTYPING List all the observation variables measured in the study. Refer to the data type definition of variables in &#x60;/Specification/ObservationVariables/README.md&#x60;. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationvariables&lt;/a&gt; # noqa: E501

    :param studyDbId: string database unique identifier
    :type studyDbId: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: StudyObservationVariablesResponse
    """

#    return StudiesController_impl.studies_study_db_id_observationvariables_get(studyDbId, pageSize=None, page=None)
    return "Not implemented"


def studies_study_db_id_table_get(studyDbId, format=None):  # noqa: E501
    """Retrieve study Observation Units as table

     Scope: PHENOTYPING. Status: ACCEPTED. Implemented in Cassavabase, HIDAP and Germinate. Notes: Implementation target date: after PAG2016 Retrieve the details of the study required for field data collection. Includes actual trait data. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/table&lt;/a&gt; # noqa: E501

    :param studyDbId: Identifier of the study. Usually a number, could be alphanumeric.
    :type studyDbId: str
    :param format: The format parameter will cause the data to be dumped to a file in the specified format. Currently, tsv and csv are supported.
    :type format: str

    :rtype: StudyobservationsTableResponse
    """

#    return StudiesController_impl.studies_study_db_id_table_get(studyDbId, format=None)
    return "Not implemented"


def studies_study_db_id_table_post(studyDbId, newObservationsTableRequest=None):  # noqa: E501
    """Save study Observation Units as table

     This call can be used to create new observations in bulk. Note: If you need to update any existing observation, please use &#x60;PUT /studies/{studyDbId}/observations&#x60;. This call should only be used to create NEW observations. Implementation Guidelines: + All observations submitted through this call should create NEW observation records in the database under the given observation unit. + Each \&quot;observationUnitDbId\&quot; listed should already exist in the database. If the server can not find a given \&quot;observationUnitDbId\&quot;, it should report an error. (see Error Handling) + The response of this call should be the set of \&quot;observationDbIds\&quot; created from this call, along with the associated \&quot;observationUnitDbId\&quot; and \&quot;observationVariableDbId\&quot; that each observation is associated with. Images can optionally be saved using this call by providing a zipped file of all images in the datafiles. The physical zipped file should be transferred as well in the mulit-part form data. Scope: PHENOTYPING  # noqa: E501

    :param studyDbId: Identifier of the study. Usually a number, could be alphanumeric.
    :type studyDbId: str
    :param newObservationsTableRequest: 
    :type newObservationsTableRequest: dict | bytes

    :rtype: NewObservationDbIdsResponse
    """
    if connexion.request.is_json:
        newObservationsTableRequest = NewObservationsTableRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return StudiesController_impl.studies_study_db_id_table_post(studyDbId, newObservationsTableRequest=None)
    return "Not implemented"


def study_types_get(pageSize=None, page=None):  # noqa: E501
    """&lt;strong&gt;Deprecated&lt;/strong&gt; List study types

     ** DEPRECTED ** Use /studytypes Call to retrieve the list of study types. Scope: PHENOTYPING. Implementation target date: PAG2016  # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: StudyTypesResponse
    """

#    return StudiesController_impl.study_types_get(pageSize=None, page=None)
    return "Not implemented"


def studytypes_get(pageSize=None, page=None):  # noqa: E501
    """List study types

     Call to retrieve the list of study types. Scope: PHENOTYPING. Implementation target date: PAG2016 &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studytypes\&quot;&gt; test-server.brapi.org/brapi/v1/studytypes&lt;/a&gt; # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: StudyTypesResponse
    """

#    return StudiesController_impl.studytypes_get(pageSize=None, page=None)
    return "Not implemented"

