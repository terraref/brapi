import connexion
import six
#from bety_brapi.controllers_impl import CallsController_impl

from bety_brapi.models.calls_response import CallsResponse  # noqa: E501
from bety_brapi import util


def calls_get(datatype=None, pageSize=None, page=None):  # noqa: E501
    """Call search

    &lt;strong&gt;Implementation Notes&lt;/strong&gt; Having a consistent structure for the path string of each call is very important for teams to be able to connect and find errors. Read more on &lt;a href&#x3D;\&quot;https://github.com/plantbreeding/API/issues/144\&quot;&gt;Github&lt;/a&gt;. Here are the rules for the path of each call that should be returned &lt;ul&gt;          &lt;li&gt;Every word in the call path should match the documentation exactly, both in spelling and capitalization. Note that path strings are all lower case, but path parameters are camel case.&lt;/li&gt;           &lt;li&gt;Each path should start relative to &#39;/&#39; and therefore should not include &#39;/&#39;&lt;/li&gt;   &lt;li&gt;No leading or trailing slashes (&#39;/&#39;) &lt;/li&gt;   &lt;li&gt;Path parameters are wrapped in curly braces (&#39;{}&#39;). The name of the path parameter should be spelled exactly as it is specified in the documentation.&lt;/li&gt;         &lt;/ul&gt; &lt;table&gt;   &lt;tr&gt;     &lt;th&gt;Examples&lt;/th&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;strong&gt;GOOD&lt;/strong&gt;&lt;/td&gt;     &lt;td&gt;\&quot;call\&quot;: \&quot;germplasm/{germplasmDbId}/markerprofiles\&quot;&lt;/td&gt;   &lt;/tr&gt;    &lt;tr&gt;     &lt;td&gt;BAD&lt;/td&gt;     &lt;td&gt;\&quot;call\&quot;: \&quot;germplasm/{&lt;strong&gt;id&lt;/strong&gt;}/markerprofiles\&quot;&lt;/td&gt;   &lt;/tr&gt;    &lt;tr&gt;     &lt;td&gt;BAD&lt;/td&gt;     &lt;td&gt;\&quot;call\&quot;: \&quot;germplasm/{germplasmDbId}/marker&lt;strong&gt;P&lt;/strong&gt;rofiles\&quot;&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;BAD&lt;/td&gt;     &lt;td&gt;\&quot;call\&quot;: \&quot;germplasm/{germplasm&lt;strong&gt;dbid&lt;/strong&gt;}/markerprofiles\&quot;&lt;/td&gt;   &lt;/tr&gt;    &lt;tr&gt;     &lt;td&gt;BAD&lt;/td&gt;     &lt;td&gt;\&quot;call\&quot;: \&quot;&lt;strong&gt;brapi/v1&lt;/strong&gt;/germplasm/{germplasmDbId}/markerprofiles\&quot;&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;BAD&lt;/td&gt;     &lt;td&gt;\&quot;call\&quot;: \&quot;&lt;strong&gt;/g&lt;/strong&gt;ermplasm/{germplasmDbId}/markerprofile&lt;strong&gt;s/&lt;/strong&gt;\&quot;&lt;/td&gt;   &lt;/tr&gt;    &lt;tr&gt;     &lt;td&gt;BAD&lt;/td&gt;     &lt;td&gt;\&quot;call\&quot;: \&quot;germplasm/&lt;strong&gt;&amp;lt&lt;/strong&gt;germplasmDbId&lt;strong&gt;&amp;gt&lt;/strong&gt;/markerprofiles\&quot;&lt;/td&gt;   &lt;/tr&gt;  &lt;/table&gt;  &lt;a href&#x3D;\&quot;https://test-server.brapi.org/brapi/v1/calls\&quot;&gt; test-server.brapi.org/brapi/v1/calls&lt;/a&gt; # noqa: E501

    :param datatype: The data format supported by the call. Example: &#x60;json&#x60;
    :type datatype: str
    :param pageSize: The size of the pages to be returned. Default is &#x60;1000&#x60;.
    :type pageSize: int
    :param page: Which result page is requested. The page indexing starts at 0 (the first page is &#39;page&#39;&#x3D; 0). Default is &#x60;0&#x60;.
    :type page: int

    :rtype: CallsResponse
    """

    return CallsController_impl.calls_get(datatype=None, pageSize=None, page=None)

