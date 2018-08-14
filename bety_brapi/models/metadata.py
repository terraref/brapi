# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.metadata_pagination import MetadataPagination  # noqa: F401,E501
from bety_brapi.models.status import Status  # noqa: F401,E501
from bety_brapi import util


class Metadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, datafiles: List[str]=None, pagination: MetadataPagination=None, status: List[Status]=None):  # noqa: E501
        """Metadata - a model defined in Swagger

        :param datafiles: The datafiles of this Metadata.  # noqa: E501
        :type datafiles: List[str]
        :param pagination: The pagination of this Metadata.  # noqa: E501
        :type pagination: MetadataPagination
        :param status: The status of this Metadata.  # noqa: E501
        :type status: List[Status]
        """
        self.swagger_types = {
            'datafiles': List[str],
            'pagination': MetadataPagination,
            'status': List[Status]
        }

        self.attribute_map = {
            'datafiles': 'datafiles',
            'pagination': 'pagination',
            'status': 'status'
        }

        self._datafiles = datafiles
        self._pagination = pagination
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Metadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The metadata of this Metadata.  # noqa: E501
        :rtype: Metadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datafiles(self) -> List[str]:
        """Gets the datafiles of this Metadata.

        The datafiles key contains a list of file paths, which can be relative or complete URLs. These files contain additional information related to the returned object and can be retrieved by a subsequent call. The empty list should be returned if no additional data files are present.  # noqa: E501

        :return: The datafiles of this Metadata.
        :rtype: List[str]
        """
        return self._datafiles

    @datafiles.setter
    def datafiles(self, datafiles: List[str]):
        """Sets the datafiles of this Metadata.

        The datafiles key contains a list of file paths, which can be relative or complete URLs. These files contain additional information related to the returned object and can be retrieved by a subsequent call. The empty list should be returned if no additional data files are present.  # noqa: E501

        :param datafiles: The datafiles of this Metadata.
        :type datafiles: List[str]
        """

        self._datafiles = datafiles

    @property
    def pagination(self) -> MetadataPagination:
        """Gets the pagination of this Metadata.


        :return: The pagination of this Metadata.
        :rtype: MetadataPagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination: MetadataPagination):
        """Sets the pagination of this Metadata.


        :param pagination: The pagination of this Metadata.
        :type pagination: MetadataPagination
        """

        self._pagination = pagination

    @property
    def status(self) -> List[Status]:
        """Gets the status of this Metadata.

        The status field contains a list of informational status messages from the server. If no status is reported, an empty list should be returned. See Error Reporting for more information.  # noqa: E501

        :return: The status of this Metadata.
        :rtype: List[Status]
        """
        return self._status

    @status.setter
    def status(self, status: List[Status]):
        """Sets the status of this Metadata.

        The status field contains a list of informational status messages from the server. If no status is reported, an empty list should be returned. See Error Reporting for more information.  # noqa: E501

        :param status: The status of this Metadata.
        :type status: List[Status]
        """

        self._status = status
