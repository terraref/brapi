# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.germplasm_attribute_categories_response import GermplasmAttributeCategoriesResponse  # noqa: E501
from bety_brapi.models.germplasm_attribute_defs_response import GermplasmAttributeDefsResponse  # noqa: E501
from bety_brapi.models.germplasm_attribute_list_response import GermplasmAttributeListResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestGermplasmAttributesController(BaseTestCase):
    """GermplasmAttributesController integration test stubs"""

    def test_attributes_categories_get(self):
        """Test case for attributes_categories_get

        Germplasm attribute categories
        """
        query_string = [('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/attributes/categories',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_attributes_get(self):
        """Test case for attributes_get

        Attributes by attributeCategoryDbId
        """
        query_string = [('attributeCategoryDbId', 'attributeCategoryDbId_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/attributes',
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


if __name__ == '__main__':
    import unittest
    unittest.main()
