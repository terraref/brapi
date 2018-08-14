# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class VendorSpecificationStandardRequirementBlankWellPosition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, number_of_blanks_per_plate: int=None, positions: List[str]=None):  # noqa: E501
        """VendorSpecificationStandardRequirementBlankWellPosition - a model defined in Swagger

        :param number_of_blanks_per_plate: The number_of_blanks_per_plate of this VendorSpecificationStandardRequirementBlankWellPosition.  # noqa: E501
        :type number_of_blanks_per_plate: int
        :param positions: The positions of this VendorSpecificationStandardRequirementBlankWellPosition.  # noqa: E501
        :type positions: List[str]
        """
        self.swagger_types = {
            'number_of_blanks_per_plate': int,
            'positions': List[str]
        }

        self.attribute_map = {
            'number_of_blanks_per_plate': 'numberOfBlanksPerPlate',
            'positions': 'positions'
        }

        self._number_of_blanks_per_plate = number_of_blanks_per_plate
        self._positions = positions

    @classmethod
    def from_dict(cls, dikt) -> 'VendorSpecificationStandardRequirementBlankWellPosition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vendorSpecificationStandardRequirement_blankWellPosition of this VendorSpecificationStandardRequirementBlankWellPosition.  # noqa: E501
        :rtype: VendorSpecificationStandardRequirementBlankWellPosition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def number_of_blanks_per_plate(self) -> int:
        """Gets the number_of_blanks_per_plate of this VendorSpecificationStandardRequirementBlankWellPosition.


        :return: The number_of_blanks_per_plate of this VendorSpecificationStandardRequirementBlankWellPosition.
        :rtype: int
        """
        return self._number_of_blanks_per_plate

    @number_of_blanks_per_plate.setter
    def number_of_blanks_per_plate(self, number_of_blanks_per_plate: int):
        """Sets the number_of_blanks_per_plate of this VendorSpecificationStandardRequirementBlankWellPosition.


        :param number_of_blanks_per_plate: The number_of_blanks_per_plate of this VendorSpecificationStandardRequirementBlankWellPosition.
        :type number_of_blanks_per_plate: int
        """

        self._number_of_blanks_per_plate = number_of_blanks_per_plate

    @property
    def positions(self) -> List[str]:
        """Gets the positions of this VendorSpecificationStandardRequirementBlankWellPosition.


        :return: The positions of this VendorSpecificationStandardRequirementBlankWellPosition.
        :rtype: List[str]
        """
        return self._positions

    @positions.setter
    def positions(self, positions: List[str]):
        """Sets the positions of this VendorSpecificationStandardRequirementBlankWellPosition.


        :param positions: The positions of this VendorSpecificationStandardRequirementBlankWellPosition.
        :type positions: List[str]
        """

        self._positions = positions
