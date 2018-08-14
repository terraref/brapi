# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.metadata import Metadata  # noqa: F401,E501
from bety_brapi.models.samples_response_result import SamplesResponseResult  # noqa: F401,E501
from bety_brapi import util


class SamplesResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: Metadata=None, result: SamplesResponseResult=None):  # noqa: E501
        """SamplesResponse - a model defined in Swagger

        :param metadata: The metadata of this SamplesResponse.  # noqa: E501
        :type metadata: Metadata
        :param result: The result of this SamplesResponse.  # noqa: E501
        :type result: SamplesResponseResult
        """
        self.swagger_types = {
            'metadata': Metadata,
            'result': SamplesResponseResult
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'result': 'result'
        }

        self._metadata = metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'SamplesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The samplesResponse of this SamplesResponse.  # noqa: E501
        :rtype: SamplesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this SamplesResponse.


        :return: The metadata of this SamplesResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this SamplesResponse.


        :param metadata: The metadata of this SamplesResponse.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def result(self) -> SamplesResponseResult:
        """Gets the result of this SamplesResponse.


        :return: The result of this SamplesResponse.
        :rtype: SamplesResponseResult
        """
        return self._result

    @result.setter
    def result(self, result: SamplesResponseResult):
        """Sets the result of this SamplesResponse.


        :param result: The result of this SamplesResponse.
        :type result: SamplesResponseResult
        """

        self._result = result
