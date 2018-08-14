# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.data_types_response import DataTypesResponse  # noqa: E501
from bety_brapi.models.observation_variable_response import ObservationVariableResponse  # noqa: E501
from bety_brapi.models.observation_variable_search_request import ObservationVariableSearchRequest  # noqa: E501
from bety_brapi.models.observation_variables_response import ObservationVariablesResponse  # noqa: E501
from bety_brapi.models.ontologies_response import OntologiesResponse  # noqa: E501
from bety_brapi.models.study_observation_variables_response import StudyObservationVariablesResponse  # noqa: E501
from bety_brapi.models.trait_response import TraitResponse  # noqa: E501
from bety_brapi.models.traits_response import TraitsResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestObservationVariablesController(BaseTestCase):
    """ObservationVariablesController integration test stubs"""

    def test_ontologies_get(self):
        """Test case for ontologies_get

        Variable ontology list
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/ontologies',
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

    def test_traits_get(self):
        """Test case for traits_get

        List all traits
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/traits',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_traits_trait_db_id_get(self):
        """Test case for traits_trait_db_id_get

        Retrieve trait details by id
        """
        response = self.client.open(
            '/brapi/v1/traits/{traitDbId}'.format(traitDbId='traitDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_variables_datatypes_get(self):
        """Test case for variables_datatypes_get

        Variable data type list
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/variables/datatypes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_variables_get(self):
        """Test case for variables_get

        Variable list
        """
        query_string = [('pageSize', 56),
                        ('page', 56),
                        ('traitClass', 'traitClass_example')]
        response = self.client.open(
            '/brapi/v1/variables',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_variables_observation_variable_db_id_get(self):
        """Test case for variables_observation_variable_db_id_get

        Variable details by id
        """
        response = self.client.open(
            '/brapi/v1/variables/{observationVariableDbId}'.format(observationVariableDbId='observationVariableDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_variables_search_post(self):
        """Test case for variables_search_post

        Variable search
        """
        body = ObservationVariableSearchRequest()
        response = self.client.open(
            '/brapi/v1/variables-search',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
