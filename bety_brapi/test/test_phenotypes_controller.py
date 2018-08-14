# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.new_observation_db_ids_response import NewObservationDbIdsResponse  # noqa: E501
from bety_brapi.models.observation_units_response import ObservationUnitsResponse  # noqa: E501
from bety_brapi.models.observation_units_table_response1 import ObservationUnitsTableResponse1  # noqa: E501
from bety_brapi.models.phenotypes_request import PhenotypesRequest  # noqa: E501
from bety_brapi.models.phenotypes_search_request import PhenotypesSearchRequest  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestPhenotypesController(BaseTestCase):
    """PhenotypesController integration test stubs"""

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

    def test_phenotypes_search_csv_post(self):
        """Test case for phenotypes_search_csv_post

        Phenotype Search CSV
        """
        body = PhenotypesSearchRequest()
        response = self.client.open(
            '/brapi/v1/phenotypes-search/csv',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phenotypes_search_get(self):
        """Test case for phenotypes_search_get

        Phenotype Search
        """
        query_string = [('germplasmDbId', 'germplasmDbId_example'),
                        ('observationVariableDbId', 'observationVariableDbId_example'),
                        ('studyDbId', 'studyDbId_example'),
                        ('locationDbId', 'locationDbId_example'),
                        ('trialDbId', 'trialDbId_example'),
                        ('programDbId', 'programDbId_example'),
                        ('seasonDbId', 'seasonDbId_example'),
                        ('observationLevel', 'observationLevel_example'),
                        ('observationTimeStampRangeStart', '2013-10-20T19:20:30+01:00'),
                        ('observationTimeStampRangeEnd', '2013-10-20T19:20:30+01:00'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/phenotypes-search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phenotypes_search_post(self):
        """Test case for phenotypes_search_post

        Phenotype Search
        """
        body = PhenotypesSearchRequest()
        response = self.client.open(
            '/brapi/v1/phenotypes-search',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phenotypes_search_table_post(self):
        """Test case for phenotypes_search_table_post

        Phenotype Search Table
        """
        body = PhenotypesSearchRequest()
        response = self.client.open(
            '/brapi/v1/phenotypes-search/table',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phenotypes_search_tsv_post(self):
        """Test case for phenotypes_search_tsv_post

        Phenotype Search TSV
        """
        body = PhenotypesSearchRequest()
        response = self.client.open(
            '/brapi/v1/phenotypes-search/tsv',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
