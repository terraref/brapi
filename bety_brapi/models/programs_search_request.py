# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi import util


class ProgramsSearchRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, abbreviation: str=None, lead_person: str=None, name: str=None, objective: str=None, page: int=None, page_size: int=None, program_db_id: str=None, program_name: str=None):  # noqa: E501
        """ProgramsSearchRequest - a model defined in Swagger

        :param abbreviation: The abbreviation of this ProgramsSearchRequest.  # noqa: E501
        :type abbreviation: str
        :param lead_person: The lead_person of this ProgramsSearchRequest.  # noqa: E501
        :type lead_person: str
        :param name: The name of this ProgramsSearchRequest.  # noqa: E501
        :type name: str
        :param objective: The objective of this ProgramsSearchRequest.  # noqa: E501
        :type objective: str
        :param page: The page of this ProgramsSearchRequest.  # noqa: E501
        :type page: int
        :param page_size: The page_size of this ProgramsSearchRequest.  # noqa: E501
        :type page_size: int
        :param program_db_id: The program_db_id of this ProgramsSearchRequest.  # noqa: E501
        :type program_db_id: str
        :param program_name: The program_name of this ProgramsSearchRequest.  # noqa: E501
        :type program_name: str
        """
        self.swagger_types = {
            'abbreviation': str,
            'lead_person': str,
            'name': str,
            'objective': str,
            'page': int,
            'page_size': int,
            'program_db_id': str,
            'program_name': str
        }

        self.attribute_map = {
            'abbreviation': 'abbreviation',
            'lead_person': 'leadPerson',
            'name': 'name',
            'objective': 'objective',
            'page': 'page',
            'page_size': 'pageSize',
            'program_db_id': 'programDbId',
            'program_name': 'programName'
        }

        self._abbreviation = abbreviation
        self._lead_person = lead_person
        self._name = name
        self._objective = objective
        self._page = page
        self._page_size = page_size
        self._program_db_id = program_db_id
        self._program_name = program_name

    @classmethod
    def from_dict(cls, dikt) -> 'ProgramsSearchRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The programsSearchRequest of this ProgramsSearchRequest.  # noqa: E501
        :rtype: ProgramsSearchRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def abbreviation(self) -> str:
        """Gets the abbreviation of this ProgramsSearchRequest.

        An abbreviation of a program to search for  # noqa: E501

        :return: The abbreviation of this ProgramsSearchRequest.
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation: str):
        """Sets the abbreviation of this ProgramsSearchRequest.

        An abbreviation of a program to search for  # noqa: E501

        :param abbreviation: The abbreviation of this ProgramsSearchRequest.
        :type abbreviation: str
        """

        self._abbreviation = abbreviation

    @property
    def lead_person(self) -> str:
        """Gets the lead_person of this ProgramsSearchRequest.

        The name or identifier of the program leader to search for  # noqa: E501

        :return: The lead_person of this ProgramsSearchRequest.
        :rtype: str
        """
        return self._lead_person

    @lead_person.setter
    def lead_person(self, lead_person: str):
        """Sets the lead_person of this ProgramsSearchRequest.

        The name or identifier of the program leader to search for  # noqa: E501

        :param lead_person: The lead_person of this ProgramsSearchRequest.
        :type lead_person: str
        """

        self._lead_person = lead_person

    @property
    def name(self) -> str:
        """Gets the name of this ProgramsSearchRequest.

        DEPRECATED in v1.3 - Use \"programName\"  # noqa: E501

        :return: The name of this ProgramsSearchRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ProgramsSearchRequest.

        DEPRECATED in v1.3 - Use \"programName\"  # noqa: E501

        :param name: The name of this ProgramsSearchRequest.
        :type name: str
        """

        self._name = name

    @property
    def objective(self) -> str:
        """Gets the objective of this ProgramsSearchRequest.

        A program objective to search for  # noqa: E501

        :return: The objective of this ProgramsSearchRequest.
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective: str):
        """Sets the objective of this ProgramsSearchRequest.

        A program objective to search for  # noqa: E501

        :param objective: The objective of this ProgramsSearchRequest.
        :type objective: str
        """

        self._objective = objective

    @property
    def page(self) -> int:
        """Gets the page of this ProgramsSearchRequest.

        Which page of the \"data\" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.  # noqa: E501

        :return: The page of this ProgramsSearchRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page: int):
        """Sets the page of this ProgramsSearchRequest.

        Which page of the \"data\" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.  # noqa: E501

        :param page: The page of this ProgramsSearchRequest.
        :type page: int
        """

        self._page = page

    @property
    def page_size(self) -> int:
        """Gets the page_size of this ProgramsSearchRequest.

        The maximum number of items to return per page of the \"data\" array. Default is 1000.  # noqa: E501

        :return: The page_size of this ProgramsSearchRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int):
        """Sets the page_size of this ProgramsSearchRequest.

        The maximum number of items to return per page of the \"data\" array. Default is 1000.  # noqa: E501

        :param page_size: The page_size of this ProgramsSearchRequest.
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def program_db_id(self) -> str:
        """Gets the program_db_id of this ProgramsSearchRequest.

        A program identifier to search for  # noqa: E501

        :return: The program_db_id of this ProgramsSearchRequest.
        :rtype: str
        """
        return self._program_db_id

    @program_db_id.setter
    def program_db_id(self, program_db_id: str):
        """Sets the program_db_id of this ProgramsSearchRequest.

        A program identifier to search for  # noqa: E501

        :param program_db_id: The program_db_id of this ProgramsSearchRequest.
        :type program_db_id: str
        """

        self._program_db_id = program_db_id

    @property
    def program_name(self) -> str:
        """Gets the program_name of this ProgramsSearchRequest.

        A name of a program to search for  # noqa: E501

        :return: The program_name of this ProgramsSearchRequest.
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name: str):
        """Sets the program_name of this ProgramsSearchRequest.

        A name of a program to search for  # noqa: E501

        :param program_name: The program_name of this ProgramsSearchRequest.
        :type program_name: str
        """

        self._program_name = program_name
