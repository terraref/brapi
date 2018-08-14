# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.programs_response import ProgramsResponse  # noqa: E501
from bety_brapi.models.programs_search_request import ProgramsSearchRequest  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestProgramsController(BaseTestCase):
    """ProgramsController integration test stubs"""

    def test_programs_get(self):
        """Test case for programs_get

        List programs
        """
        query_string = [('programName', 'programName_example'),
                        ('abbreviation', 'abbreviation_example'),
                        ('pageSize', 56),
                        ('page', 56)]
        response = self.client.open(
            '/brapi/v1/programs',
            method='GET',
            query_string=query_string)
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


if __name__ == '__main__':
    import unittest
    unittest.main()
