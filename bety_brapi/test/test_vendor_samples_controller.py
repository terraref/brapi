# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.vendor_plate_request import VendorPlateRequest  # noqa: E501
from bety_brapi.models.vendor_plate_response import VendorPlateResponse  # noqa: E501
from bety_brapi.models.vendor_plate_search_request import VendorPlateSearchRequest  # noqa: E501
from bety_brapi.models.vendor_plates_response import VendorPlatesResponse  # noqa: E501
from bety_brapi.models.vendor_plates_response1 import VendorPlatesResponse1  # noqa: E501
from bety_brapi.models.vendor_specification_response import VendorSpecificationResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestVendorSamplesController(BaseTestCase):
    """VendorSamplesController integration test stubs"""

    def test_vendor_plates_post(self):
        """Test case for vendor_plates_post

        Register plates
        """
        body = VendorPlateRequest()
        response = self.client.open(
            '/brapi/v1/vendor/plates',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vendor_plates_search_get(self):
        """Test case for vendor_plates_search_get

        Search for plates
        """
        query_string = [('vendorProjectDbId', 'vendorProjectDbId_example'),
                        ('vendorPlateDbId', 'vendorPlateDbId_example'),
                        ('clientPlateDbId', 'clientPlateDbId_example'),
                        ('sampleInfo', true),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/vendor/plates-search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vendor_plates_search_post(self):
        """Test case for vendor_plates_search_post

        Search for plates
        """
        body = VendorPlateSearchRequest()
        response = self.client.open(
            '/brapi/v1/vendor/plates-search',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vendor_plates_vendor_plate_db_id_get(self):
        """Test case for vendor_plates_vendor_plate_db_id_get

        Plate Details by vendorPlateId
        """
        response = self.client.open(
            '/brapi/v1/vendor/plates/{vendorPlateDbId}'.format(vendorPlateDbId='vendorPlateDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vendor_specifications_get(self):
        """Test case for vendor_specifications_get

        Vendor specification
        """
        response = self.client.open(
            '/brapi/v1/vendor/specifications',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
