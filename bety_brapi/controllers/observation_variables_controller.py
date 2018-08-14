import connexion
import six
#from bety_brapi.controllers_impl import ObservationVariablesController_impl

from bety_brapi.models.data_types_response import DataTypesResponse  # noqa: E501
from bety_brapi.models.observation_variable_response import ObservationVariableResponse  # noqa: E501
from bety_brapi.models.observation_variable_search_request import ObservationVariableSearchRequest  # noqa: E501
from bety_brapi.models.observation_variables_response import ObservationVariablesResponse  # noqa: E501
from bety_brapi.models.ontologies_response import OntologiesResponse  # noqa: E501
from bety_brapi.models.study_observation_variables_response import StudyObservationVariablesResponse  # noqa: E501
from bety_brapi.models.trait_response import TraitResponse  # noqa: E501
from bety_brapi.models.traits_response import TraitsResponse  # noqa: E501
from bety_brapi import util


def ontologies_get(pageSize=None, page=None):  # noqa: E501
    """Variable ontology list

    Call to retrieve a list of observation variable ontologies available in the system. &lt;br&gt; &lt;strong&gt;Scope:&lt;/strong&gt; CORE.  &lt;strong&gt;Status:&lt;/strong&gt; ACCEPTED. # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: OntologiesResponse
    """

#    return ObservationVariablesController_impl.ontologies_get(pageSize=None, page=None)
    return "Not implemented"


def studies_study_db_id_observation_variables_get(studyDbId):  # noqa: E501
    """&lt;strong&gt;Deprecated&lt;/strong&gt; Retrieve study observation variables

      &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/studies\&quot;&gt; test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationVariables&lt;/a&gt; # noqa: E501

    :param studyDbId: string database unique identifier
    :type studyDbId: str

    :rtype: StudyObservationVariablesResponse
    """

#    return ObservationVariablesController_impl.studies_study_db_id_observation_variables_get(studyDbId)
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

#    return ObservationVariablesController_impl.studies_study_db_id_observationvariables_get(studyDbId, pageSize=None, page=None)
    return "Not implemented"


def traits_get(pageSize=None, page=None):  # noqa: E501
    """List all traits

     Scope: CORE. Status: ACCEPTED. Implemented by: Germinate, Cassavabase Call to retrieve a list of traits available in the system and their associated variables. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/traits\&quot;&gt; test-server.brapi.org/brapi/v1/traits&lt;/a&gt; # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: TraitsResponse
    """

#    return ObservationVariablesController_impl.traits_get(pageSize=None, page=None)
    return "Not implemented"


def traits_trait_db_id_get(traitDbId):  # noqa: E501
    """Retrieve trait details by id

     Scope: CORE. Status: ACCEPTED. Implemented by: Germinate Retrieve the variables associated to a trait &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/traits\&quot;&gt; test-server.brapi.org/brapi/v1/traits/{traitDbId}&lt;/a&gt; # noqa: E501

    :param traitDbId: Id of the trait to retrieve details of.
    :type traitDbId: str

    :rtype: TraitResponse
    """

#    return ObservationVariablesController_impl.traits_trait_db_id_get(traitDbId)
    return "Not implemented"


def variables_datatypes_get(pageSize=None, page=None):  # noqa: E501
    """Variable data type list

    Call to retrieve a list of data types the variable can have. # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: DataTypesResponse
    """

#    return ObservationVariablesController_impl.variables_datatypes_get(pageSize=None, page=None)
    return "Not implemented"


def variables_get(pageSize=None, page=None, traitClass=None):  # noqa: E501
    """Variable list

    Call to retrieve a list of observationVariables available in the system. &lt;br&gt; &lt;strong&gt;Scope:&lt;/strong&gt; CORE. &lt;strong&gt;Status:&lt;/strong&gt; ACCEPTED. # noqa: E501

    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int
    :param traitClass: Variable&#39;s trait class (phenological, physiological, morphological, etc.)
    :type traitClass: str

    :rtype: ObservationVariablesResponse
    """

#    return ObservationVariablesController_impl.variables_get(pageSize=None, page=None, traitClass=None)
    return "Not implemented"


def variables_observation_variable_db_id_get(observationVariableDbId):  # noqa: E501
    """Variable details by id

    Retrieve variable details &lt;br&gt; &lt;strong&gt;Scope:&lt;/strong&gt; CORE &lt;strong&gt;Status:&lt;/strong&gt; ACCEPTED # noqa: E501

    :param observationVariableDbId: string id of the variable
    :type observationVariableDbId: str

    :rtype: ObservationVariableResponse
    """

#    return ObservationVariablesController_impl.variables_observation_variable_db_id_get(observationVariableDbId)
    return "Not implemented"


def variables_search_post(body=None):  # noqa: E501
    """Variable search

    Search observation variables. See &lt;a href&#x3D;\&quot;https://brapi.docs.apiary.io/#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details. &lt;br&gt; &lt;strong&gt;Scope:&lt;/strong&gt; CORE. &lt;strong&gt;Status:&lt;/strong&gt; ACCEPTED. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ObservationVariablesResponse
    """
    if connexion.request.is_json:
        body = ObservationVariableSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return ObservationVariablesController_impl.variables_search_post(body=None)
    return "Not implemented"

