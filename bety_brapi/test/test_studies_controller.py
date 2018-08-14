# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.germplasm_summary_list_response import GermplasmSummaryListResponse  # noqa: E501
from bety_brapi.models.new_observation_db_ids_response import NewObservationDbIdsResponse  # noqa: E501
from bety_brapi.models.new_observation_unit_db_ids_response import NewObservationUnitDbIdsResponse  # noqa: E501
from bety_brapi.models.new_observation_unit_request import NewObservationUnitRequest  # noqa: E501
from bety_brapi.models.new_observations_request import NewObservationsRequest  # noqa: E501
from bety_brapi.models.new_observations_request_wrapper_deprecated import NewObservationsRequestWrapperDeprecated  # noqa: E501
from bety_brapi.models.new_observations_table_request import NewObservationsTableRequest  # noqa: E501
from bety_brapi.models.observation_unit_positions_response import ObservationUnitPositionsResponse  # noqa: E501
from bety_brapi.models.observation_units_response1 import ObservationUnitsResponse1  # noqa: E501
from bety_brapi.models.observations_response import ObservationsResponse  # noqa: E501
from bety_brapi.models.seasons_response import SeasonsResponse  # noqa: E501
from bety_brapi.models.studies_response import StudiesResponse  # noqa: E501
from bety_brapi.models.study_layout_request import StudyLayoutRequest  # noqa: E501
from bety_brapi.models.study_observation_variables_response import StudyObservationVariablesResponse  # noqa: E501
from bety_brapi.models.study_response import StudyResponse  # noqa: E501
from bety_brapi.models.study_search_request import StudySearchRequest  # noqa: E501
from bety_brapi.models.study_types_response import StudyTypesResponse  # noqa: E501
from bety_brapi.models.studyobservations_table_response import StudyobservationsTableResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestStudiesController(BaseTestCase):
    """StudiesController integration test stubs"""

    def test_seasons_get(self):
        """Test case for seasons_get

        List seasons or years
        """
        query_string = [('year', 'year_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/seasons',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_search_get(self):
        """Test case for studies_search_get

        Search Studies (GET)
        """
        query_string = [('studyType', 'studyType_example'),
                        ('programDbId', 'programDbId_example'),
                        ('locationDbId', 'locationDbId_example'),
                        ('seasonDbId', 'seasonDbId_example'),
                        ('trialDbId', 'trialDbId_example'),
                        ('studyDbId', 'studyDbId_example'),
                        ('germplasmDbIds', 'germplasmDbIds_example'),
                        ('observationVariableDbIds', 'observationVariableDbIds_example'),
                        ('pageSize', 56),
                        ('page', 56),
                        ('active', true),
                        ('sortBy', 'sortBy_example'),
                        ('sortOrder', 'sortOrder_example')]
        response = self.client.open(
            '/brapi/v1/studies-search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_search_post(self):
        """Test case for studies_search_post

        Search Studies (GET)
        """
        studySearchRequest = StudySearchRequest()
        response = self.client.open(
            '/brapi/v1/studies-search',
            method='POST',
            data=json.dumps(studySearchRequest),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_germplasm_get(self):
        """Test case for studies_study_db_id_germplasm_get

        Study Germplasm Details
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/germplasm'.format(studyDbId='studyDbId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_get(self):
        """Test case for studies_study_db_id_get

        Retrieve study details
        """
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}'.format(studyDbId='studyDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_layout_get(self):
        """Test case for studies_study_db_id_layout_get

        Retrieve plot layout details
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/layout'.format(studyDbId='studyDbId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_studies_study_db_id_layout_put(self):
        """Test case for studies_study_db_id_layout_put

        Retrieve plot layout details
        """
        studyLayoutRequest = StudyLayoutRequest()
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/layout'.format(studyDbId='studyDbId_example'),
            method='PUT',
            data=json.dumps(studyLayoutRequest),
            content_type='application/json')
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

    def test_studies_study_db_id_observationvariables_get(self):
        """Test case for studies_study_db_id_observationvariables_get

        Get Observation Variables By Study
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/studies/{studyDbId}/observationvariables'.format(studyDbId='studyDbId_example'),
            method='GET',
            query_string=query_string)
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

    def test_studytypes_get(self):
        """Test case for studytypes_get

        List study types
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/studytypes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
