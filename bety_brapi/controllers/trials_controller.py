import connexion
import six
#from bety_brapi.controllers_impl import TrialsController_impl

from bety_brapi.models.trial_response import TrialResponse  # noqa: E501
from bety_brapi.models.trials_response import TrialsResponse  # noqa: E501
from bety_brapi import util


def trials_get(programDbId=None, locationDbId=None, pageSize=None, page=None, active=None, sortBy=None, sortOrder=None):  # noqa: E501
    """List of trial summaries

     Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/trials\&quot;&gt; test-server.brapi.org/brapi/v1/trials&lt;/a&gt; # noqa: E501

    :param programDbId: Program filter to only return trials associated with given program id.
    :type programDbId: str
    :param locationDbId: Filter by location
    :type locationDbId: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int
    :param active: Filter active status true/false.
    :type active: bool
    :param sortBy: Sort order. Name of the field to sorty by.
    :type sortBy: str
    :param sortOrder: Sort order direction: asc/desc
    :type sortOrder: str

    :rtype: TrialsResponse
    """

#    return TrialsController_impl.trials_get(programDbId=None, locationDbId=None, pageSize=None, page=None, active=None, sortBy=None, sortOrder=None)
    return "Not implemented"


def trials_trial_db_id_get(trialDbId):  # noqa: E501
    """Get trial by Id

     Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016. Get trial by id. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/trials\&quot;&gt; test-server.brapi.org/brapi/v1/trials/{trialDbId}&lt;/a&gt; # noqa: E501

    :param trialDbId: The internal trialDbId
    :type trialDbId: str

    :rtype: TrialResponse
    """

#    return TrialsController_impl.trials_trial_db_id_get(trialDbId)
    return "Not implemented"

