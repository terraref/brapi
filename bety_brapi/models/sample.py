# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class Sample(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, germplasm_db_id: str=None, notes: str=None, observation_unit_db_id: str=None, plant_db_id: str=None, plate_db_id: str=None, plate_index: int=None, plot_db_id: str=None, sample_db_id: str=None, sample_timestamp: datetime=None, sample_type: str=None, study_db_id: str=None, taken_by: str=None, tissue_type: str=None):  # noqa: E501
        """Sample - a model defined in Swagger

        :param germplasm_db_id: The germplasm_db_id of this Sample.  # noqa: E501
        :type germplasm_db_id: str
        :param notes: The notes of this Sample.  # noqa: E501
        :type notes: str
        :param observation_unit_db_id: The observation_unit_db_id of this Sample.  # noqa: E501
        :type observation_unit_db_id: str
        :param plant_db_id: The plant_db_id of this Sample.  # noqa: E501
        :type plant_db_id: str
        :param plate_db_id: The plate_db_id of this Sample.  # noqa: E501
        :type plate_db_id: str
        :param plate_index: The plate_index of this Sample.  # noqa: E501
        :type plate_index: int
        :param plot_db_id: The plot_db_id of this Sample.  # noqa: E501
        :type plot_db_id: str
        :param sample_db_id: The sample_db_id of this Sample.  # noqa: E501
        :type sample_db_id: str
        :param sample_timestamp: The sample_timestamp of this Sample.  # noqa: E501
        :type sample_timestamp: datetime
        :param sample_type: The sample_type of this Sample.  # noqa: E501
        :type sample_type: str
        :param study_db_id: The study_db_id of this Sample.  # noqa: E501
        :type study_db_id: str
        :param taken_by: The taken_by of this Sample.  # noqa: E501
        :type taken_by: str
        :param tissue_type: The tissue_type of this Sample.  # noqa: E501
        :type tissue_type: str
        """
        self.swagger_types = {
            'germplasm_db_id': str,
            'notes': str,
            'observation_unit_db_id': str,
            'plant_db_id': str,
            'plate_db_id': str,
            'plate_index': int,
            'plot_db_id': str,
            'sample_db_id': str,
            'sample_timestamp': datetime,
            'sample_type': str,
            'study_db_id': str,
            'taken_by': str,
            'tissue_type': str
        }

        self.attribute_map = {
            'germplasm_db_id': 'germplasmDbId',
            'notes': 'notes',
            'observation_unit_db_id': 'observationUnitDbId',
            'plant_db_id': 'plantDbId',
            'plate_db_id': 'plateDbId',
            'plate_index': 'plateIndex',
            'plot_db_id': 'plotDbId',
            'sample_db_id': 'sampleDbId',
            'sample_timestamp': 'sampleTimestamp',
            'sample_type': 'sampleType',
            'study_db_id': 'studyDbId',
            'taken_by': 'takenBy',
            'tissue_type': 'tissueType'
        }

        self._germplasm_db_id = germplasm_db_id
        self._notes = notes
        self._observation_unit_db_id = observation_unit_db_id
        self._plant_db_id = plant_db_id
        self._plate_db_id = plate_db_id
        self._plate_index = plate_index
        self._plot_db_id = plot_db_id
        self._sample_db_id = sample_db_id
        self._sample_timestamp = sample_timestamp
        self._sample_type = sample_type
        self._study_db_id = study_db_id
        self._taken_by = taken_by
        self._tissue_type = tissue_type

    @classmethod
    def from_dict(cls, dikt) -> 'Sample':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The sample of this Sample.  # noqa: E501
        :rtype: Sample
        """
        return util.deserialize_model(dikt, cls)

    @property
    def germplasm_db_id(self) -> str:
        """Gets the germplasm_db_id of this Sample.

         The ID which uniquely identifies a germplasm  # noqa: E501

        :return: The germplasm_db_id of this Sample.
        :rtype: str
        """
        return self._germplasm_db_id

    @germplasm_db_id.setter
    def germplasm_db_id(self, germplasm_db_id: str):
        """Sets the germplasm_db_id of this Sample.

         The ID which uniquely identifies a germplasm  # noqa: E501

        :param germplasm_db_id: The germplasm_db_id of this Sample.
        :type germplasm_db_id: str
        """

        self._germplasm_db_id = germplasm_db_id

    @property
    def notes(self) -> str:
        """Gets the notes of this Sample.

        Additional notes about a samle  # noqa: E501

        :return: The notes of this Sample.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """Sets the notes of this Sample.

        Additional notes about a samle  # noqa: E501

        :param notes: The notes of this Sample.
        :type notes: str
        """

        self._notes = notes

    @property
    def observation_unit_db_id(self) -> str:
        """Gets the observation_unit_db_id of this Sample.

        The ID which uniquely identifies an observation unit  # noqa: E501

        :return: The observation_unit_db_id of this Sample.
        :rtype: str
        """
        return self._observation_unit_db_id

    @observation_unit_db_id.setter
    def observation_unit_db_id(self, observation_unit_db_id: str):
        """Sets the observation_unit_db_id of this Sample.

        The ID which uniquely identifies an observation unit  # noqa: E501

        :param observation_unit_db_id: The observation_unit_db_id of this Sample.
        :type observation_unit_db_id: str
        """

        self._observation_unit_db_id = observation_unit_db_id

    @property
    def plant_db_id(self) -> str:
        """Gets the plant_db_id of this Sample.

        The ID which uniquely identifies a plant. Usually 'plantNumber'  # noqa: E501

        :return: The plant_db_id of this Sample.
        :rtype: str
        """
        return self._plant_db_id

    @plant_db_id.setter
    def plant_db_id(self, plant_db_id: str):
        """Sets the plant_db_id of this Sample.

        The ID which uniquely identifies a plant. Usually 'plantNumber'  # noqa: E501

        :param plant_db_id: The plant_db_id of this Sample.
        :type plant_db_id: str
        """

        self._plant_db_id = plant_db_id

    @property
    def plate_db_id(self) -> str:
        """Gets the plate_db_id of this Sample.

        The ID which uniquely identifies a plate of samples  # noqa: E501

        :return: The plate_db_id of this Sample.
        :rtype: str
        """
        return self._plate_db_id

    @plate_db_id.setter
    def plate_db_id(self, plate_db_id: str):
        """Sets the plate_db_id of this Sample.

        The ID which uniquely identifies a plate of samples  # noqa: E501

        :param plate_db_id: The plate_db_id of this Sample.
        :type plate_db_id: str
        """

        self._plate_db_id = plate_db_id

    @property
    def plate_index(self) -> int:
        """Gets the plate_index of this Sample.

        The index number of this sample on a plate  # noqa: E501

        :return: The plate_index of this Sample.
        :rtype: int
        """
        return self._plate_index

    @plate_index.setter
    def plate_index(self, plate_index: int):
        """Sets the plate_index of this Sample.

        The index number of this sample on a plate  # noqa: E501

        :param plate_index: The plate_index of this Sample.
        :type plate_index: int
        """

        self._plate_index = plate_index

    @property
    def plot_db_id(self) -> str:
        """Gets the plot_db_id of this Sample.

         The ID which uniquely identifies a plot. Usually 'plotNumber'  # noqa: E501

        :return: The plot_db_id of this Sample.
        :rtype: str
        """
        return self._plot_db_id

    @plot_db_id.setter
    def plot_db_id(self, plot_db_id: str):
        """Sets the plot_db_id of this Sample.

         The ID which uniquely identifies a plot. Usually 'plotNumber'  # noqa: E501

        :param plot_db_id: The plot_db_id of this Sample.
        :type plot_db_id: str
        """

        self._plot_db_id = plot_db_id

    @property
    def sample_db_id(self) -> str:
        """Gets the sample_db_id of this Sample.

        The ID which uniquely identifies a sample  # noqa: E501

        :return: The sample_db_id of this Sample.
        :rtype: str
        """
        return self._sample_db_id

    @sample_db_id.setter
    def sample_db_id(self, sample_db_id: str):
        """Sets the sample_db_id of this Sample.

        The ID which uniquely identifies a sample  # noqa: E501

        :param sample_db_id: The sample_db_id of this Sample.
        :type sample_db_id: str
        """

        self._sample_db_id = sample_db_id

    @property
    def sample_timestamp(self) -> datetime:
        """Gets the sample_timestamp of this Sample.

        The date and time a sample was collected from the field  # noqa: E501

        :return: The sample_timestamp of this Sample.
        :rtype: datetime
        """
        return self._sample_timestamp

    @sample_timestamp.setter
    def sample_timestamp(self, sample_timestamp: datetime):
        """Sets the sample_timestamp of this Sample.

        The date and time a sample was collected from the field  # noqa: E501

        :param sample_timestamp: The sample_timestamp of this Sample.
        :type sample_timestamp: datetime
        """

        self._sample_timestamp = sample_timestamp

    @property
    def sample_type(self) -> str:
        """Gets the sample_type of this Sample.

        The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc   # noqa: E501

        :return: The sample_type of this Sample.
        :rtype: str
        """
        return self._sample_type

    @sample_type.setter
    def sample_type(self, sample_type: str):
        """Sets the sample_type of this Sample.

        The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc   # noqa: E501

        :param sample_type: The sample_type of this Sample.
        :type sample_type: str
        """

        self._sample_type = sample_type

    @property
    def study_db_id(self) -> str:
        """Gets the study_db_id of this Sample.

        The ID which uniquely identifies a study within the given database server  # noqa: E501

        :return: The study_db_id of this Sample.
        :rtype: str
        """
        return self._study_db_id

    @study_db_id.setter
    def study_db_id(self, study_db_id: str):
        """Sets the study_db_id of this Sample.

        The ID which uniquely identifies a study within the given database server  # noqa: E501

        :param study_db_id: The study_db_id of this Sample.
        :type study_db_id: str
        """

        self._study_db_id = study_db_id

    @property
    def taken_by(self) -> str:
        """Gets the taken_by of this Sample.

        The name or identifier of the entity which took the sample from the field  # noqa: E501

        :return: The taken_by of this Sample.
        :rtype: str
        """
        return self._taken_by

    @taken_by.setter
    def taken_by(self, taken_by: str):
        """Sets the taken_by of this Sample.

        The name or identifier of the entity which took the sample from the field  # noqa: E501

        :param taken_by: The taken_by of this Sample.
        :type taken_by: str
        """

        self._taken_by = taken_by

    @property
    def tissue_type(self) -> str:
        """Gets the tissue_type of this Sample.

        The type of tissue sampled. ex. 'Leaf', 'Root', etc.  # noqa: E501

        :return: The tissue_type of this Sample.
        :rtype: str
        """
        return self._tissue_type

    @tissue_type.setter
    def tissue_type(self, tissue_type: str):
        """Sets the tissue_type of this Sample.

        The type of tissue sampled. ex. 'Leaf', 'Root', etc.  # noqa: E501

        :param tissue_type: The tissue_type of this Sample.
        :type tissue_type: str
        """

        self._tissue_type = tissue_type
