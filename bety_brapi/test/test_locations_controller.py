# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.location_response import LocationResponse  # noqa: E501
from bety_brapi.models.locations_response import LocationsResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestLocationsController(BaseTestCase):
    """LocationsController integration test stubs"""

    def test_locations_get(self):
        """Test case for locations_get

        
        """
        query_string = [('locationType', 'locationType_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/locations',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_locations_location_db_id_get(self):
        """Test case for locations_location_db_id_get

        The internal DB id for a location
        """
        response = self.client.open(
            '/brapi/v1/locations/{locationDbId}'.format(locationDbId='locationDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
