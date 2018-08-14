import connexion
import six
#from bety_brapi.controllers_impl import VendorSamplesController_impl

from bety_brapi.models.vendor_plate_request import VendorPlateRequest  # noqa: E501
from bety_brapi.models.vendor_plate_response import VendorPlateResponse  # noqa: E501
from bety_brapi.models.vendor_plate_search_request import VendorPlateSearchRequest  # noqa: E501
from bety_brapi.models.vendor_plates_response import VendorPlatesResponse  # noqa: E501
from bety_brapi.models.vendor_plates_response1 import VendorPlatesResponse1  # noqa: E501
from bety_brapi.models.vendor_specification_response import VendorSpecificationResponse  # noqa: E501
from bety_brapi import util


def vendor_plates_post(body=None):  # noqa: E501
    """Register plates

    Note: if the samples array is empty, plate ID will be returned. Samples can be updated later. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: VendorPlatesResponse
    """
    if connexion.request.is_json:
        body = VendorPlateRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return VendorSamplesController_impl.vendor_plates_post(body=None)
    return "Not implemented"


def vendor_plates_search_get(vendorProjectDbId=None, vendorPlateDbId=None, clientPlateDbId=None, sampleInfo=None, pageSize=None, page=None):  # noqa: E501
    """Search for plates

    Search for plates in the database.  &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/vendor/plates-search\&quot;&gt; test-server.brapi.org/brapi/v1/vendor/plates-search&lt;/a&gt; # noqa: E501

    :param vendorProjectDbId: 
    :type vendorProjectDbId: str
    :param vendorPlateDbId: 
    :type vendorPlateDbId: str
    :param clientPlateDbId: 
    :type clientPlateDbId: str
    :param sampleInfo: 
    :type sampleInfo: bool
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: VendorPlatesResponse1
    """

#    return VendorSamplesController_impl.vendor_plates_search_get(vendorProjectDbId=None, vendorPlateDbId=None, clientPlateDbId=None, sampleInfo=None, pageSize=None, page=None)
    return "Not implemented"


def vendor_plates_search_post(body=None):  # noqa: E501
    """Search for plates

    Search for plates in the database.  &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/vendor\&quot;&gt; test-server.brapi.org/brapi/v1/vendor/plate-search&lt;/a&gt; # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: VendorPlatesResponse
    """
    if connexion.request.is_json:
        body = VendorPlateSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501

#    return VendorSamplesController_impl.vendor_plates_search_post(body=None)
    return "Not implemented"


def vendor_plates_vendor_plate_db_id_get(vendorPlateDbId):  # noqa: E501
    """Plate Details by vendorPlateId

     Response data types   &lt;table&gt; &lt;thead&gt; &lt;tr&gt; &lt;th&gt;Variable&lt;/th&gt; &lt;th&gt;Datatype&lt;/th&gt; &lt;th&gt;Description&lt;/th&gt; &lt;th&gt;Required&lt;/th&gt; &lt;/tr&gt; &lt;/thead&gt; &lt;tbody&gt; &lt;tr&gt; &lt;td&gt;metadata&lt;/td&gt; &lt;td&gt;object&lt;/td&gt; &lt;td&gt;pagination, status&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;pagination&lt;/td&gt; &lt;td&gt;object&lt;/td&gt; &lt;td&gt;pageSize, currentPage, totalCount, totalPages&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;status&lt;/td&gt; &lt;td&gt;list&lt;/td&gt; &lt;td&gt;code, message&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;result&lt;/td&gt; &lt;td&gt;Object&lt;/td&gt; &lt;td&gt;Object containing MCPD data&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;vendorProjectDbId&lt;/td&gt; &lt;td&gt;string&lt;/td&gt; &lt;td&gt;the name or identifier given to a project by the vendor&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;vendorPlateDbId&lt;/td&gt; &lt;td&gt;string&lt;/td&gt; &lt;td&gt;the name or identifier of the plate, given by the vendor&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;clientPlateDbId&lt;/td&gt; &lt;td&gt;string&lt;/td&gt; &lt;td&gt;the name of the plate, given by the client&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;barcode&lt;/td&gt; &lt;td&gt;string&lt;/td&gt; &lt;td&gt;a string that can be represented as a barcode, identifying this plate&lt;/td&gt; &lt;td&gt;N&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;plateFormat&lt;/td&gt; &lt;td&gt;string&lt;/td&gt; &lt;td&gt;defines that plate format, usually Plate_96 or tubes for plateless format&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;sampleType&lt;/td&gt; &lt;td&gt;string&lt;/td&gt; &lt;td&gt;DNA or RNA or Tissue, etc.&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;status&lt;/td&gt; &lt;td&gt;string&lt;/td&gt; &lt;td&gt;The status of the plate in the processing pipeline. Typically,  &amp;quot;Received&amp;quot;, &amp;quot;Processing&amp;quot;, &amp;quot;QC_passed&amp;quot;, QC_failed&amp;quot;, &amp;quot;Completed&amp;quot; (as per vendor-requirements call)&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;samples&lt;/td&gt; &lt;td&gt;Array&lt;/td&gt; &lt;td&gt;list of samples in the plate&lt;/td&gt; &lt;td&gt;Y&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;  &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/vendor\&quot;&gt; test-server.brapi.org/brapi/v1/vendor/plate/{vendorPlateDbId}&lt;/a&gt; # noqa: E501

    :param vendorPlateDbId: The plate ID defined by the vendor
    :type vendorPlateDbId: str

    :rtype: VendorPlateResponse
    """

#    return VendorSamplesController_impl.vendor_plates_vendor_plate_db_id_get(vendorPlateDbId)
    return "Not implemented"


def vendor_specifications_get():  # noqa: E501
    """Vendor specification

     Defines the plate format specification for the vendor. &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/vendor\&quot;&gt; test-server.brapi.org/brapi/v1/vendor/specifications&lt;/a&gt; # noqa: E501


    :rtype: VendorSpecificationResponse
    """

#    return VendorSamplesController_impl.vendor_specifications_get()
    return "Not implemented"

