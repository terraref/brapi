import connexion
import six
#from bety_brapi.controllers_impl import ObservationsController_impl

from bety_brapi.models.new_observation_db_ids_response import NewObservationDbIdsResponse  # noqa: E501
from bety_brapi.models.new_observation_unit_db_ids_response import NewObservationUnitDbIdsResponse  # noqa: E501
from bety_brapi.models.new_observation_unit_request import NewObservationUnitRequest  # noqa: E501
from bety_brapi.models.new_observations_request import NewObservationsRequest  # noqa: E501
from bety_brapi.models.new_observations_request_wrapper_deprecated import NewObservationsRequestWrapperDeprecated  # noqa: E501
from bety_brapi.models.new_observations_table_request import NewObservationsTableRequest  # noqa: E501
from bety_brapi.models.observation_levels_response import ObservationLevelsResponse  # noqa: E501
from bety_brapi.models.observation_units_response1 import ObservationUnitsResponse1  # noqa: E501
from bety_brapi.models.observations_response import ObservationsResponse  # noqa: E501
from bety_brapi.models.phenotypes_request import PhenotypesRequest  # noqa: E501
from bety_brapi.models.studyobservations_table_response import StudyobservationsTableResponse  # noqa: E501
from bety_brapi import util


def observation_levels_get(pageSize=None, page=None):  # noqa: E501
    """&lt;strong&gt;Deprecated&lt;/strong&gt; List observation levels

     ** DEPRECTED ** Use /observationlevels Call to retrieve the list of supported observation levels. Observation levels indicate the granularity level at which the measurements are taken. The values are used to supply the &#x60;observationLevel&#x60; parameter in the observation unit details call.  # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: ObservationLevelsResponse
    """

#    return ObservationsController_impl.observation_levels_get(pageSize=None, page=None)
    return "Not implemented"


def observationlevels_get(pageSize=None, page=None):  # noqa: E501
    """Get Observation Levels

     Call to retrieve the list of supported observation levels. Observation levels indicate the granularity level at which the measurements are taken. The values are used to supply the &#x60;observationLevel&#x60; parameter in the observation unit details call. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/observationlevels\&quot;&gt; test-server.brapi.org/brapi/v1/observationlevels&lt;/a&gt; # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: ObservationLevelsResponse
    """

#    return ObservationsController_impl.observationlevels_get(pageSize=None, page=None)
    return "Not implemented"


def phenotypes_post(format=None, body=None):  # noqa: E501
    """Save Observation Unit Phenotypes

    Scope: PHENOTYPING.   Notes:  Along with the study specific phenotype saving calls (in the observationUnit and table formats), this call allows phenotypes to be saved and images to optionally be transferred as well.        Call to invoke for saving the measurements (observations) collected from field for all the observation units. Observation timestamp should be ISO 8601 https://www.w3.org/TR/NOTE-datetime In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call. In this case a format parameter should be passed as well. Images can be optionally be uploaded using this call by providing a zipfile of all images in the datafiles, along with the actual zipfile in multi-part form data. # noqa: E501

    :param format: In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
    :type format: str
    :param body: 
    :type body: dict | bytes

    :rtype: NewObservationDbIdsResponse
    """
    if connexion.request.is_json:
        body = PhenotypesRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return ObservationsController_impl.phenotypes_post(format=None, body=None)
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

#    return ObservationsController_impl.studies_study_db_id_observations_get(studyDbId, observationVariableDbIds=None, pageSize=None, page=None)
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

#    return ObservationsController_impl.studies_study_db_id_observations_put(studyDbId, newObservations=None)
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

#    return ObservationsController_impl.studies_study_db_id_observationunits_get(studyDbId, observationLevel=None, pageSize=None, page=None)
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

#    return ObservationsController_impl.studies_study_db_id_observationunits_post(studyDbId, format, body=None)
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

#    return ObservationsController_impl.studies_study_db_id_observationunits_put(studyDbId, newObservationUnitRequest=None)
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

#    return ObservationsController_impl.studies_study_db_id_observationunits_zip_post(studyDbId, zipRequest=None)
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

#    return ObservationsController_impl.studies_study_db_id_table_get(studyDbId, format=None)
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

#    return ObservationsController_impl.studies_study_db_id_table_post(studyDbId, newObservationsTableRequest=None)
    return "Not implemented"

