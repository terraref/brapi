# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.vendor_plate_request_plates import VendorPlateRequestPlates  # noqa: F401,E501
from bety_brapi import util


class VendorPlateRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, plates: List[VendorPlateRequestPlates]=None):  # noqa: E501
        """VendorPlateRequest - a model defined in Swagger

        :param plates: The plates of this VendorPlateRequest.  # noqa: E501
        :type plates: List[VendorPlateRequestPlates]
        """
        self.swagger_types = {
            'plates': List[VendorPlateRequestPlates]
        }

        self.attribute_map = {
            'plates': 'plates'
        }

        self._plates = plates

    @classmethod
    def from_dict(cls, dikt) -> 'VendorPlateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vendorPlateRequest of this VendorPlateRequest.  # noqa: E501
        :rtype: VendorPlateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plates(self) -> List[VendorPlateRequestPlates]:
        """Gets the plates of this VendorPlateRequest.

        Array of new plates to be submitted to a vendor  # noqa: E501

        :return: The plates of this VendorPlateRequest.
        :rtype: List[VendorPlateRequestPlates]
        """
        return self._plates

    @plates.setter
    def plates(self, plates: List[VendorPlateRequestPlates]):
        """Sets the plates of this VendorPlateRequest.

        Array of new plates to be submitted to a vendor  # noqa: E501

        :param plates: The plates of this VendorPlateRequest.
        :type plates: List[VendorPlateRequestPlates]
        """

        self._plates = plates
