import connexion
import six
#from bety_brapi.controllers_impl import LocationsController_impl

from bety_brapi.models.location_response import LocationResponse  # noqa: E501
from bety_brapi.models.locations_response import LocationsResponse  # noqa: E501
from bety_brapi import util


def locations_get(locationType=None, pageSize=None, page=None):  # noqa: E501
    """locations_get

     Implemented by: Germinate Get a list of locations. * The &#x60;countryCode&#x60; is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec. * &#x60;altitude&#x60; is in meters. **Note**: Consider revising to describe polygon lat/lan points and check if adopting http://geojson.org/ is worth doing for v1.  # noqa: E501

    :param locationType: Filter by location type specified.
    :type locationType: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: LocationsResponse
    """

#    return LocationsController_impl.locations_get(locationType=None, pageSize=None, page=None)
    return "Not implemented"


def locations_location_db_id_get(locationDbId):  # noqa: E501
    """The internal DB id for a location

     &lt;strong&gt;Implemented by:&lt;/strong&gt;  GnpIS Get details for a location. * The &#x60;countryCode&#x60; is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec. * &#x60;altitude&#x60; is in meters.  # noqa: E501

    :param locationDbId: The internal DB id for a location
    :type locationDbId: str

    :rtype: LocationResponse
    """

#    return LocationsController_impl.locations_location_db_id_get(locationDbId)
    return "Not implemented"

