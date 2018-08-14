# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.metadata import Metadata  # noqa: F401,E501
from bety_brapi.models.ontologies_response_result import OntologiesResponseResult  # noqa: F401,E501
from bety_brapi import util


class OntologiesResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: Metadata=None, result: OntologiesResponseResult=None):  # noqa: E501
        """OntologiesResponse - a model defined in Swagger

        :param metadata: The metadata of this OntologiesResponse.  # noqa: E501
        :type metadata: Metadata
        :param result: The result of this OntologiesResponse.  # noqa: E501
        :type result: OntologiesResponseResult
        """
        self.swagger_types = {
            'metadata': Metadata,
            'result': OntologiesResponseResult
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'result': 'result'
        }

        self._metadata = metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'OntologiesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ontologiesResponse of this OntologiesResponse.  # noqa: E501
        :rtype: OntologiesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this OntologiesResponse.


        :return: The metadata of this OntologiesResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this OntologiesResponse.


        :param metadata: The metadata of this OntologiesResponse.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def result(self) -> OntologiesResponseResult:
        """Gets the result of this OntologiesResponse.


        :return: The result of this OntologiesResponse.
        :rtype: OntologiesResponseResult
        """
        return self._result

    @result.setter
    def result(self, result: OntologiesResponseResult):
        """Sets the result of this OntologiesResponse.


        :param result: The result of this OntologiesResponse.
        :type result: OntologiesResponseResult
        """

        self._result = result
