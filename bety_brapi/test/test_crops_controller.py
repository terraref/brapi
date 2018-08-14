# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.common_crop_names_response import CommonCropNamesResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestCropsController(BaseTestCase):
    """CropsController integration test stubs"""

    def test_common_crop_names_get(self):
        """Test case for common_crop_names_get

        List supported crops
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/commonCropNames',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crops_get(self):
        """Test case for crops_get

        List supported crops
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/crops',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
