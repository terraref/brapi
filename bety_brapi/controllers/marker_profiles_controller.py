import connexion
import six
#from bety_brapi.controllers_impl import MarkerProfilesController_impl

from bety_brapi.models.allele_matrix_details_response import AlleleMatrixDetailsResponse  # noqa: E501
from bety_brapi.models.allele_matrix_search_request import AlleleMatrixSearchRequest  # noqa: E501
from bety_brapi.models.allele_matrix_values_response import AlleleMatrixValuesResponse  # noqa: E501
from bety_brapi.models.marker_profile_descriptions_response import MarkerProfileDescriptionsResponse  # noqa: E501
from bety_brapi.models.marker_profiles_response import MarkerProfilesResponse  # noqa: E501
from bety_brapi import util


def allelematrices_get(studyDbId, pageSize=None, page=None):  # noqa: E501
    """Matrices through GET

    &lt;strong&gt;Status&lt;/strong&gt;: Proposed &lt;strong&gt;Implemented by&lt;/strong&gt;: GOBII &lt;strong&gt;Used by&lt;/strong&gt;: Flapjack &lt;/br&gt; This resource is used for reading and writing genomic matrices: &lt;/br&gt; GET provides a list of available matrices, optionally filtered by study; POST will provide a means for adding new matrices (content TBD). # noqa: E501

    :param studyDbId: restricts the list of matrices to a specific study.
    :type studyDbId: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: AlleleMatrixDetailsResponse
    """

#    return MarkerProfilesController_impl.allelematrices_get(studyDbId, pageSize=None, page=None)
    return "Not implemented"


def allelematrices_search_get(markerprofileDbId=None, markerDbId=None, matrixDbId=None, format=None, expandHomozygotes=None, unknownString=None, sepPhased=None, sepUnphased=None, pageSize=None, page=None):  # noqa: E501
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

#    return MarkerProfilesController_impl.allelematrices_search_get(markerprofileDbId=None, markerDbId=None, matrixDbId=None, format=None, expandHomozygotes=None, unknownString=None, sepPhased=None, sepUnphased=None, pageSize=None, page=None)
    return "Not implemented"


def allelematrices_search_post(markerprofileDbId):  # noqa: E501
    """Scores through POST

    Status: ACCEPTED.  Implemented by: Germinate (POST only), Cassavabase  Used by: Flapjack (POST only)  See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details.  This uses a more efficient data structure and pagination for large number of markers.  Use POST when parameter size is greater than 2K bytes.  - If no format is specified, this call returns the data in JSON form.  - If a format (other than JSON) is specified and the server supports this format, it will return the link to the exported data file in the \&quot;datafiles\&quot; field of the \&quot;metadata\&quot;.  - If more than one format is requested at a time, the server will throw a \&quot;501 Not Implemented\&quot; error.  The format of the tsv response can be found on GitHub (https://github.com/plantbreeding/Documentation/wiki/BrAPI-TSV-Expected-Formats) # noqa: E501

    :param markerprofileDbId: The markerprofile db ids. Not Required if &#39;markerDbId&#39; or &#39;matrixDbId&#39; is present.
    :type markerprofileDbId: dict | bytes

    :rtype: AlleleMatrixValuesResponse
    """
    if connexion.request.is_json:
        markerprofileDbId = AlleleMatrixSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return MarkerProfilesController_impl.allelematrices_search_post(markerprofileDbId)
    return "Not implemented"


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

#    return MarkerProfilesController_impl.allelematrix_search_get(markerprofileDbId=None, markerDbId=None, matrixDbId=None, format=None, expandHomozygotes=None, unknownString=None, sepPhased=None, sepUnphased=None, pageSize=None, page=None)
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

#    return MarkerProfilesController_impl.allelematrix_search_post(markerprofileDbId)
    return "Not implemented"


