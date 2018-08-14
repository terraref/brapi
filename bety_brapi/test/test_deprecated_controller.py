# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.allele_matrix_search_request import AlleleMatrixSearchRequest  # noqa: E501
from bety_brapi.models.allele_matrix_values_response import AlleleMatrixValuesResponse  # noqa: E501
from bety_brapi.models.body import Body  # noqa: E501
from bety_brapi.models.body1 import Body1  # noqa: E501
from bety_brapi.models.common_crop_names_response import CommonCropNamesResponse  # noqa: E501
from bety_brapi.models.markers_response2 import MarkersResponse2  # noqa: E501
from bety_brapi.models.new_observations_request_wrapper_deprecated import NewObservationsRequestWrapperDeprecated  # noqa: E501
from bety_brapi.models.observation_levels_response import ObservationLevelsResponse  # noqa: E501
from bety_brapi.models.study_observation_variables_response import StudyObservationVariablesResponse  # noqa: E501
from bety_brapi.models.study_types_response import StudyTypesResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestDeprecatedController(BaseTestCase):
    """DeprecatedController integration test stubs"""

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

    def test_observation_levels_get(self):
        """Test case for observation_levels_get

        <strong>Deprecated</strong> List observation levels
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/observationLevels',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_observation_variables_get(self):
        """Test case for studies_study_db_id_observation_variables_get

        <strong>Deprecated</strong> Retrieve study observation variables
        """
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/observationVariables'.format(studyDbId='studyDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_observationunits_post(self):
        """Test case for studies_study_db_id_observationunits_post

        <strong>Deprecated</strong> Save Observation Unit Phenotypes
        """
        body = NewObservationsRequestWrapperDeprecated()
        query_string = [('format', 'format_example')]
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/observationunits'.format(studyDbId='studyDbId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_study_types_get(self):
        """Test case for study_types_get

        <strong>Deprecated</strong> List study types
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/studyTypes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
