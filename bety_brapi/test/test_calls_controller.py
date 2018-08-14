# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.calls_response import CallsResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestCallsController(BaseTestCase):
    """CallsController integration test stubs"""

    def test_calls_get(self):
        """Test case for calls_get

        Call search
        """
        query_string = [('datatype', 'datatype_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/calls',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
