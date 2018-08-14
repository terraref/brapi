# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class LinkageGroup(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, linkage_group_name: str=None, marker_count: int=None, max_position: int=None):  # noqa: E501
        """LinkageGroup - a model defined in Swagger

        :param linkage_group_name: The linkage_group_name of this LinkageGroup.  # noqa: E501
        :type linkage_group_name: str
        :param marker_count: The marker_count of this LinkageGroup.  # noqa: E501
        :type marker_count: int
        :param max_position: The max_position of this LinkageGroup.  # noqa: E501
        :type max_position: int
        """
        self.swagger_types = {
            'linkage_group_name': str,
            'marker_count': int,
            'max_position': int
        }

        self.attribute_map = {
            'linkage_group_name': 'linkageGroupName',
            'marker_count': 'markerCount',
            'max_position': 'maxPosition'
        }

        self._linkage_group_name = linkage_group_name
        self._marker_count = marker_count
        self._max_position = max_position

    @classmethod
    def from_dict(cls, dikt) -> 'LinkageGroup':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The linkageGroup of this LinkageGroup.  # noqa: E501
        :rtype: LinkageGroup
        """
        return util.deserialize_model(dikt, cls)

    @property
    def linkage_group_name(self) -> str:
        """Gets the linkage_group_name of this LinkageGroup.

        The Uniquely Identifiable name of this linkage group  # noqa: E501

        :return: The linkage_group_name of this LinkageGroup.
        :rtype: str
        """
        return self._linkage_group_name

    @linkage_group_name.setter
    def linkage_group_name(self, linkage_group_name: str):
        """Sets the linkage_group_name of this LinkageGroup.

        The Uniquely Identifiable name of this linkage group  # noqa: E501

        :param linkage_group_name: The linkage_group_name of this LinkageGroup.
        :type linkage_group_name: str
        """

        self._linkage_group_name = linkage_group_name

    @property
    def marker_count(self) -> int:
        """Gets the marker_count of this LinkageGroup.

        The number of markers associated with this linkage group  # noqa: E501

        :return: The marker_count of this LinkageGroup.
        :rtype: int
        """
        return self._marker_count

    @marker_count.setter
    def marker_count(self, marker_count: int):
        """Sets the marker_count of this LinkageGroup.

        The number of markers associated with this linkage group  # noqa: E501

        :param marker_count: The marker_count of this LinkageGroup.
        :type marker_count: int
        """

        self._marker_count = marker_count

    @property
    def max_position(self) -> int:
        """Gets the max_position of this LinkageGroup.

        The maximum position of a marker within this linkage group  # noqa: E501

        :return: The max_position of this LinkageGroup.
        :rtype: int
        """
        return self._max_position

    @max_position.setter
    def max_position(self, max_position: int):
        """Sets the max_position of this LinkageGroup.

        The maximum position of a marker within this linkage group  # noqa: E501

        :param max_position: The max_position of this LinkageGroup.
        :type max_position: int
        """

        self._max_position = max_position
