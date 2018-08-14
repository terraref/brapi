# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.vendor_plate import VendorPlate  # noqa: F401,E501
from bety_brapi import util


class VendorPlatesResponse1Result(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, data: List[VendorPlate]=None):  # noqa: E501
        """VendorPlatesResponse1Result - a model defined in Swagger

        :param data: The data of this VendorPlatesResponse1Result.  # noqa: E501
        :type data: List[VendorPlate]
        """
        self.swagger_types = {
            'data': List[VendorPlate]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'VendorPlatesResponse1Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vendorPlatesResponse_1_result of this VendorPlatesResponse1Result.  # noqa: E501
        :rtype: VendorPlatesResponse1Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[VendorPlate]:
        """Gets the data of this VendorPlatesResponse1Result.


        :return: The data of this VendorPlatesResponse1Result.
        :rtype: List[VendorPlate]
        """
        return self._data

    @data.setter
    def data(self, data: List[VendorPlate]):
        """Sets the data of this VendorPlatesResponse1Result.


        :param data: The data of this VendorPlatesResponse1Result.
        :type data: List[VendorPlate]
        """

        self._data = data
