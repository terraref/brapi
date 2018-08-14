import connexion
import six
#from bety_brapi.controllers_impl import MarkersController_impl

from bety_brapi.models.marker_response import MarkerResponse  # noqa: E501
from bety_brapi.models.markers_response2 import MarkersResponse2  # noqa: E501
from bety_brapi.models.markers_search_request import MarkersSearchRequest  # noqa: E501
from bety_brapi import util


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

#    return MarkersController_impl.markers_get(name=None, matchMethod=None, include=None, type=None, pageSize=None, page=None)
    return "Not implemented"


def markers_marker_db_id_get(markerDbId):  # noqa: E501
    """Marker Details by id

    &lt;strong&gt;Status&lt;/strong&gt;: ACCEPTED  &lt;strong&gt;Implemented By&lt;/strong&gt;: # noqa: E501

    :param markerDbId: the internal id of the marker
    :type markerDbId: str

    :rtype: MarkerResponse
    """

#    return MarkersController_impl.markers_marker_db_id_get(markerDbId)
    return "Not implemented"


def markers_search_get(markerDbIds=None, name=None, matchMethod=None, includeSynonyms=None, type=None, pageSize=None, page=None):  # noqa: E501
    """Markers Search (GET)

     Scope: CORE.  Status: ACCEPTED. Implemented by: Germinate See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details. Other service requests use the servers internal &#x60;markerDbId&#x60;. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria. - If there is none, an empty array is returned. - If there is one or more than one match, returns an array of all marker records that match the search criteria.  # noqa: E501

    :param markerDbIds: The database IDs of the markers to search for
    :type markerDbIds: List[str]
    :param name: The search pattern for a marker name or synonym. Examples: \&quot;11_10002\&quot; \&quot;11_1%\&quot; \&quot;11_1*\&quot; \&quot;11_10?02\&quot;
    :type name: str
    :param matchMethod: Possible values are &#39;case_insensitive&#39;, &#39;exact&#39; (case sensitive), &#39;wildcard&#39; (which is case insensitive). Wildcard uses both &#39;*&#39; and &#39;%&#39; for any number of characters and &#39;?&#39; for one character matching. Default is exact.
    :type matchMethod: str
    :param includeSynonyms: Whether to include synonyms in the output.
    :type includeSynonyms: bool
    :param type: The type of the marker.
    :type type: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: MarkersResponse2
    """

#    return MarkersController_impl.markers_search_get(markerDbIds=None, name=None, matchMethod=None, includeSynonyms=None, type=None, pageSize=None, page=None)
    return "Not implemented"


def markers_search_post(markerDbIds=None):  # noqa: E501
    """Markers Search (POST)

     Scope: CORE.  Status: ACCEPTED. Implemented by: Germinate See &lt;a href&#x3D;\&quot;#introduction/search-services\&quot;&gt;Search Services&lt;/a&gt; for additional implementation details. Other service requests use the servers internal &#x60;markerDbId&#x60;. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria. - If there is none, an empty array is returned. - If there is one or more than one match, returns an array of all marker records that match the search criteria.  # noqa: E501

    :param markerDbIds: The database IDs of the markers to search for
    :type markerDbIds: dict | bytes

    :rtype: MarkersResponse2
    """
    if connexion.request.is_json:
        markerDbIds = MarkersSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return MarkersController_impl.markers_search_post(markerDbIds=None)
    return "Not implemented"

