# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.marker_response import MarkerResponse  # noqa: E501
from bety_brapi.models.markers_response2 import MarkersResponse2  # noqa: E501
from bety_brapi.models.markers_search_request import MarkersSearchRequest  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestMarkersController(BaseTestCase):
    """MarkersController integration test stubs"""

    def test_markers_get(self):
        """Test case for markers_get

        Markers Search (/markers)
        """
        query_string = [('name', 'name_example'),
                        ('matchMethod', 'matchMethod_example'),
                        ('include', 'include_example'),
                        ('type', 'type_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/markers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_markers_marker_db_id_get(self):
        """Test case for markers_marker_db_id_get

        Marker Details by id
        """
        response = self.client.open(
            '/brapi/v1/markers/{markerDbId}'.format(markerDbId='markerDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_markers_search_get(self):
        """Test case for markers_search_get

        Markers Search (GET)
        """
        query_string = [('markerDbIds', 'markerDbIds_example'),
                        ('name', 'name_example'),
                        ('matchMethod', 'matchMethod_example'),
                        ('includeSynonyms', true),
                        ('type', 'type_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/markers-search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_markers_search_post(self):
        """Test case for markers_search_post

        Markers Search (POST)
        """
        markerDbIds = MarkersSearchRequest()
        response = self.client.open(
            '/brapi/v1/markers-search',
            method='POST',
            data=json.dumps(markerDbIds),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
