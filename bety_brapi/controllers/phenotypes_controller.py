import connexion
import six
from bety_brapi.controllers_impl import PhenotypesController_impl

from bety_brapi.models.new_observation_db_ids_response import NewObservationDbIdsResponse  # noqa: E501
from bety_brapi.models.observation_units_response import ObservationUnitsResponse  # noqa: E501
from bety_brapi.models.observation_units_table_response1 import ObservationUnitsTableResponse1  # noqa: E501
from bety_brapi.models.phenotypes_request import PhenotypesRequest  # noqa: E501
from bety_brapi.models.phenotypes_search_request import PhenotypesSearchRequest  # noqa: E501
from bety_brapi import util


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

#    return PhenotypesController_impl.phenotypes_post(format=None, body=None)
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

#    return PhenotypesController_impl.phenotypes_search_csv_post(body=None)
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
    if observationTimeStampRangeStart:
        observationTimeStampRangeStart = util.deserialize_datetime(observationTimeStampRangeStart)

    if observationTimeStampRangeEnd:
        observationTimeStampRangeEnd = util.deserialize_datetime(observationTimeStampRangeEnd)

    return PhenotypesController_impl.phenotypes_search_get(germplasmDbId, observationVariableDbId, studyDbId, locationDbId, trialDbId, programDbId, seasonDbId, observationLevel, observationTimeStampRangeStart, observationTimeStampRangeEnd, pageSize, page)


def phenotypes_search_post(body=None):  # noqa: E501
    """Phenotype Search

    Scope: PHENOTYPING. Status: ACCEPTED.  Returns a list of observationUnit with the observed Phenotypes.  See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details.  Implemented for GnpIS and PHIS data (https://urgi.versailles.inra.fr/ws/webresources/brapi/v1/phenotypes).  Use case: this section allows to get a dataset from multiple studies. It allows to integrate data from several databases. Refactor note : This call allows to get and integrate portions of multiple phenotyping data matrixes. A proposed evolution allowed to get a list of single observations, this functionality is still possible with this call by specifybing the observation variable, see below. Example Use cases: - Study a panel of germplasm accross multiple studies, search parameters : {\&quot;germplasmDbIds\&quot; : [ \&quot;Syrah\&quot;, \&quot;34Mtp362\&quot; ]} - Get all data for a specific study : {\&quot;studyDbIds\&quot; : [ \&quot;383\&quot; ]} - Get simple atomic phenotyping values : {\&quot;germplasmDbIds\&quot; : [ \&quot;Syrah\&quot;, \&quot;34Mtp362\&quot; ], \&quot;observationVariableDbIds\&quot; : [ \&quot;CO_345:0000043\&quot;]} - Study Locations for adaptation to climat change : {\&quot;locationDbIds\&quot; : [ \&quot;383838\&quot;, \&quot;MONTPELLIER\&quot; ], \&quot;germplasmDbIds\&quot; : [ \&quot;all ids for a given species\&quot;]} - Find phenotypes that are from after a certain timestamp  observationTimeStamp : Iso Standard 8601.  observationValue data type inferred from the ontology # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ObservationUnitsResponse
    """
    if connexion.request.is_json:
        body = PhenotypesSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return PhenotypesController_impl.phenotypes_search_post(body=None)
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

#    return PhenotypesController_impl.phenotypes_search_table_post(body=None)
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

#    return PhenotypesController_impl.phenotypes_search_tsv_post(body=None)
    return "Not implemented"

