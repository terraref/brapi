# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.observation_variable import ObservationVariable  # noqa: F401,E501
from bety_brapi import util


class StudyObservationVariablesResponseResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, data: List[ObservationVariable]=None, study_db_id: str=None, trial_name: str=None):  # noqa: E501
        """StudyObservationVariablesResponseResult - a model defined in Swagger

        :param data: The data of this StudyObservationVariablesResponseResult.  # noqa: E501
        :type data: List[ObservationVariable]
        :param study_db_id: The study_db_id of this StudyObservationVariablesResponseResult.  # noqa: E501
        :type study_db_id: str
        :param trial_name: The trial_name of this StudyObservationVariablesResponseResult.  # noqa: E501
        :type trial_name: str
        """
        self.swagger_types = {
            'data': List[ObservationVariable],
            'study_db_id': str,
            'trial_name': str
        }

        self.attribute_map = {
            'data': 'data',
            'study_db_id': 'studyDbId',
            'trial_name': 'trialName'
        }

        self._data = data
        self._study_db_id = study_db_id
        self._trial_name = trial_name

    @classmethod
    def from_dict(cls, dikt) -> 'StudyObservationVariablesResponseResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The studyObservationVariablesResponse_result of this StudyObservationVariablesResponseResult.  # noqa: E501
        :rtype: StudyObservationVariablesResponseResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[ObservationVariable]:
        """Gets the data of this StudyObservationVariablesResponseResult.


        :return: The data of this StudyObservationVariablesResponseResult.
        :rtype: List[ObservationVariable]
        """
        return self._data

    @data.setter
    def data(self, data: List[ObservationVariable]):
        """Sets the data of this StudyObservationVariablesResponseResult.


        :param data: The data of this StudyObservationVariablesResponseResult.
        :type data: List[ObservationVariable]
        """

        self._data = data

    @property
    def study_db_id(self) -> str:
        """Gets the study_db_id of this StudyObservationVariablesResponseResult.


        :return: The study_db_id of this StudyObservationVariablesResponseResult.
        :rtype: str
        """
        return self._study_db_id

    @study_db_id.setter
    def study_db_id(self, study_db_id: str):
        """Sets the study_db_id of this StudyObservationVariablesResponseResult.


        :param study_db_id: The study_db_id of this StudyObservationVariablesResponseResult.
        :type study_db_id: str
        """

        self._study_db_id = study_db_id

    @property
    def trial_name(self) -> str:
        """Gets the trial_name of this StudyObservationVariablesResponseResult.


        :return: The trial_name of this StudyObservationVariablesResponseResult.
        :rtype: str
        """
        return self._trial_name

    @trial_name.setter
    def trial_name(self, trial_name: str):
        """Sets the trial_name of this StudyObservationVariablesResponseResult.


        :param trial_name: The trial_name of this StudyObservationVariablesResponseResult.
        :type trial_name: str
        """

        self._trial_name = trial_name
