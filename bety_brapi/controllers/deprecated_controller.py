import connexion
import six
#from bety_brapi.controllers_impl import DeprecatedController_impl

from bety_brapi.models.allele_matrix_search_request import AlleleMatrixSearchRequest  # noqa: E501
from bety_brapi.models.allele_matrix_values_response import AlleleMatrixValuesResponse  # noqa: E501
from bety_brapi.models.body import Body  # noqa: E501
from bety_brapi.models.body1 import Body1  # noqa: E501
from bety_brapi.models.common_crop_names_response import CommonCropNamesResponse  # noqa: E501
from bety_brapi.models.markers_response2 import MarkersResponse2  # noqa: E501
from bety_brapi.models.new_observations_request_wrapper_deprecated import NewObservationsRequestWrapperDeprecated  # noqa: E501
from bety_brapi.models.observation_levels_response import ObservationLevelsResponse  # noqa: E501
from bety_brapi.models.study_observation_variables_response import StudyObservationVariablesResponse  # noqa: E501
from bety_brapi.models.study_types_response import StudyTypesResponse  # noqa: E501
from bety_brapi import util


def allelematrix_search_get(markerprofileDbId=None, markerDbId=None, matrixDbId=None, format=None, expandHomozygotes=None, unknownString=None, sepPhased=None, sepUnphased=None, pageSize=None, page=None):  # noqa: E501
    """Scores through GET

    Status: ACCEPTED.  Implemented by: Germinate (POST only), Cassavabase  Used by: Flapjack (POST only)  See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details.  This uses a more efficient data structure and pagination for large number of markers.  See Search Services for additional implementation details. &lt;/br&gt; This uses a more efficient data structure and pagination for large number of markers.  &lt;/br&gt; Use GET when parameter size is less than 2K bytes. This method may support asynchronous processing. # noqa: E501

    :param markerprofileDbId: The markerprofile db ids. Not Required if &#39;markerDbId&#39; or &#39;matrixDbId&#39; is present.
    :type markerprofileDbId: List[str]
    :param markerDbId: ids of the markers. if none are specified, results are returned for all markers in the database. Not Required if &#39;markerprofileDbId&#39; or &#39;matrixDbId&#39; is present.
    :type markerDbId: List[str]
    :param matrixDbId: 
    :type matrixDbId: List[str]
    :param format: format for the datafile to be downloaded. tsv and csv currently supported; flapjack may be supported.
    :type format: str
    :param expandHomozygotes: Should homozygotes NOT be collapsed into a single occurrence?
    :type expandHomozygotes: bool
    :param unknownString: The string to use as a representation for missing data or the reserved word \&quot;empty_string\&quot;.
    :type unknownString: str
    :param sepPhased: The string to use as a separator for phased allele calls or the reserved word \&quot;empty_string\&quot;.
    :type sepPhased: str
    :param sepUnphased: The string to use as a separator for unphased allele calls or the reserved word \&quot;empty_string\&quot;.
    :type sepUnphased: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: AlleleMatrixValuesResponse
    """

#    return DeprecatedController_impl.allelematrix_search_get(markerprofileDbId=None, markerDbId=None, matrixDbId=None, format=None, expandHomozygotes=None, unknownString=None, sepPhased=None, sepUnphased=None, pageSize=None, page=None)
    return "Not implemented"


def allelematrix_search_post(markerprofileDbId):  # noqa: E501
    """Scores through POST

    Status: ACCEPTED.  Implemented by: Germinate (POST only), Cassavabase  Used by: Flapjack (POST only)  See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details.  This uses a more efficient data structure and pagination for large number of markers.  Use POST when parameter size is greater than 2K bytes.  - If no format is specified, this call returns the data in JSON form.  - If a format (other than JSON) is specified and the server supports this format, it will return the link to the exported data file in the \&quot;datafiles\&quot; field of the \&quot;metadata\&quot;.  - If more than one format is requested at a time, the server will throw a \&quot;501 Not Implemented\&quot; error.  The format of the tsv response can be found on GitHub (https://github.com/plantbreeding/Documentation/wiki/BrAPI-TSV-Expected-Formats) # noqa: E501

    :param markerprofileDbId: The markerprofile db ids. Not Required if &#39;markerDbId&#39; or &#39;matrixDbId&#39; is present.
    :type markerprofileDbId: dict | bytes

    :rtype: AlleleMatrixValuesResponse
    """
    if connexion.request.is_json:
        markerprofileDbId = AlleleMatrixSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return DeprecatedController_impl.allelematrix_search_post(markerprofileDbId)
    return "Not implemented"


