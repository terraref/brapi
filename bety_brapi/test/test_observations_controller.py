# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.new_observation_db_ids_response import NewObservationDbIdsResponse  # noqa: E501
from bety_brapi.models.new_observation_unit_db_ids_response import NewObservationUnitDbIdsResponse  # noqa: E501
from bety_brapi.models.new_observation_unit_request import NewObservationUnitRequest  # noqa: E501
from bety_brapi.models.new_observations_request import NewObservationsRequest  # noqa: E501
from bety_brapi.models.new_observations_request_wrapper_deprecated import NewObservationsRequestWrapperDeprecated  # noqa: E501
from bety_brapi.models.new_observations_table_request import NewObservationsTableRequest  # noqa: E501
from bety_brapi.models.observation_levels_response import ObservationLevelsResponse  # noqa: E501
from bety_brapi.models.observation_units_response1 import ObservationUnitsResponse1  # noqa: E501
from bety_brapi.models.observations_response import ObservationsResponse  # noqa: E501
from bety_brapi.models.phenotypes_request import PhenotypesRequest  # noqa: E501
from bety_brapi.models.studyobservations_table_response import StudyobservationsTableResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestObservationsController(BaseTestCase):
    """ObservationsController integration test stubs"""

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

    def test_observationlevels_get(self):
        """Test case for observationlevels_get

        Get Observation Levels
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/observationlevels',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phenotypes_post(self):
        """Test case for phenotypes_post

        Save Observation Unit Phenotypes
        """
        body = PhenotypesRequest()
        query_string = [('format', 'format_example')]
        response = self.client.open(
            '/brapi/v1/phenotypes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_observations_get(self):
        """Test case for studies_study_db_id_observations_get

        Get Observation Units by observation variable ids
        """
        query_string = [('observationVariableDbIds', 'observationVariableDbIds_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/observations'.format(studyDbId='studyDbId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_observations_put(self):
        """Test case for studies_study_db_id_observations_put

        Get Observation Units by observation variable ids
        """
        newObservations = NewObservationsRequest()
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/observations'.format(studyDbId='studyDbId_example'),
            method='PUT',
            data=json.dumps(newObservations),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_observationunits_get(self):
        """Test case for studies_study_db_id_observationunits_get

        Get all observation units
        """
        query_string = [('observationLevel', 'observationLevel_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/observationunits'.format(studyDbId='studyDbId_example'),
            method='GET',
            query_string=query_string)
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

    def test_studies_study_db_id_observationunits_put(self):
        """Test case for studies_study_db_id_observationunits_put

        Save Observation Unit Phenotypes
        """
        newObservationUnitRequest = [NewObservationUnitRequest()]
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/observationunits'.format(studyDbId='studyDbId_example'),
            method='PUT',
            data=json.dumps(newObservationUnitRequest),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_observationunits_zip_post(self):
        """Test case for studies_study_db_id_observationunits_zip_post

        Use this call for uploading new Observations as a Batched Zip File to a system.
        """
        zipRequest = Binary()
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/observationunits/zip'.format(studyDbId='studyDbId_example'),
            method='POST',
            data=json.dumps(zipRequest),
            content_type='application/zip')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_table_get(self):
        """Test case for studies_study_db_id_table_get

        Retrieve study Observation Units as table
        """
        query_string = [('format', 'format_example')]
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/table'.format(studyDbId='studyDbId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_table_post(self):
        """Test case for studies_study_db_id_table_post

        Save study Observation Units as table
        """
        newObservationsTableRequest = NewObservationsTableRequest()
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/table'.format(studyDbId='studyDbId_example'),
            method='POST',
            data=json.dumps(newObservationsTableRequest),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
