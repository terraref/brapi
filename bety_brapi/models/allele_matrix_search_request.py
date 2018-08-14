# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class AlleleMatrixSearchRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, expand_homozygotes: bool=None, format: str=None, marker_db_id: List[str]=None, markerprofile_db_id: List[str]=None, matrix_db_id: List[str]=None, page: int=None, page_size: int=None, sep_phased: str=None, sep_unphased: str=None, unknown_string: str=None):  # noqa: E501
        """AlleleMatrixSearchRequest - a model defined in Swagger

        :param expand_homozygotes: The expand_homozygotes of this AlleleMatrixSearchRequest.  # noqa: E501
        :type expand_homozygotes: bool
        :param format: The format of this AlleleMatrixSearchRequest.  # noqa: E501
        :type format: str
        :param marker_db_id: The marker_db_id of this AlleleMatrixSearchRequest.  # noqa: E501
        :type marker_db_id: List[str]
        :param markerprofile_db_id: The markerprofile_db_id of this AlleleMatrixSearchRequest.  # noqa: E501
        :type markerprofile_db_id: List[str]
        :param matrix_db_id: The matrix_db_id of this AlleleMatrixSearchRequest.  # noqa: E501
        :type matrix_db_id: List[str]
        :param page: The page of this AlleleMatrixSearchRequest.  # noqa: E501
        :type page: int
        :param page_size: The page_size of this AlleleMatrixSearchRequest.  # noqa: E501
        :type page_size: int
        :param sep_phased: The sep_phased of this AlleleMatrixSearchRequest.  # noqa: E501
        :type sep_phased: str
        :param sep_unphased: The sep_unphased of this AlleleMatrixSearchRequest.  # noqa: E501
        :type sep_unphased: str
        :param unknown_string: The unknown_string of this AlleleMatrixSearchRequest.  # noqa: E501
        :type unknown_string: str
        """
        self.swagger_types = {
            'expand_homozygotes': bool,
            'format': str,
            'marker_db_id': List[str],
            'markerprofile_db_id': List[str],
            'matrix_db_id': List[str],
            'page': int,
            'page_size': int,
            'sep_phased': str,
            'sep_unphased': str,
            'unknown_string': str
        }

        self.attribute_map = {
            'expand_homozygotes': 'expandHomozygotes',
            'format': 'format',
            'marker_db_id': 'markerDbId',
            'markerprofile_db_id': 'markerprofileDbId',
            'matrix_db_id': 'matrixDbId',
            'page': 'page',
            'page_size': 'pageSize',
            'sep_phased': 'sepPhased',
            'sep_unphased': 'sepUnphased',
            'unknown_string': 'unknownString'
        }

        self._expand_homozygotes = expand_homozygotes
        self._format = format
        self._marker_db_id = marker_db_id
        self._markerprofile_db_id = markerprofile_db_id
        self._matrix_db_id = matrix_db_id
        self._page = page
        self._page_size = page_size
        self._sep_phased = sep_phased
        self._sep_unphased = sep_unphased
        self._unknown_string = unknown_string

    @classmethod
    def from_dict(cls, dikt) -> 'AlleleMatrixSearchRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The alleleMatrixSearchRequest of this AlleleMatrixSearchRequest.  # noqa: E501
        :rtype: AlleleMatrixSearchRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def expand_homozygotes(self) -> bool:
        """Gets the expand_homozygotes of this AlleleMatrixSearchRequest.

        Should homozygotes be expanded (true) or collapsed into a single occurence (false)  # noqa: E501

        :return: The expand_homozygotes of this AlleleMatrixSearchRequest.
        :rtype: bool
        """
        return self._expand_homozygotes

    @expand_homozygotes.setter
    def expand_homozygotes(self, expand_homozygotes: bool):
        """Sets the expand_homozygotes of this AlleleMatrixSearchRequest.

        Should homozygotes be expanded (true) or collapsed into a single occurence (false)  # noqa: E501

        :param expand_homozygotes: The expand_homozygotes of this AlleleMatrixSearchRequest.
        :type expand_homozygotes: bool
        """

        self._expand_homozygotes = expand_homozygotes

    @property
    def format(self) -> str:
        """Gets the format of this AlleleMatrixSearchRequest.

        The data format of the response data. ie \"json\", \"tsv\", etc  # noqa: E501

        :return: The format of this AlleleMatrixSearchRequest.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format: str):
        """Sets the format of this AlleleMatrixSearchRequest.

        The data format of the response data. ie \"json\", \"tsv\", etc  # noqa: E501

        :param format: The format of this AlleleMatrixSearchRequest.
        :type format: str
        """

        self._format = format

    @property
    def marker_db_id(self) -> List[str]:
        """Gets the marker_db_id of this AlleleMatrixSearchRequest.

        An ID which uniquely identifies a Marker  # noqa: E501

        :return: The marker_db_id of this AlleleMatrixSearchRequest.
        :rtype: List[str]
        """
        return self._marker_db_id

    @marker_db_id.setter
    def marker_db_id(self, marker_db_id: List[str]):
        """Sets the marker_db_id of this AlleleMatrixSearchRequest.

        An ID which uniquely identifies a Marker  # noqa: E501

        :param marker_db_id: The marker_db_id of this AlleleMatrixSearchRequest.
        :type marker_db_id: List[str]
        """

        self._marker_db_id = marker_db_id

    @property
    def markerprofile_db_id(self) -> List[str]:
        """Gets the markerprofile_db_id of this AlleleMatrixSearchRequest.

        An ID which uniquely identifies a Marker Profile  # noqa: E501

        :return: The markerprofile_db_id of this AlleleMatrixSearchRequest.
        :rtype: List[str]
        """
        return self._markerprofile_db_id

    @markerprofile_db_id.setter
    def markerprofile_db_id(self, markerprofile_db_id: List[str]):
        """Sets the markerprofile_db_id of this AlleleMatrixSearchRequest.

        An ID which uniquely identifies a Marker Profile  # noqa: E501

        :param markerprofile_db_id: The markerprofile_db_id of this AlleleMatrixSearchRequest.
        :type markerprofile_db_id: List[str]
        """

        self._markerprofile_db_id = markerprofile_db_id

    @property
    def matrix_db_id(self) -> List[str]:
        """Gets the matrix_db_id of this AlleleMatrixSearchRequest.

        An ID which uniquely identifies an Allele Matrix  # noqa: E501

        :return: The matrix_db_id of this AlleleMatrixSearchRequest.
        :rtype: List[str]
        """
        return self._matrix_db_id

    @matrix_db_id.setter
    def matrix_db_id(self, matrix_db_id: List[str]):
        """Sets the matrix_db_id of this AlleleMatrixSearchRequest.

        An ID which uniquely identifies an Allele Matrix  # noqa: E501

        :param matrix_db_id: The matrix_db_id of this AlleleMatrixSearchRequest.
        :type matrix_db_id: List[str]
        """

        self._matrix_db_id = matrix_db_id

    @property
    def page(self) -> int:
        """Gets the page of this AlleleMatrixSearchRequest.

        Which page of the \"data\" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.  # noqa: E501

        :return: The page of this AlleleMatrixSearchRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page: int):
        """Sets the page of this AlleleMatrixSearchRequest.

        Which page of the \"data\" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.  # noqa: E501

        :param page: The page of this AlleleMatrixSearchRequest.
        :type page: int
        """

        self._page = page

    @property
    def page_size(self) -> int:
        """Gets the page_size of this AlleleMatrixSearchRequest.

        The maximum number of items to return per page of the \"data\" array. Default is 1000.  # noqa: E501

        :return: The page_size of this AlleleMatrixSearchRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int):
        """Sets the page_size of this AlleleMatrixSearchRequest.

        The maximum number of items to return per page of the \"data\" array. Default is 1000.  # noqa: E501

        :param page_size: The page_size of this AlleleMatrixSearchRequest.
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def sep_phased(self) -> str:
        """Gets the sep_phased of this AlleleMatrixSearchRequest.

        The string to use as a separator for phased allele calls.  # noqa: E501

        :return: The sep_phased of this AlleleMatrixSearchRequest.
        :rtype: str
        """
        return self._sep_phased

    @sep_phased.setter
    def sep_phased(self, sep_phased: str):
        """Sets the sep_phased of this AlleleMatrixSearchRequest.

        The string to use as a separator for phased allele calls.  # noqa: E501

        :param sep_phased: The sep_phased of this AlleleMatrixSearchRequest.
        :type sep_phased: str
        """

        self._sep_phased = sep_phased

    @property
    def sep_unphased(self) -> str:
        """Gets the sep_unphased of this AlleleMatrixSearchRequest.

        The string to use as a separator for unphased allele calls.  # noqa: E501

        :return: The sep_unphased of this AlleleMatrixSearchRequest.
        :rtype: str
        """
        return self._sep_unphased

    @sep_unphased.setter
    def sep_unphased(self, sep_unphased: str):
        """Sets the sep_unphased of this AlleleMatrixSearchRequest.

        The string to use as a separator for unphased allele calls.  # noqa: E501

        :param sep_unphased: The sep_unphased of this AlleleMatrixSearchRequest.
        :type sep_unphased: str
        """

        self._sep_unphased = sep_unphased

    @property
    def unknown_string(self) -> str:
        """Gets the unknown_string of this AlleleMatrixSearchRequest.

        The string to use as a representation for missing data.  # noqa: E501

        :return: The unknown_string of this AlleleMatrixSearchRequest.
        :rtype: str
        """
        return self._unknown_string

    @unknown_string.setter
    def unknown_string(self, unknown_string: str):
        """Sets the unknown_string of this AlleleMatrixSearchRequest.

        The string to use as a representation for missing data.  # noqa: E501

        :param unknown_string: The unknown_string of this AlleleMatrixSearchRequest.
        :type unknown_string: str
        """

        self._unknown_string = unknown_string
