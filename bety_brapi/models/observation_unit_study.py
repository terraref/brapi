# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.observation_summary import ObservationSummary  # noqa: F401,E501
from bety_brapi.models.observation_unit_xref import ObservationUnitXref  # noqa: F401,E501
from bety_brapi import util


class ObservationUnitStudy(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, x: str=None, y: str=None, block_number: str=None, entry_number: str=None, entry_type: str=None, germplasm_db_id: str=None, germplasm_name: str=None, observation_unit_db_id: str=None, observation_unit_name: str=None, observation_unit_xref: List[ObservationUnitXref]=None, observations: List[ObservationSummary]=None, pedigree: str=None, plant_number: str=None, plot_number: str=None, position_coordinate_x: str=None, position_coordinate_x_type: str=None, position_coordinate_y: str=None, position_coordinate_y_type: str=None, replicate: str=None):  # noqa: E501
        """ObservationUnitStudy - a model defined in Swagger

        :param x: The x of this ObservationUnitStudy.  # noqa: E501
        :type x: str
        :param y: The y of this ObservationUnitStudy.  # noqa: E501
        :type y: str
        :param block_number: The block_number of this ObservationUnitStudy.  # noqa: E501
        :type block_number: str
        :param entry_number: The entry_number of this ObservationUnitStudy.  # noqa: E501
        :type entry_number: str
        :param entry_type: The entry_type of this ObservationUnitStudy.  # noqa: E501
        :type entry_type: str
        :param germplasm_db_id: The germplasm_db_id of this ObservationUnitStudy.  # noqa: E501
        :type germplasm_db_id: str
        :param germplasm_name: The germplasm_name of this ObservationUnitStudy.  # noqa: E501
        :type germplasm_name: str
        :param observation_unit_db_id: The observation_unit_db_id of this ObservationUnitStudy.  # noqa: E501
        :type observation_unit_db_id: str
        :param observation_unit_name: The observation_unit_name of this ObservationUnitStudy.  # noqa: E501
        :type observation_unit_name: str
        :param observation_unit_xref: The observation_unit_xref of this ObservationUnitStudy.  # noqa: E501
        :type observation_unit_xref: List[ObservationUnitXref]
        :param observations: The observations of this ObservationUnitStudy.  # noqa: E501
        :type observations: List[ObservationSummary]
        :param pedigree: The pedigree of this ObservationUnitStudy.  # noqa: E501
        :type pedigree: str
        :param plant_number: The plant_number of this ObservationUnitStudy.  # noqa: E501
        :type plant_number: str
        :param plot_number: The plot_number of this ObservationUnitStudy.  # noqa: E501
        :type plot_number: str
        :param position_coordinate_x: The position_coordinate_x of this ObservationUnitStudy.  # noqa: E501
        :type position_coordinate_x: str
        :param position_coordinate_x_type: The position_coordinate_x_type of this ObservationUnitStudy.  # noqa: E501
        :type position_coordinate_x_type: str
        :param position_coordinate_y: The position_coordinate_y of this ObservationUnitStudy.  # noqa: E501
        :type position_coordinate_y: str
        :param position_coordinate_y_type: The position_coordinate_y_type of this ObservationUnitStudy.  # noqa: E501
        :type position_coordinate_y_type: str
        :param replicate: The replicate of this ObservationUnitStudy.  # noqa: E501
        :type replicate: str
        """
        self.swagger_types = {
            'x': str,
            'y': str,
            'block_number': str,
            'entry_number': str,
            'entry_type': str,
            'germplasm_db_id': str,
            'germplasm_name': str,
            'observation_unit_db_id': str,
            'observation_unit_name': str,
            'observation_unit_xref': List[ObservationUnitXref],
            'observations': List[ObservationSummary],
            'pedigree': str,
            'plant_number': str,
            'plot_number': str,
            'position_coordinate_x': str,
            'position_coordinate_x_type': str,
            'position_coordinate_y': str,
            'position_coordinate_y_type': str,
            'replicate': str
        }

        self.attribute_map = {
            'x': 'X',
            'y': 'Y',
            'block_number': 'blockNumber',
            'entry_number': 'entryNumber',
            'entry_type': 'entryType',
            'germplasm_db_id': 'germplasmDbId',
            'germplasm_name': 'germplasmName',
            'observation_unit_db_id': 'observationUnitDbId',
            'observation_unit_name': 'observationUnitName',
            'observation_unit_xref': 'observationUnitXref',
            'observations': 'observations',
            'pedigree': 'pedigree',
            'plant_number': 'plantNumber',
            'plot_number': 'plotNumber',
            'position_coordinate_x': 'positionCoordinateX',
            'position_coordinate_x_type': 'positionCoordinateXType',
            'position_coordinate_y': 'positionCoordinateY',
            'position_coordinate_y_type': 'positionCoordinateYType',
            'replicate': 'replicate'
        }

        self._x = x
        self._y = y
        self._block_number = block_number
        self._entry_number = entry_number
        self._entry_type = entry_type
        self._germplasm_db_id = germplasm_db_id
        self._germplasm_name = germplasm_name
        self._observation_unit_db_id = observation_unit_db_id
        self._observation_unit_name = observation_unit_name
        self._observation_unit_xref = observation_unit_xref
        self._observations = observations
        self._pedigree = pedigree
        self._plant_number = plant_number
        self._plot_number = plot_number
        self._position_coordinate_x = position_coordinate_x
        self._position_coordinate_x_type = position_coordinate_x_type
        self._position_coordinate_y = position_coordinate_y
        self._position_coordinate_y_type = position_coordinate_y_type
        self._replicate = replicate

    @classmethod
    def from_dict(cls, dikt) -> 'ObservationUnitStudy':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The observationUnitStudy of this ObservationUnitStudy.  # noqa: E501
        :rtype: ObservationUnitStudy
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self) -> str:
        """Gets the x of this ObservationUnitStudy.

        DEPRECATED - use \"positionCoordinateX\"  # noqa: E501

        :return: The x of this ObservationUnitStudy.
        :rtype: str
        """
        return self._x

    @x.setter
    def x(self, x: str):
        """Sets the x of this ObservationUnitStudy.

        DEPRECATED - use \"positionCoordinateX\"  # noqa: E501

        :param x: The x of this ObservationUnitStudy.
        :type x: str
        """

        self._x = x

    @property
    def y(self) -> str:
        """Gets the y of this ObservationUnitStudy.

        DEPRECATED - use \"positionCoordinateY\"  # noqa: E501

        :return: The y of this ObservationUnitStudy.
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y: str):
        """Sets the y of this ObservationUnitStudy.

        DEPRECATED - use \"positionCoordinateY\"  # noqa: E501

        :param y: The y of this ObservationUnitStudy.
        :type y: str
        """

        self._y = y

    @property
    def block_number(self) -> str:
        """Gets the block_number of this ObservationUnitStudy.

        The block number for an observation unit. Different systems may use different block designs.  # noqa: E501

        :return: The block_number of this ObservationUnitStudy.
        :rtype: str
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number: str):
        """Sets the block_number of this ObservationUnitStudy.

        The block number for an observation unit. Different systems may use different block designs.  # noqa: E501

        :param block_number: The block_number of this ObservationUnitStudy.
        :type block_number: str
        """

        self._block_number = block_number

    @property
    def entry_number(self) -> str:
        """Gets the entry_number of this ObservationUnitStudy.

        The entry number for an observation unit. Different systems may use different entry systems.  # noqa: E501

        :return: The entry_number of this ObservationUnitStudy.
        :rtype: str
        """
        return self._entry_number

    @entry_number.setter
    def entry_number(self, entry_number: str):
        """Sets the entry_number of this ObservationUnitStudy.

        The entry number for an observation unit. Different systems may use different entry systems.  # noqa: E501

        :param entry_number: The entry_number of this ObservationUnitStudy.
        :type entry_number: str
        """

        self._entry_number = entry_number

    @property
    def entry_type(self) -> str:
        """Gets the entry_type of this ObservationUnitStudy.

        The type of entry for this observation unit. ex. \"check\", \"test\", \"filler\"  # noqa: E501

        :return: The entry_type of this ObservationUnitStudy.
        :rtype: str
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type: str):
        """Sets the entry_type of this ObservationUnitStudy.

        The type of entry for this observation unit. ex. \"check\", \"test\", \"filler\"  # noqa: E501

        :param entry_type: The entry_type of this ObservationUnitStudy.
        :type entry_type: str
        """

        self._entry_type = entry_type

    @property
    def germplasm_db_id(self) -> str:
        """Gets the germplasm_db_id of this ObservationUnitStudy.

         The ID which uniquely identifies a germplasm  # noqa: E501

        :return: The germplasm_db_id of this ObservationUnitStudy.
        :rtype: str
        """
        return self._germplasm_db_id

    @germplasm_db_id.setter
    def germplasm_db_id(self, germplasm_db_id: str):
        """Sets the germplasm_db_id of this ObservationUnitStudy.

         The ID which uniquely identifies a germplasm  # noqa: E501

        :param germplasm_db_id: The germplasm_db_id of this ObservationUnitStudy.
        :type germplasm_db_id: str
        """

        self._germplasm_db_id = germplasm_db_id

    @property
    def germplasm_name(self) -> str:
        """Gets the germplasm_name of this ObservationUnitStudy.

        Name of the germplasm. It can be the prefered name and does not have to be unique.  # noqa: E501

        :return: The germplasm_name of this ObservationUnitStudy.
        :rtype: str
        """
        return self._germplasm_name

    @germplasm_name.setter
    def germplasm_name(self, germplasm_name: str):
        """Sets the germplasm_name of this ObservationUnitStudy.

        Name of the germplasm. It can be the prefered name and does not have to be unique.  # noqa: E501

        :param germplasm_name: The germplasm_name of this ObservationUnitStudy.
        :type germplasm_name: str
        """

        self._germplasm_name = germplasm_name

    @property
    def observation_unit_db_id(self) -> str:
        """Gets the observation_unit_db_id of this ObservationUnitStudy.

        The ID which uniquely identifies an observation unit  # noqa: E501

        :return: The observation_unit_db_id of this ObservationUnitStudy.
        :rtype: str
        """
        return self._observation_unit_db_id

    @observation_unit_db_id.setter
    def observation_unit_db_id(self, observation_unit_db_id: str):
        """Sets the observation_unit_db_id of this ObservationUnitStudy.

        The ID which uniquely identifies an observation unit  # noqa: E501

        :param observation_unit_db_id: The observation_unit_db_id of this ObservationUnitStudy.
        :type observation_unit_db_id: str
        """

        self._observation_unit_db_id = observation_unit_db_id

    @property
    def observation_unit_name(self) -> str:
        """Gets the observation_unit_name of this ObservationUnitStudy.

        A human readable name for an observation unit  # noqa: E501

        :return: The observation_unit_name of this ObservationUnitStudy.
        :rtype: str
        """
        return self._observation_unit_name

    @observation_unit_name.setter
    def observation_unit_name(self, observation_unit_name: str):
        """Sets the observation_unit_name of this ObservationUnitStudy.

        A human readable name for an observation unit  # noqa: E501

        :param observation_unit_name: The observation_unit_name of this ObservationUnitStudy.
        :type observation_unit_name: str
        """

        self._observation_unit_name = observation_unit_name

    @property
    def observation_unit_xref(self) -> List[ObservationUnitXref]:
        """Gets the observation_unit_xref of this ObservationUnitStudy.

        A list of external references to this observation unit  # noqa: E501

        :return: The observation_unit_xref of this ObservationUnitStudy.
        :rtype: List[ObservationUnitXref]
        """
        return self._observation_unit_xref

    @observation_unit_xref.setter
    def observation_unit_xref(self, observation_unit_xref: List[ObservationUnitXref]):
        """Sets the observation_unit_xref of this ObservationUnitStudy.

        A list of external references to this observation unit  # noqa: E501

        :param observation_unit_xref: The observation_unit_xref of this ObservationUnitStudy.
        :type observation_unit_xref: List[ObservationUnitXref]
        """

        self._observation_unit_xref = observation_unit_xref

    @property
    def observations(self) -> List[ObservationSummary]:
        """Gets the observations of this ObservationUnitStudy.

        List of observations associated with this observation unit  # noqa: E501

        :return: The observations of this ObservationUnitStudy.
        :rtype: List[ObservationSummary]
        """
        return self._observations

    @observations.setter
    def observations(self, observations: List[ObservationSummary]):
        """Sets the observations of this ObservationUnitStudy.

        List of observations associated with this observation unit  # noqa: E501

        :param observations: The observations of this ObservationUnitStudy.
        :type observations: List[ObservationSummary]
        """

        self._observations = observations

    @property
    def pedigree(self) -> str:
        """Gets the pedigree of this ObservationUnitStudy.

        The string representation of the pedigree of this observation unit  # noqa: E501

        :return: The pedigree of this ObservationUnitStudy.
        :rtype: str
        """
        return self._pedigree

    @pedigree.setter
    def pedigree(self, pedigree: str):
        """Sets the pedigree of this ObservationUnitStudy.

        The string representation of the pedigree of this observation unit  # noqa: E501

        :param pedigree: The pedigree of this ObservationUnitStudy.
        :type pedigree: str
        """

        self._pedigree = pedigree

    @property
    def plant_number(self) -> str:
        """Gets the plant_number of this ObservationUnitStudy.

        The plant number in a field. Applicable for observationLevel: \"plant\"  # noqa: E501

        :return: The plant_number of this ObservationUnitStudy.
        :rtype: str
        """
        return self._plant_number

    @plant_number.setter
    def plant_number(self, plant_number: str):
        """Sets the plant_number of this ObservationUnitStudy.

        The plant number in a field. Applicable for observationLevel: \"plant\"  # noqa: E501

        :param plant_number: The plant_number of this ObservationUnitStudy.
        :type plant_number: str
        """

        self._plant_number = plant_number

    @property
    def plot_number(self) -> str:
        """Gets the plot_number of this ObservationUnitStudy.

        The plot number in a field. Applicable for observationLevel: \"plot\"  # noqa: E501

        :return: The plot_number of this ObservationUnitStudy.
        :rtype: str
        """
        return self._plot_number

    @plot_number.setter
    def plot_number(self, plot_number: str):
        """Sets the plot_number of this ObservationUnitStudy.

        The plot number in a field. Applicable for observationLevel: \"plot\"  # noqa: E501

        :param plot_number: The plot_number of this ObservationUnitStudy.
        :type plot_number: str
        """

        self._plot_number = plot_number

    @property
    def position_coordinate_x(self) -> str:
        """Gets the position_coordinate_x of this ObservationUnitStudy.

        The X position coordinate for an observation unit. Different systems may use different coordinate systems.  # noqa: E501

        :return: The position_coordinate_x of this ObservationUnitStudy.
        :rtype: str
        """
        return self._position_coordinate_x

    @position_coordinate_x.setter
    def position_coordinate_x(self, position_coordinate_x: str):
        """Sets the position_coordinate_x of this ObservationUnitStudy.

        The X position coordinate for an observation unit. Different systems may use different coordinate systems.  # noqa: E501

        :param position_coordinate_x: The position_coordinate_x of this ObservationUnitStudy.
        :type position_coordinate_x: str
        """

        self._position_coordinate_x = position_coordinate_x

    @property
    def position_coordinate_x_type(self) -> str:
        """Gets the position_coordinate_x_type of this ObservationUnitStudy.

        The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column   # noqa: E501

        :return: The position_coordinate_x_type of this ObservationUnitStudy.
        :rtype: str
        """
        return self._position_coordinate_x_type

    @position_coordinate_x_type.setter
    def position_coordinate_x_type(self, position_coordinate_x_type: str):
        """Sets the position_coordinate_x_type of this ObservationUnitStudy.

        The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column   # noqa: E501

        :param position_coordinate_x_type: The position_coordinate_x_type of this ObservationUnitStudy.
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
        """Gets the position_coordinate_y of this ObservationUnitStudy.

        The Y position coordinate for an observation unit. Different systems may use different coordinate systems.  # noqa: E501

        :return: The position_coordinate_y of this ObservationUnitStudy.
        :rtype: str
        """
        return self._position_coordinate_y

    @position_coordinate_y.setter
    def position_coordinate_y(self, position_coordinate_y: str):
        """Sets the position_coordinate_y of this ObservationUnitStudy.

        The Y position coordinate for an observation unit. Different systems may use different coordinate systems.  # noqa: E501

        :param position_coordinate_y: The position_coordinate_y of this ObservationUnitStudy.
        :type position_coordinate_y: str
        """

        self._position_coordinate_y = position_coordinate_y

    @property
    def position_coordinate_y_type(self) -> str:
        """Gets the position_coordinate_y_type of this ObservationUnitStudy.

        The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column   # noqa: E501

        :return: The position_coordinate_y_type of this ObservationUnitStudy.
        :rtype: str
        """
        return self._position_coordinate_y_type

    @position_coordinate_y_type.setter
    def position_coordinate_y_type(self, position_coordinate_y_type: str):
        """Sets the position_coordinate_y_type of this ObservationUnitStudy.

        The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See \"Location Coordinate Encoding\" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column   # noqa: E501

        :param position_coordinate_y_type: The position_coordinate_y_type of this ObservationUnitStudy.
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
        """Gets the replicate of this ObservationUnitStudy.

        The replicate number of an observation unit. May be the same as blockNumber.  # noqa: E501

        :return: The replicate of this ObservationUnitStudy.
        :rtype: str
        """
        return self._replicate

    @replicate.setter
    def replicate(self, replicate: str):
        """Sets the replicate of this ObservationUnitStudy.

        The replicate number of an observation unit. May be the same as blockNumber.  # noqa: E501

        :param replicate: The replicate of this ObservationUnitStudy.
        :type replicate: str
        """

        self._replicate = replicate
