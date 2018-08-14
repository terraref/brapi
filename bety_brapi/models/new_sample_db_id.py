# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.metadata import Metadata  # noqa: F401,E501
from bety_brapi.models.new_sample_db_id_result import NewSampleDbIdResult  # noqa: F401,E501
from bety_brapi import util


class NewSampleDbId(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: Metadata=None, result: NewSampleDbIdResult=None):  # noqa: E501
        """NewSampleDbId - a model defined in Swagger

        :param metadata: The metadata of this NewSampleDbId.  # noqa: E501
        :type metadata: Metadata
        :param result: The result of this NewSampleDbId.  # noqa: E501
        :type result: NewSampleDbIdResult
        """
        self.swagger_types = {
            'metadata': Metadata,
            'result': NewSampleDbIdResult
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'result': 'result'
        }

        self._metadata = metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'NewSampleDbId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The newSampleDbId of this NewSampleDbId.  # noqa: E501
        :rtype: NewSampleDbId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this NewSampleDbId.

        Metadata of this response  # noqa: E501

        :return: The metadata of this NewSampleDbId.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this NewSampleDbId.

        Metadata of this response  # noqa: E501

        :param metadata: The metadata of this NewSampleDbId.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def result(self) -> NewSampleDbIdResult:
        """Gets the result of this NewSampleDbId.


        :return: The result of this NewSampleDbId.
        :rtype: NewSampleDbIdResult
        """
        return self._result

    @result.setter
    def result(self, result: NewSampleDbIdResult):
        """Sets the result of this NewSampleDbId.


        :param result: The result of this NewSampleDbId.
        :type result: NewSampleDbIdResult
        """

        self._result = result