def crops_get(pageSize=None, page=None):  # noqa: E501
    """List supported crops

    For multi crop systems this is a useful call to list all the supported crops.  &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/crops\&quot;&gt; test-server.brapi.org/brapi/v1/crops&lt;/a&gt; # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: CommonCropNamesResponse
    """

#    return DeprecatedController_impl.crops_get(pageSize=None, page=None)
    return "Not implemented"


def login_post(body=None):  # noqa: E501
    """Login

    Implemented by: Tripal Brapi module, Cassavabase, Germinate, BMS  Used by: Flapjack, BMS  Response data types Exception: the result is not embeded in a \&quot;result\&quot; structure in order to be (one day) OAuth2 compliant. It&#39;s also why the anwser mixes snake_case and camelCase. For login, returns a hash with the user name and the token as the value. A metadata key is also present (but usually set to null, unless an error condition occurs).  For logout, returns an empty resource. A token to remove could be provided (amdin interface) but it is not required. By default, current user token will be removed.  |Variable|Datatype|Description|Required|   |------|------|------|:-----:| | userDisplayName| string| the display name of the user | Y | | access_token | string | the access token for the session | Y | | expires_in | integer | The lifetime in seconds of the access token | Y |  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501

#    return DeprecatedController_impl.login_post(body=None)
    return "Not implemented"


def logout_delete(body=None):  # noqa: E501
    """Logout

    Implemented by: Tripal Brapi module, Cassavabase, Germinate, BMS  Used by: Flapjack, BMS  For logout, returns an empty resource. A token to remove could be provided (amdin interface) but it is not required. By default, current user token will be removed. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501

#    return DeprecatedController_impl.logout_delete(body=None)
    return "Not implemented"


def markers_get(name=None, matchMethod=None, include=None, type=None, pageSize=None, page=None):  # noqa: E501
    """Markers Search (/markers)

     Scope: CORE.  Status: ACCEPTED. Implemented by: Germinate See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details. Other service requests use the servers internal &#x60;markerDbId&#x60;. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria. - If there is none, an empty array is returned. - If there is one or more than one match, returns an array of all marker records that match the search criteria.  # noqa: E501

    :param name: The name or synonym.
    :type name: str
    :param matchMethod: Possible values are &#39;case_insensitive&#39;, &#39;exact&#39; (case sensitive), &#39;wildcard&#39; (which is case insensitive). Wildcard uses both &#39;*&#39; and &#39;%&#39; for any number of characters and &#39;?&#39; for one character matching. Default is exact.
    :type matchMethod: str
    :param include: Whether to include synonyms in the output.
    :type include: str
    :param type: The type of the marker.
    :type type: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: MarkersResponse2
    """

#    return DeprecatedController_impl.markers_get(name=None, matchMethod=None, include=None, type=None, pageSize=None, page=None)
    return "Not implemented"


def observation_levels_get(pageSize=None, page=None):  # noqa: E501
    """&lt;strong&gt;Deprecated&lt;/strong&gt; List observation levels

     ** DEPRECTED ** Use /observationlevels Call to retrieve the list of supported observation levels. Observation levels indicate the granularity level at which the measurements are taken. The values are used to supply the &#x60;observationLevel&#x60; parameter in the observation unit details call.  # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: ObservationLevelsResponse
    """

#    return DeprecatedController_impl.observation_levels_get(pageSize=None, page=None)
    return "Not implemented"


def studies_study_db_id_observation_variables_get(studyDbId):  # noqa: E501
    """&lt;strong&gt;Deprecated&lt;/strong&gt; Retrieve study observation variables

      &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationVariables&lt;/a&gt; # noqa: E501

    :param studyDbId: string database unique identifier
    :type studyDbId: str

    :rtype: StudyObservationVariablesResponse
    """

#    return DeprecatedController_impl.studies_study_db_id_observation_variables_get(studyDbId)
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

#    return DeprecatedController_impl.studies_study_db_id_observationunits_post(studyDbId, format, body=None)
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

#    return DeprecatedController_impl.study_types_get(pageSize=None, page=None)
    return "Not implemented"

