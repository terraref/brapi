# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.breeding_method import BreedingMethod  # noqa: F401,E501
from bety_brapi.models.metadata import Metadata  # noqa: F401,E501
from bety_brapi import util


class BreedingMethodResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: Metadata=None, result: BreedingMethod=None):  # noqa: E501
        """BreedingMethodResponse - a model defined in Swagger

        :param metadata: The metadata of this BreedingMethodResponse.  # noqa: E501
        :type metadata: Metadata
        :param result: The result of this BreedingMethodResponse.  # noqa: E501
        :type result: BreedingMethod
        """
        self.swagger_types = {
            'metadata': Metadata,
            'result': BreedingMethod
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'result': 'result'
        }

        self._metadata = metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'BreedingMethodResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The breedingMethodResponse of this BreedingMethodResponse.  # noqa: E501
        :rtype: BreedingMethodResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this BreedingMethodResponse.


        :return: The metadata of this BreedingMethodResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this BreedingMethodResponse.


        :param metadata: The metadata of this BreedingMethodResponse.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def result(self) -> BreedingMethod:
        """Gets the result of this BreedingMethodResponse.


        :return: The result of this BreedingMethodResponse.
        :rtype: BreedingMethod
        """
        return self._result

    @result.setter
    def result(self, result: BreedingMethod):
        """Sets the result of this BreedingMethodResponse.


        :param result: The result of this BreedingMethodResponse.
        :type result: BreedingMethod
        """

        self._result = result
