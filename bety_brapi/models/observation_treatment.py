# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class ObservationTreatment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, factor: str=None, modality: str=None):  # noqa: E501
        """ObservationTreatment - a model defined in Swagger

        :param factor: The factor of this ObservationTreatment.  # noqa: E501
        :type factor: str
        :param modality: The modality of this ObservationTreatment.  # noqa: E501
        :type modality: str
        """
        self.swagger_types = {
            'factor': str,
            'modality': str
        }

        self.attribute_map = {
            'factor': 'factor',
            'modality': 'modality'
        }

        self._factor = factor
        self._modality = modality

    @classmethod
    def from_dict(cls, dikt) -> 'ObservationTreatment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The observationTreatment of this ObservationTreatment.  # noqa: E501
        :rtype: ObservationTreatment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def factor(self) -> str:
        """Gets the factor of this ObservationTreatment.

        The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  # noqa: E501

        :return: The factor of this ObservationTreatment.
        :rtype: str
        """
        return self._factor

    @factor.setter
    def factor(self, factor: str):
        """Sets the factor of this ObservationTreatment.

        The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  # noqa: E501

        :param factor: The factor of this ObservationTreatment.
        :type factor: str
        """

        self._factor = factor

    @property
    def modality(self) -> str:
        """Gets the modality of this ObservationTreatment.

        The treatment/factor descritpion. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  # noqa: E501

        :return: The modality of this ObservationTreatment.
        :rtype: str
        """
        return self._modality

    @modality.setter
    def modality(self, modality: str):
        """Sets the modality of this ObservationTreatment.

        The treatment/factor descritpion. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  # noqa: E501

        :param modality: The modality of this ObservationTreatment.
        :type modality: str
        """

        self._modality = modality