def markerprofiles_get(germplasmDbId=None, studyDbId=None, sampleDbId=None, extractDbId=None, pageSize=None, page=None):  # noqa: E501
    """Retrieve Markerprofile Ids

    &lt;strong&gt;Scope&lt;/strong&gt;: GENOTYPING. &lt;strong&gt;Status&lt;/strong&gt;: ACCEPTED. &lt;strong&gt;Implemented by&lt;/strong&gt;: Germinate &lt;strong&gt;Used by&lt;/strong&gt;: Flapjack &lt;/br&gt; For the requested Germplasm Id and/or Extract Id, returns the Markerprofile Id and number of non-missing allele calls (marker/allele pairs). # noqa: E501

    :param germplasmDbId: The server&#39;s internal ids for the Germplasm IDs, as returned by the &lt;strong&gt;Find markerprofile by Germplasm&lt;/strong&gt; service.
    :type germplasmDbId: str
    :param studyDbId: The server&#39;s internal id for the StudyDbId
    :type studyDbId: str
    :param sampleDbId: The server&#39;s internal id for the SampleDbId
    :type sampleDbId: str
    :param extractDbId: The server&#39;s internal id for the ExtractDbId
    :type extractDbId: str
    :param pageSize: The number of allele call results (marker/allele pairs) to be returned in the response. If multiple experiments are requested, some responses will contain the last results from one experiment followed by the first results from the next.
    :type pageSize: int
    :param page: Required if &#x60;pageSize&#x60; is given; and requires that &#x60;pageSize&#x60; be given. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D;0)
    :type page: int

    :rtype: MarkerProfileDescriptionsResponse
    """

#    return MarkerProfilesController_impl.markerprofiles_get(germplasmDbId=None, studyDbId=None, sampleDbId=None, extractDbId=None, pageSize=None, page=None)
    return "Not implemented"


def markerprofiles_markerprofile_db_id_get(markerprofileDbId, expandHomozygotes=None, unknownString=None, sepPhased=None, sepUnphased=None, pageSize=None, page=None):  # noqa: E501
    """Alleles By Markerprofile Id

    &lt;strong&gt;Scope&lt;/strong&gt;:GENOTYPING. &lt;strong&gt;Status&lt;/strong&gt;: ACCEPTED. &lt;strong&gt;Implemented by&lt;/strong&gt;: Germinate, Cassavabase &lt;/br&gt; For the requested markerprofile ID, returns the allele call for each marker.  [Example](http://malt.pw.usda.gov/t3/wheatplus/markerprofiles/1784_99/count?analysisMethod&#x3D;GoldenGate) &lt;/br&gt; &lt;strong&gt;Allele encodings&lt;/strong&gt;  - Unknown data will by default be encoded by \&quot;N\&quot; - Homozygotes are returned as a single occurance, e.g. AA -&gt; A, GG -&gt; G - Phased heterozygotes are by default separated by a pipe (\&quot;|\&quot;) and unphased heterozygotes are by default separated by a forward slash (\&quot;/\&quot;) - Dominant markers such as DArTs: 1 for present, 0 for absent  &lt;strong&gt;Parameters&lt;/strong&gt; - If the user would like to use an empty string (\&quot;\&quot;) for any of the parameters, the value should be set to the reserved word \&quot;empty_string\&quot;, e.g. sepUnphased&#x3D;empty_string.  &lt;strong&gt;Open issue:&lt;/strong&gt; The pages of data will need to be sorted sensibly in order for the requested page to be delivered consistently.  By map or genome position? Alphabetically?&#39; # noqa: E501

    :param markerprofileDbId: The server&#39;s internal id for the markerprofile
    :type markerprofileDbId: str
    :param expandHomozygotes: Should homozygotes NOT be collapsed into a single orrucance?
    :type expandHomozygotes: bool
    :param unknownString: The string to use as a representation for missing data or the reserved word \&quot;empty_string\&quot;.
    :type unknownString: str
    :param sepPhased: The string to use as a separator for phased allele calls or the reserved word \&quot;empty_string\&quot;.
    :type sepPhased: str
    :param sepUnphased: The string to use as a separator for unphased allele calls or the reserved word \&quot;empty_string\&quot;.
    :type sepUnphased: str
    :param pageSize: The number of allele call results (marker/allele pairs) to be returned in the response. If multiple experiments are requested, some responses will contain the last results from one experiment followed by the first results from the next.
    :type pageSize: int
    :param page: Required if &#x60;pageSize&#x60; is given; and requires that &#x60;pageSize&#x60; be given. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D;0)
    :type page: int

    :rtype: MarkerProfilesResponse
    """

#    return MarkerProfilesController_impl.markerprofiles_markerprofile_db_id_get(markerprofileDbId, expandHomozygotes=None, unknownString=None, sepPhased=None, sepUnphased=None, pageSize=None, page=None)
    return "Not implemented"

