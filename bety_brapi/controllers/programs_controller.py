import connexion
import six
#from bety_brapi.controllers_impl import ProgramsController_impl

from bety_brapi.models.programs_response import ProgramsResponse  # noqa: E501
from bety_brapi.models.programs_search_request import ProgramsSearchRequest  # noqa: E501
from bety_brapi import util


def programs_get(programName=None, abbreviation=None, pageSize=None, page=None):  # noqa: E501
    """List programs

     Call to retrieve a list of programs. Status: ACCEPTED Implemented By: &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/programs\&quot;&gt; test-server.brapi.org/brapi/v1/programs&lt;/a&gt; # noqa: E501

    :param programName: Filter by program name. Exact match.
    :type programName: str
    :param abbreviation: Filter by program abbreviation. Exact match.
    :type abbreviation: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: ProgramsResponse
    """

#    return ProgramsController_impl.programs_get(programName=None, abbreviation=None, pageSize=None, page=None)
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

#    return ProgramsController_impl.programs_search_post(body=None)
    return "Not implemented"

