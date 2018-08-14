# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from bety_brapi.models.trial_response import TrialResponse  # noqa: E501
from bety_brapi.models.trials_response import TrialsResponse  # noqa: E501
from bety_brapi.test import BaseTestCase


class TestTrialsController(BaseTestCase):
    """TrialsController integration test stubs"""

    def test_trials_get(self):
        """Test case for trials_get

        List of trial summaries
        """
        query_string = [('programDbId', 'programDbId_example'),
                        ('locationDbId', 'locationDbId_example'),
                        ('pageSize', 56),
                        ('page', 56),
                        ('active', true),
                        ('sortBy', 'sortBy_example'),
                        ('sortOrder', 'sortOrder_example')]
        response = self.client.open(
            '/brapi/v1/trials',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_trials_trial_db_id_get(self):
        """Test case for trials_trial_db_id_get

        Get trial by Id
        """
        response = self.client.open(
            '/brapi/v1/trials/{trialDbId}'.format(trialDbId='trialDbId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
