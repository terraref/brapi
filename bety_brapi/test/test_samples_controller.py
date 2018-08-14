# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.new_sample_db_id import NewSampleDbId  # noqa: E501
from bety_brapi.models.sample import Sample  # noqa: E501
from bety_brapi.models.sample_response import SampleResponse  # noqa: E501
from bety_brapi.models.sample_search_request import SampleSearchRequest  # noqa: E501
from bety_brapi.models.samples_response import SamplesResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestSamplesController(BaseTestCase):
    """SamplesController integration test stubs"""

    def test_samples_put(self):
        """Test case for samples_put

        Add a sample
        """
        sample = Sample()
        response = self.client.open(
            '/brapi/v1/samples',
            method='PUT',
            data=json.dumps(sample),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_samples_sample_db_id_get(self):
        """Test case for samples_sample_db_id_get

        Get Sample
        """
        response = self.client.open(
            '/brapi/v1/samples/{sampleDbId}'.format(sampleDbId='sampleDbId_example'),
            method='GET')
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


if __name__ == '__main__':
    import unittest
    unittest.main()
