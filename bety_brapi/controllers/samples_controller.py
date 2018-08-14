import connexion
import six
#from bety_brapi.controllers_impl import SamplesController_impl

from bety_brapi.models.new_sample_db_id import NewSampleDbId  # noqa: E501
from bety_brapi.models.sample import Sample  # noqa: E501
from bety_brapi.models.sample_response import SampleResponse  # noqa: E501
from bety_brapi.models.sample_search_request import SampleSearchRequest  # noqa: E501
from bety_brapi.models.samples_response import SamplesResponse  # noqa: E501
from bety_brapi import util


def samples_put(sample=None):  # noqa: E501
    """Add a sample

    Call to register the event of a sample being taken. Sample ID is assigned as a result of the operation and returned in response.  # noqa: E501

    :param sample: 
    :type sample: dict | bytes

    :rtype: NewSampleDbId
    """
    if connexion.request.is_json:
        sample = Sample.from_dict(connexion.request.get_json())  # noqa: E501

#    return SamplesController_impl.samples_put(sample=None)
    return "Not implemented"


def samples_sample_db_id_get(sampleDbId):  # noqa: E501
    """Get Sample

     Used to retrieve the details of a single Sample from a Sample Tracking system. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/samples\&quot;&gt; test-server.brapi.org/brapi/v1/samples/{sampleDbId}&lt;/a&gt; # noqa: E501

    :param sampleDbId: the internal DB id for a sample
    :type sampleDbId: str

    :rtype: SampleResponse
    """

#    return SamplesController_impl.samples_sample_db_id_get(sampleDbId)
    return "Not implemented"


def samples_search_get(sampleDbId=None, observationUnitDbId=None, plateDbId=None, germplasmDbId=None, pageSize=None, page=None):  # noqa: E501
    """Get Sample Search

     Used to retrieve list of Samples from a Sample Tracking system based on some search criteria. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/samples\&quot;&gt; test-server.brapi.org/brapi/v1/samples-search&lt;/a&gt; # noqa: E501

    :param sampleDbId: the internal DB id for a sample
    :type sampleDbId: str
    :param observationUnitDbId: the internal DB id for an observation unit where a sample was taken from
    :type observationUnitDbId: str
    :param plateDbId: the internal DB id for a plate of samples
    :type plateDbId: str
    :param germplasmDbId: the internal DB id for a germplasm
    :type germplasmDbId: str
    :param pageSize: The size of the pages to be returned. Default is 1000.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is 0.
    :type page: int

    :rtype: SamplesResponse
    """

#    return SamplesController_impl.samples_search_get(sampleDbId=None, observationUnitDbId=None, plateDbId=None, germplasmDbId=None, pageSize=None, page=None)
    return "Not implemented"


def samples_search_post(sampleSearch=None):  # noqa: E501
    """Post Sample Search

     Used to retrieve list of Samples from a Sample Tracking system based on some search criteria. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/samples\&quot;&gt; test-server.brapi.org/brapi/v1/samples-search&lt;/a&gt; # noqa: E501

    :param sampleSearch: 
    :type sampleSearch: dict | bytes

    :rtype: SamplesResponse
    """
    if connexion.request.is_json:
        sampleSearch = SampleSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return SamplesController_impl.samples_search_post(sampleSearch=None)
    return "Not implemented"

