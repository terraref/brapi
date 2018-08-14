# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.vendor_plate import VendorPlate  # noqa: F401,E501
from bety_brapi import util


class VendorPlatesResponseResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, plates: List[VendorPlate]=None):  # noqa: E501
        """VendorPlatesResponseResult - a model defined in Swagger

        :param plates: The plates of this VendorPlatesResponseResult.  # noqa: E501
        :type plates: List[VendorPlate]
        """
        self.swagger_types = {
            'plates': List[VendorPlate]
        }

        self.attribute_map = {
            'plates': 'plates'
        }

        self._plates = plates

    @classmethod
    def from_dict(cls, dikt) -> 'VendorPlatesResponseResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vendorPlatesResponse_result of this VendorPlatesResponseResult.  # noqa: E501
        :rtype: VendorPlatesResponseResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plates(self) -> List[VendorPlate]:
        """Gets the plates of this VendorPlatesResponseResult.


        :return: The plates of this VendorPlatesResponseResult.
        :rtype: List[VendorPlate]
        """
        return self._plates

    @plates.setter
    def plates(self, plates: List[VendorPlate]):
        """Sets the plates of this VendorPlatesResponseResult.


        :param plates: The plates of this VendorPlatesResponseResult.
        :type plates: List[VendorPlate]
        """

        self._plates = plates
