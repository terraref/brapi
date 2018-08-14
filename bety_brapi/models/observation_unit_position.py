# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class ObservationUnitPosition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, x: str=None, y: str=None, additional_info: Dict[str, str]=None, block_number: str=None, entry_type: str=None, germplasm_db_id: str=None, germplasm_name: str=None, observation_level: str=None, observation_unit_db_id: str=None, observation_unit_name: str=None, position_coordinate_x: str=None, position_coordinate_x_type: str=None, position_coordinate_y: str=None, position_coordinate_y_type: str=None, replicate: str=None, study_db_id: str=None):  # noqa: E501
        """ObservationUnitPosition - a model defined in Swagger

        :param x: The x of this ObservationUnitPosition.  # noqa: E501
        :type x: str
        :param y: The y of this ObservationUnitPosition.  # noqa: E501
        :type y: str
        :param additional_info: The additional_info of this ObservationUnitPosition.  # noqa: E501
        :type additional_info: Dict[str, str]
        :param block_number: The block_number of this ObservationUnitPosition.  # noqa: E501
        :type block_number: str
        :param entry_type: The entry_type of this ObservationUnitPosition.  # noqa: E501
        :type entry_type: str
        :param germplasm_db_id: The germplasm_db_id of this ObservationUnitPosition.  # noqa: E501
        :type germplasm_db_id: str
        :param germplasm_name: The germplasm_name of this ObservationUnitPosition.  # noqa: E501
        :type germplasm_name: str
        :param observation_level: The observation_level of this ObservationUnitPosition.  # noqa: E501
        :type observation_level: str
        :param observation_unit_db_id: The observation_unit_db_id of this ObservationUnitPosition.  # noqa: E501
        :type observation_unit_db_id: str
        :param observation_unit_name: The observation_unit_name of this ObservationUnitPosition.  # noqa: E501
        :type observation_unit_name: str
        :param position_coordinate_x: The position_coordinate_x of this ObservationUnitPosition.  # noqa: E501
        :type position_coordinate_x: str
        :param position_coordinate_x_type: The position_coordinate_x_type of this ObservationUnitPosition.  # noqa: E501
        :type position_coordinate_x_type: str
        :param position_coordinate_y: The position_coordinate_y of this ObservationUnitPosition.  # noqa: E501
        :type position_coordinate_y: str
        :param position_coordinate_y_type: The position_coordinate_y_type of this ObservationUnitPosition.  # noqa: E501
        :type position_coordinate_y_type: str
        :param replicate: The replicate of this ObservationUnitPosition.  # noqa: E501
        :type replicate: str
        :param study_db_id: The study_db_id of this ObservationUnitPosition.  # noqa: E501
        :type study_db_id: str
        """
        self.swagger_types = {
            'x': str,
            'y': str,
            'additional_info': Dict[str, str],
            'block_number': str,
            'entry_type': str,
            'germplasm_db_id': str,
            'germplasm_name': str,
            'observation_level': str,
            'observation_unit_db_id': str,
            'observation_unit_name': str,
            'position_coordinate_x': str,
            'position_coordinate_x_type': str,
            'position_coordinate_y': str,
            'position_coordinate_y_type': str,
            'replicate': str,
            'study_db_id': str
        }

        self.attribute_map = {
            'x': 'X',
            'y': 'Y',
            'additional_info': 'additionalInfo',
            'block_number': 'blockNumber',
            'entry_type': 'entryType',
            'germplasm_db_id': 'germplasmDbId',
            'germplasm_name': 'germplasmName',
            'observation_level': 'observationLevel',
            'observation_unit_db_id': 'observationUnitDbId',
            'observation_unit_name': 'observationUnitName',
            'position_coordinate_x': 'positionCoordinateX',
            'position_coordinate_x_type': 'positionCoordinateXType',
            'position_coordinate_y': 'positionCoordinateY',
            'position_coordinate_y_type': 'positionCoordinateYType',
            'replicate': 'replicate',
            'study_db_id': 'studyDbId'
        }

        self._x = x
        self._y = y
        self._additional_info = additional_info
        self._block_number = block_number
        self._entry_type = entry_type
        self._germplasm_db_id = germplasm_db_id
        self._germplasm_name = germplasm_name
        self._observation_level = observation_level
        self._observation_unit_db_id = observation_unit_db_id
        self._observation_unit_name = observation_unit_name
        self._position_coordinate_x = position_coordinate_x
        self._position_coordinate_x_type = position_coordinate_x_type
        self._position_coordinate_y = position_coordinate_y
        self._position_coordinate_y_type = position_coordinate_y_type
        self._replicate = replicate
        self._study_db_id = study_db_id

    @classmethod
    def from_dict(cls, dikt) -> 'ObservationUnitPosition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The observationUnitPosition of this ObservationUnitPosition.  # noqa: E501
        :rtype: ObservationUnitPosition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self) -> str:
        """Gets the x of this ObservationUnitPosition.

        DEPRECATED - use \"positionCoordinateX\"  # noqa: E501

        :return: The x of this ObservationUnitPosition.
        :rtype: str
        """
        return self._x

    @x.setter
    def x(self, x: str):
        """Sets the x of this ObservationUnitPosition.

        DEPRECATED - use \"positionCoordinateX\"  # noqa: E501

        :param x: The x of this ObservationUnitPosition.
        :type x: str
        """

        self._x = x

    @property
    def y(self) -> str:
        """Gets the y of this ObservationUnitPosition.

        DEPRECATED - use \"positionCoordinateY\"  # noqa: E501

        :return: The y of this ObservationUnitPosition.
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y: str):
        """Sets the y of this ObservationUnitPosition.

        DEPRECATED - use \"positionCoordinateY\"  # noqa: E501

        :param y: The y of this ObservationUnitPosition.
        :type y: str
        """

        self._y = y

    @property
    def additional_info(self) -> Dict[str, str]:
        """Gets the additional_info of this ObservationUnitPosition.

        Additional arbitrary info  # noqa: E501

        :return: The additional_info of this ObservationUnitPosition.
        :rtype: Dict[str, str]
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info: Dict[str, str]):
        """Sets the additional_info of this ObservationUnitPosition.

        Additional arbitrary info  # noqa: E501

        :param additional_info: The additional_info of this ObservationUnitPosition.
        :type additional_info: Dict[str, str]
        """

        self._additional_info = additional_info

    @property
    def block_number(self) -> str:
        """Gets the block_number of this ObservationUnitPosition.

        The block number for an observation unit. Different systems may use different block designs.  # noqa: E501

        :return: The block_number of this ObservationUnitPosition.
        :rtype: str
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number: str):
        """Sets the block_number of this ObservationUnitPosition.

        The block number for an observation unit. Different systems may use different block designs.  # noqa: E501

        :param block_number: The block_number of this ObservationUnitPosition.
        :type block_number: str
        """

        self._block_number = block_number

    @property
    def entry_type(self) -> str:
        """Gets the entry_type of this ObservationUnitPosition.

        The type of entry for this observation unit. ex. \"check\", \"test\", \"filler\"  # noqa: E501

        :return: The entry_type of this ObservationUnitPosition.
        :rtype: str
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type: str):
        """Sets the entry_type of this ObservationUnitPosition.

        The type of entry for this observation unit. ex. \"check\", \"test\", \"filler\"  # noqa: E501

        :param entry_type: The entry_type of this ObservationUnitPosition.
        :type entry_type: str
        """
        allowed_values = ["CHECK", "TEST", "FILLER"]  # noqa: E501
        if entry_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entry_type` ({0}), must be one of {1}"
                .format(entry_type, allowed_values)
            )

        self._entry_type = entry_type

    @property
    def germplasm_db_id(self) -> str:
        """Gets the germplasm_db_id of this ObservationUnitPosition.

         The ID which uniquely identifies a germplasm  # noqa: E501

        :return: The germplasm_db_id of this ObservationUnitPosition.
        :rtype: str
        """
        return self._germplasm_db_id

    @germplasm_db_id.setter
    def germplasm_db_id(self, germplasm_db_id: str):
        """Sets the germplasm_db_id of this ObservationUnitPosition.

         The ID which uniquely identifies a germplasm  # noqa: E501

        :param germplasm_db_id: The germplasm_db_id of this ObservationUnitPosition.
        :type germplasm_db_id: str
        """

        self._germplasm_db_id = germplasm_db_id

    @property
    def germplasm_name(self) -> str:
        """Gets the germplasm_name of this ObservationUnitPosition.

        Name of the germplasm. It can be the prefered name and does not have to be unique.  # noqa: E501

        :return: The germplasm_name of this ObservationUnitPosition.
        :rtype: str
        """
        return self._germplasm_name

    @germplasm_name.setter
    def germplasm_name(self, germplasm_name: str):
        """Sets the germplasm_name of this ObservationUnitPosition.

        Name of the germplasm. It can be the prefered name and does not have to be unique.  # noqa: E501

        :param germplasm_name: The germplasm_name of this ObservationUnitPosition.
        :type germplasm_name: str
        """

        self._germplasm_name = germplasm_name

    @property
    def observation_level(self) -> str:
        """Gets the observation_level of this ObservationUnitPosition.

        The level of an observation unit. ex. \"plot\", \"plant\"  # noqa: E501

        :return: The observation_level of this ObservationUnitPosition.
        :rtype: str
        """
        return self._observation_level

    @observation_level.setter
    def observation_level(self, observation_level: str):
        """Sets the observation_level of this ObservationUnitPosition.

        The level of an observation unit. ex. \"plot\", \"plant\"  # noqa: E501

        :param observation_level: The observation_level of this ObservationUnitPosition.
        :type observation_level: str
        """

        self._observation_level = observation_level

    @property
    def observation_unit_db_id(self) -> str:
        """Gets the observation_unit_db_id of this ObservationUnitPosition.

        The ID which uniquely identifies an observation unit  # noqa: E501

        :return: The observation_unit_db_id of this ObservationUnitPosition.
        :rtype: str
        """
        return self._observation_unit_db_id

    @observation_unit_db_id.setter
    def observation_unit_db_id(self, observation_unit_db_id: str):
        """Sets the observation_unit_db_id of this ObservationUnitPosition.

        The ID which uniquely identifies an observation unit  # noqa: E501

        :param observation_unit_db_id: The observation_unit_db_id of this ObservationUnitPosition.
        :type observation_unit_db_id: str
        """

        self._observation_unit_db_id = observation_unit_db_id

    @property
    def observation_unit_name(self) -> str:
        """Gets the observation_unit_name of this ObservationUnitPosition.

        A human readable name for an observation unit  # noqa: E501

        :return: The observation_unit_name of this ObservationUnitPosition.
        :rtype: str
        """
        return self._observation_unit_name

    @observation_unit_name.setter
    def observation_unit_name(self, observation_unit_name: str):
        """Sets the observation_unit_name of this ObservationUnitPosition.

        A human readable name for an observation unit  # noqa: E501

        :param observation_unit_name: The observation_unit_name of this ObservationUnitPosition.
        :type observation_unit_name: str
        """

        self._observation_unit_name = observation_unit_name

    @property
    def position_coordinate_x(self) -> str:
        """Gets the position_coordinate_x of this ObservationUnitPosition.

        The X position coordinate for an observation unit. Different systems may use different coordinate systems.  # noqa: E501

        :return: The position_coordinate_x of this ObservationUnitPosition.
        :rtype: str
        """
        return self._position_coordinate_x

    @position_coordinate_x.setter
    def position_coordinate_x(self, position_coordinate_x: str):
        """Sets the position_coordinate_x of this ObservationUnitPosition.

        The X position coordinate for an observation unit. Different systems may use different coordinate systems.  # noqa: E501

        :param position_coordinate_x: The position_coordinate_x of this ObservationUnitPosition.
        :type position_coordinate_x: str
        """

        self._position_coordinate_x = position_coordinate_x

    @property
    def position_coordinate_x_type(self) -> str:
        """Gets the position_coordinate_x_type of this ObservationUnitPosition.

        The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column   # noqa: E501

        :return: The position_coordinate_x_type of this ObservationUnitPosition.
        :rtype: str
        """
        return self._position_coordinate_x_type

    @position_coordinate_x_type.setter
    def position_coordinate_x_type(self, position_coordinate_x_type: str):
        """Sets the position_coordinate_x_type of this ObservationUnitPosition.

        The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column   # noqa: E501

        :param position_coordinate_x_type: The position_coordinate_x_type of this ObservationUnitPosition.
        :type position_coordinate_x_type: str
        """
        allowed_values = ["LONGITUDE", "LATITUDE", "PLANTED_ROW", "PLANTED_INDIVIDUAl", "GRID_ROW", "GRID_COL", "MEASURED_ROW", "MEASURED_COL"]  # noqa: E501
        if position_coordinate_x_type not in allowed_values:
            raise ValueError(
                "Invalid value for `position_coordinate_x_type` ({0}), must be one of {1}"
                .format(position_coordinate_x_type, allowed_values)
            )

        self._position_coordinate_x_type = position_coordinate_x_type

    @property
    def position_coordinate_y(self) -> str:
        """Gets the position_coordinate_y of this ObservationUnitPosition.

        The Y position coordinate for an observation unit. Different systems may use different coordinate systems.  # noqa: E501

        :return: The position_coordinate_y of this ObservationUnitPosition.
        :rtype: str
        """
        return self._position_coordinate_y

    @position_coordinate_y.setter
    def position_coordinate_y(self, position_coordinate_y: str):
        """Sets the position_coordinate_y of this ObservationUnitPosition.

        The Y position coordinate for an observation unit. Different systems may use different coordinate systems.  # noqa: E501

        :param position_coordinate_y: The position_coordinate_y of this ObservationUnitPosition.
        :type position_coordinate_y: str
        """

        self._position_coordinate_y = position_coordinate_y

    @property
    def position_coordinate_y_type(self) -> str:
        """Gets the position_coordinate_y_type of this ObservationUnitPosition.

        The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column   # noqa: E501

        :return: The position_coordinate_y_type of this ObservationUnitPosition.
        :rtype: str
        """
        return self._position_coordinate_y_type

    @position_coordinate_y_type.setter
    def position_coordinate_y_type(self, position_coordinate_y_type: str):
        """Sets the position_coordinate_y_type of this ObservationUnitPosition.

        The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column   # noqa: E501

        :param position_coordinate_y_type: The position_coordinate_y_type of this ObservationUnitPosition.
        :type position_coordinate_y_type: str
        """
        allowed_values = ["LONGITUDE", "LATITUDE", "PLANTED_ROW", "PLANTED_INDIVIDUAl", "GRID_ROW", "GRID_COL", "MEASURED_ROW", "MEASURED_COL"]  # noqa: E501
        if position_coordinate_y_type not in allowed_values:
            raise ValueError(
                "Invalid value for `position_coordinate_y_type` ({0}), must be one of {1}"
                .format(position_coordinate_y_type, allowed_values)
            )

        self._position_coordinate_y_type = position_coordinate_y_type

    @property
    def replicate(self) -> str:
        """Gets the replicate of this ObservationUnitPosition.

        The replicate number of an observation unit. May be the same as blockNumber.  # noqa: E501

        :return: The replicate of this ObservationUnitPosition.
        :rtype: str
        """
        return self._replicate

    @replicate.setter
    def replicate(self, replicate: str):
        """Sets the replicate of this ObservationUnitPosition.

        The replicate number of an observation unit. May be the same as blockNumber.  # noqa: E501

        :param replicate: The replicate of this ObservationUnitPosition.
        :type replicate: str
        """

        self._replicate = replicate

    @property
    def study_db_id(self) -> str:
        """Gets the study_db_id of this ObservationUnitPosition.

        The ID which uniquely identifies a study within the given database server  # noqa: E501

        :return: The study_db_id of this ObservationUnitPosition.
        :rtype: str
        """
        return self._study_db_id

    @study_db_id.setter
    def study_db_id(self, study_db_id: str):
        """Sets the study_db_id of this ObservationUnitPosition.

        The ID which uniquely identifies a study within the given database server  # noqa: E501

        :param study_db_id: The study_db_id of this ObservationUnitPosition.
        :type study_db_id: str
        """

        self._study_db_id = study_db_id
