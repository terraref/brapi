import connexion
import six
#from bety_brapi.controllers_impl import AuthenticationController_impl

from bety_brapi.models.body import Body  # noqa: E501
from bety_brapi.models.body1 import Body1  # noqa: E501
from bety_brapi import util


def login_post(body=None):  # noqa: E501
    """Login

    Implemented by: Tripal Brapi module, Cassavabase, Germinate, BMS  Used by: Flapjack, BMS  Response data types Exception: the result is not embeded in a \&quot;result\&quot; structure in order to be (one day) OAuth2 compliant. It&#39;s also why the anwser mixes snake_case and camelCase. For login, returns a hash with the user name and the token as the value. A metadata key is also present (but usually set to null, unless an error condition occurs).  For logout, returns an empty resource. A token to remove could be provided (amdin interface) but it is not required. By default, current user token will be removed.  |Variable|Datatype|Description|Required|   |------|------|------|:-----:| | userDisplayName| string| the display name of the user | Y | | access_token | string | the access token for the session | Y | | expires_in | integer | The lifetime in seconds of the access token | Y |  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501

#    return AuthenticationController_impl.login_post(body=None)
    return "Not implemented"


def logout_delete(body=None):  # noqa: E501
    """Logout

    Implemented by: Tripal Brapi module, Cassavabase, Germinate, BMS  Used by: Flapjack, BMS  For logout, returns an empty resource. A token to remove could be provided (amdin interface) but it is not required. By default, current user token will be removed. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501

#    return AuthenticationController_impl.logout_delete(body=None)
    return "Not implemented"

