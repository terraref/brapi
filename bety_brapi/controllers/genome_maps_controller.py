import connexion
import six
#from bety_brapi.controllers_impl import GenomeMapsController_impl

from bety_brapi.models.genome_maps_response import GenomeMapsResponse  # noqa: E501
from bety_brapi.models.map_details_response import MapDetailsResponse  # noqa: E501
from bety_brapi.models.markers_response import MarkersResponse  # noqa: E501
from bety_brapi.models.markers_response1 import MarkersResponse1  # noqa: E501
from bety_brapi import util


def maps_get(species=None, type=None, pageSize=None, page=None):  # noqa: E501
    """Get list of maps

    Get list of maps &lt;br&gt; &lt;strong&gt;Status:&lt;/strong&gt; ACCEPTED &lt;strong&gt;Implemented by:&lt;/strong&gt; Germinate, Cassavabase &lt;strong&gt;Used by:&lt;/strong&gt; Flapjack do we need list of parents and specify mapping population? # noqa: E501

    :param species: Species name
    :type species: str
    :param type: Type of map
    :type type: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: GenomeMapsResponse
    """

#    return GenomeMapsController_impl.maps_get(species=None, type=None, pageSize=None, page=None)
    return "Not implemented"


def maps_map_db_id_get(mapDbId, pageSize=None, page=None):  # noqa: E501
    """Get map details

    Provides the number of markers on each linkageGroup and the max position on the linkageGroup &lt;br&gt; &lt;strong&gt;Status:&lt;/strong&gt; ACCEPTED &lt;strong&gt;Implemented by:&lt;/strong&gt; Germinate, Cassavabase &lt;strong&gt;Used by:&lt;/strong&gt; Flapjack # noqa: E501

    :param mapDbId: The internal db id of a selected map
    :type mapDbId: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: MapDetailsResponse
    """

#    return GenomeMapsController_impl.maps_map_db_id_get(mapDbId, pageSize=None, page=None)
    return "Not implemented"


def maps_map_db_id_positions_get(mapDbId, linkageGroupId=None, linkageGroupName=None, pageSize=None, page=None):  # noqa: E501
    """Get map data

    markers ordered by linkageGroup and position &lt;br&gt; &lt;strong&gt;Status:&lt;/strong&gt; ACCEPTED. &lt;strong&gt;Implemented by:&lt;/strong&gt; Germinate, Cassavabase &lt;strong&gt;Used by:&lt;/strong&gt; Flapjack # noqa: E501

    :param mapDbId: unique id of the map
    :type mapDbId: str
    :param linkageGroupId: &lt;strong&gt;Deprecated&lt;/strong&gt; Use linkageGroupName instead
    :type linkageGroupId: str
    :param linkageGroupName: The chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.
    :type linkageGroupName: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: MarkersResponse
    """

#    return GenomeMapsController_impl.maps_map_db_id_positions_get(mapDbId, linkageGroupId=None, linkageGroupName=None, pageSize=None, page=None)
    return "Not implemented"


def maps_map_db_id_positions_linkage_group_name_get(mapDbId, linkageGroupName, min=None, max=None, pageSize=None, page=None):  # noqa: E501
    """Get map data by range on linkageGroup

    markers ordered by linkageGroup and position # noqa: E501

    :param mapDbId: unique id of the map
    :type mapDbId: str
    :param linkageGroupName: The chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.
    :type linkageGroupName: str
    :param min: minimum position on linkage group
    :type min: int
    :param max: maximum position on linkage group
    :type max: int
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: MarkersResponse1
    """

#    return GenomeMapsController_impl.maps_map_db_id_positions_linkage_group_name_get(mapDbId, linkageGroupName, min=None, max=None, pageSize=None, page=None)
    return "Not implemented"

