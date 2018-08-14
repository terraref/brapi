# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.map_details import MapDetails  # noqa: F401,E501
from bety_brapi.models.metadata import Metadata  # noqa: F401,E501
from bety_brapi import util


class MapDetailsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: Metadata=None, result: MapDetails=None):  # noqa: E501
        """MapDetailsResponse - a model defined in Swagger

        :param metadata: The metadata of this MapDetailsResponse.  # noqa: E501
        :type metadata: Metadata
        :param result: The result of this MapDetailsResponse.  # noqa: E501
        :type result: MapDetails
        """
        self.swagger_types = {
            'metadata': Metadata,
            'result': MapDetails
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'result': 'result'
        }

        self._metadata = metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'MapDetailsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The mapDetailsResponse of this MapDetailsResponse.  # noqa: E501
        :rtype: MapDetailsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this MapDetailsResponse.


        :return: The metadata of this MapDetailsResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this MapDetailsResponse.


        :param metadata: The metadata of this MapDetailsResponse.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def result(self) -> MapDetails:
        """Gets the result of this MapDetailsResponse.


        :return: The result of this MapDetailsResponse.
        :rtype: MapDetails
        """
        return self._result

    @result.setter
    def result(self, result: MapDetails):
        """Sets the result of this MapDetailsResponse.


        :param result: The result of this MapDetailsResponse.
        :type result: MapDetails
        """

        self._result = result
