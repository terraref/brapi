# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.genome_maps_response import GenomeMapsResponse  # noqa: E501
from bety_brapi.models.map_details_response import MapDetailsResponse  # noqa: E501
from bety_brapi.models.markers_response import MarkersResponse  # noqa: E501
from bety_brapi.models.markers_response1 import MarkersResponse1  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestGenomeMapsController(BaseTestCase):
    """GenomeMapsController integration test stubs"""

    def test_maps_get(self):
        """Test case for maps_get

        Get list of maps
        """
        query_string = [('species', 'species_example'),
                        ('type', 'type_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/maps',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_maps_map_db_id_get(self):
        """Test case for maps_map_db_id_get

        Get map details
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/maps/{mapDbId}'.format(mapDbId='mapDbId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_maps_map_db_id_positions_get(self):
        """Test case for maps_map_db_id_positions_get

        Get map data
        """
        query_string = [('linkageGroupId', 'linkageGroupId_example'),
                        ('linkageGroupName', 'linkageGroupName_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/maps/{mapDbId}/positions'.format(mapDbId='mapDbId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_maps_map_db_id_positions_linkage_group_name_get(self):
        """Test case for maps_map_db_id_positions_linkage_group_name_get

        Get map data by range on linkageGroup
        """
        query_string = [('min', 56),
                        ('max', 56),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/maps/{mapDbId}/positions/{linkageGroupName}'.format(mapDbId='mapDbId_example', linkageGroupName='linkageGroupName_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
