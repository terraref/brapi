# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.breeding_method_response import BreedingMethodResponse  # noqa: E501
from bety_brapi.models.breeding_methods_response import BreedingMethodsResponse  # noqa: E501
from bety_brapi.models.germplasm_attribute_list_response import GermplasmAttributeListResponse  # noqa: E501
from bety_brapi.models.germplasm_markerprofiles_list_response import GermplasmMarkerprofilesListResponse  # noqa: E501
from bety_brapi.models.germplasm_response import GermplasmResponse  # noqa: E501
from bety_brapi.models.germplasm_response1 import GermplasmResponse1  # noqa: E501
from bety_brapi.models.germplasm_search_request import GermplasmSearchRequest  # noqa: E501
from bety_brapi.models.germplasm_summary_list_response import GermplasmSummaryListResponse  # noqa: E501
from bety_brapi.models.pedigree_response import PedigreeResponse  # noqa: E501
from bety_brapi.models.progeny_response import ProgenyResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestGermplasmController(BaseTestCase):
    """GermplasmController integration test stubs"""

    def test_breedingmethods_breeding_method_db_id_get(self):
        """Test case for breedingmethods_breeding_method_db_id_get

        GET specific breeding method details
        """
        response = self.client.open(
            '/brapi/v1/breedingmethods/{breedingMethodDbId}'.format(breedingMethodDbId='breedingMethodDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_breedingmethods_get(self):
        """Test case for breedingmethods_get

        GET List of Breeding Methods
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/breedingmethods',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_germplasm_germplasm_db_id_attributes_get(self):
        """Test case for germplasm_germplasm_db_id_attributes_get

        Germplasm attribute values
        """
        query_string = [('attributeDbIds', 'attributeDbIds_example'),
                        ('attributeList', 'attributeList_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/germplasm/{germplasmDbId}/attributes'.format(germplasmDbId='germplasmDbId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_germplasm_germplasm_db_id_get(self):
        """Test case for germplasm_germplasm_db_id_get

        Germplasm search by germplasmDbId
        """
        response = self.client.open(
            '/brapi/v1/germplasm/{germplasmDbId}'.format(germplasmDbId='germplasmDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_germplasm_germplasm_db_id_markerprofiles_get(self):
        """Test case for germplasm_germplasm_db_id_markerprofiles_get

        Markerprofiles by germplasmDbId
        """
        response = self.client.open(
            '/brapi/v1/germplasm/{germplasmDbId}/markerprofiles'.format(germplasmDbId='germplasmDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_germplasm_germplasm_db_id_pedigree_get(self):
        """Test case for germplasm_germplasm_db_id_pedigree_get

        Germplasm pedigree by id
        """
        query_string = [('notation', 'notation_example'),
                        ('includeSiblings', true)]
        response = self.client.open(
            '/brapi/v1/germplasm/{germplasmDbId}/pedigree'.format(germplasmDbId='germplasmDbId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_germplasm_germplasm_db_id_progeny_get(self):
        """Test case for germplasm_germplasm_db_id_progeny_get

        Germplasm pedigree by id
        """
        response = self.client.open(
            '/brapi/v1/germplasm/{germplasmDbId}/progeny'.format(germplasmDbId='germplasmDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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


if __name__ == '__main__':
    import unittest
    unittest.main()
