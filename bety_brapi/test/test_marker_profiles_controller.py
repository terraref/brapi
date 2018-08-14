# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.allele_matrix_details_response import AlleleMatrixDetailsResponse  # noqa: E501
from bety_brapi.models.allele_matrix_search_request import AlleleMatrixSearchRequest  # noqa: E501
from bety_brapi.models.allele_matrix_values_response import AlleleMatrixValuesResponse  # noqa: E501
from bety_brapi.models.marker_profile_descriptions_response import MarkerProfileDescriptionsResponse  # noqa: E501
from bety_brapi.models.marker_profiles_response import MarkerProfilesResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestMarkerProfilesController(BaseTestCase):
    """MarkerProfilesController integration test stubs"""

    def test_allelematrices_get(self):
        """Test case for allelematrices_get

        Matrices through GET
        """
        query_string = [('studyDbId', 'studyDbId_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/allelematrices',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_allelematrices_search_get(self):
        """Test case for allelematrices_search_get

        Scores through GET
        """
        query_string = [('markerprofileDbId', 'markerprofileDbId_example'),
                        ('markerDbId', 'markerDbId_example'),
                        ('matrixDbId', 'matrixDbId_example'),
                        ('format', 'format_example'),
                        ('expandHomozygotes', true),
                        ('unknownString', 'unknownString_example'),
                        ('sepPhased', 'sepPhased_example'),
                        ('sepUnphased', 'sepUnphased_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/allelematrices-search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_allelematrices_search_post(self):
        """Test case for allelematrices_search_post

        Scores through POST
        """
        markerprofileDbId = AlleleMatrixSearchRequest()
        response = self.client.open(
            '/brapi/v1/allelematrices-search',
            method='POST',
            data=json.dumps(markerprofileDbId),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_allelematrix_search_get(self):
        """Test case for allelematrix_search_get

        Scores through GET
        """
        query_string = [('markerprofileDbId', 'markerprofileDbId_example'),
                        ('markerDbId', 'markerDbId_example'),
                        ('matrixDbId', 'matrixDbId_example'),
                        ('format', 'format_example'),
                        ('expandHomozygotes', true),
                        ('unknownString', 'unknownString_example'),
                        ('sepPhased', 'sepPhased_example'),
                        ('sepUnphased', 'sepUnphased_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/allelematrix-search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_allelematrix_search_post(self):
        """Test case for allelematrix_search_post

        Scores through POST
        """
        markerprofileDbId = AlleleMatrixSearchRequest()
        response = self.client.open(
            '/brapi/v1/allelematrix-search',
            method='POST',
            data=json.dumps(markerprofileDbId),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_markerprofiles_get(self):
        """Test case for markerprofiles_get

        Retrieve Markerprofile Ids
        """
        query_string = [('germplasmDbId', 'germplasmDbId_example'),
                        ('studyDbId', 'studyDbId_example'),
                        ('sampleDbId', 'sampleDbId_example'),
                        ('extractDbId', 'extractDbId_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/markerprofiles',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_markerprofiles_markerprofile_db_id_get(self):
        """Test case for markerprofiles_markerprofile_db_id_get

        Alleles By Markerprofile Id
        """
        query_string = [('expandHomozygotes', true),
                        ('unknownString', 'unknownString_example'),
                        ('sepPhased', 'sepPhased_example'),
                        ('sepUnphased', 'sepUnphased_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/markerprofiles/{markerprofileDbId}'.format(markerprofileDbId='markerprofileDbId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
