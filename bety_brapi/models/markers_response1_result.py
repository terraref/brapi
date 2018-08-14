# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.marker_summary_linkage_group import MarkerSummaryLinkageGroup  # noqa: F401,E501
from bety_brapi import util


class MarkersResponse1Result(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, data: List[MarkerSummaryLinkageGroup]=None):  # noqa: E501
        """MarkersResponse1Result - a model defined in Swagger

        :param data: The data of this MarkersResponse1Result.  # noqa: E501
        :type data: List[MarkerSummaryLinkageGroup]
        """
        self.swagger_types = {
            'data': List[MarkerSummaryLinkageGroup]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'MarkersResponse1Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The markersResponse_1_result of this MarkersResponse1Result.  # noqa: E501
        :rtype: MarkersResponse1Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[MarkerSummaryLinkageGroup]:
        """Gets the data of this MarkersResponse1Result.


        :return: The data of this MarkersResponse1Result.
        :rtype: List[MarkerSummaryLinkageGroup]
        """
        return self._data

    @data.setter
    def data(self, data: List[MarkerSummaryLinkageGroup]):
        """Sets the data of this MarkersResponse1Result.


        :param data: The data of this MarkersResponse1Result.
        :type data: List[MarkerSummaryLinkageGroup]
        """

        self._data = data
