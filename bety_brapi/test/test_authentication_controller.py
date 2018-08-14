# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.body import Body  # noqa: E501
from bety_brapi.models.body1 import Body1  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestAuthenticationController(BaseTestCase):
    """AuthenticationController integration test stubs"""

    def test_login_post(self):
        """Test case for login_post

        Login
        """
        body = Body()
        response = self.client.open(
            '/brapi/v1/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_delete(self):
        """Test case for logout_delete

        Logout
        """
        body = Body1()
        response = self.client.open(
            '/brapi/v1/logout',
            method='DELETE',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
