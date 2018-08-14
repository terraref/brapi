# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.germplasm_response import GermplasmResponse  # noqa: E501
from bety_brapi.models.germplasm_search_request import GermplasmSearchRequest  # noqa: E501
from bety_brapi.models.observation_units_response import ObservationUnitsResponse  # noqa: E501
from bety_brapi.models.observation_units_table_response1 import ObservationUnitsTableResponse1  # noqa: E501
from bety_brapi.models.phenotypes_search_request import PhenotypesSearchRequest  # noqa: E501
from bety_brapi.models.programs_response import ProgramsResponse  # noqa: E501
from bety_brapi.models.programs_search_request import ProgramsSearchRequest  # noqa: E501
from bety_brapi.models.sample_search_request import SampleSearchRequest  # noqa: E501
from bety_brapi.models.samples_response import SamplesResponse  # noqa: E501
from bety_brapi.models.studies_response import StudiesResponse  # noqa: E501
from bety_brapi.models.study_search_request import StudySearchRequest  # noqa: E501
from bety_brapi.models.vendor_plate_search_request import VendorPlateSearchRequest  # noqa: E501
from bety_brapi.models.vendor_plates_response import VendorPlatesResponse  # noqa: E501
from bety_brapi.models.vendor_plates_response1 import VendorPlatesResponse1  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestSearchServicesController(BaseTestCase):
    """SearchServicesController integration test stubs"""

    def test_germplasm_search_get(self):
        """Test case for germplasm_search_get

        Germplasm search through GET
        """
        query_string = [('germplasmPUI', 'germplasmPUI_example'),
                        ('germplasmDbId', 'germplasmDbId_example'),
                        ('germplasmName', 'germplasmName_example'),
                        ('commonCropName', 'commonCropName_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/germplasm-search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_germplasm_search_post(self):
        """Test case for germplasm_search_post

        Germplasm search through POST
        """
        body = GermplasmSearchRequest()
        response = self.client.open(
            '/brapi/v1/germplasm-search',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
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

    def test_programs_search_post(self):
        """Test case for programs_search_post

        Search Programs
        """
        body = ProgramsSearchRequest()
        response = self.client.open(
            '/brapi/v1/programs-search',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_samples_search_get(self):
        """Test case for samples_search_get

        Get Sample Search
        """
        query_string = [('sampleDbId', 'sampleDbId_example'),
                        ('observationUnitDbId', 'observationUnitDbId_example'),
                        ('plateDbId', 'plateDbId_example'),
                        ('germplasmDbId', 'germplasmDbId_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/samples-search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_samples_search_post(self):
        """Test case for samples_search_post

        Post Sample Search
        """
        sampleSearch = SampleSearchRequest()
        response = self.client.open(
            '/brapi/v1/samples-search',
            method='POST',
            data=json.dumps(sampleSearch),
            content_type='application/json')
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


if __name__ == '__main__':
    import unittest
    unittest.main()
