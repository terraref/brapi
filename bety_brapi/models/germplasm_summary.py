# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from bety_brapi.models.base_model_ import Model
from bety_brapi.models.germplasm_donors import GermplasmDonors  # noqa: F401,E501
from bety_brapi.models.taxon_id import TaxonID  # noqa: F401,E501
from bety_brapi import util


class GermplasmSummary(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, accession_number: str=None, acquisition_date: date=None, biological_status_of_accession_code: int=None, breeding_method_db_id: str=None, common_crop_name: str=None, country_of_origin_code: str=None, default_display_name: str=None, donors: List[GermplasmDonors]=None, entry_number: str=None, genus: str=None, germplasm_db_id: str=None, germplasm_name: str=None, germplasm_pui: str=None, institute_code: str=None, institute_name: str=None, pedigree: str=None, seed_source: str=None, species: str=None, species_authority: str=None, subtaxa: str=None, subtaxa_authority: str=None, synonyms: List[str]=None, taxon_ids: List[TaxonID]=None, type_of_germplasm_storage_code: List[str]=None):  # noqa: E501
        """GermplasmSummary - a model defined in Swagger

        :param accession_number: The accession_number of this GermplasmSummary.  # noqa: E501
        :type accession_number: str
        :param acquisition_date: The acquisition_date of this GermplasmSummary.  # noqa: E501
        :type acquisition_date: date
        :param biological_status_of_accession_code: The biological_status_of_accession_code of this GermplasmSummary.  # noqa: E501
        :type biological_status_of_accession_code: int
        :param breeding_method_db_id: The breeding_method_db_id of this GermplasmSummary.  # noqa: E501
        :type breeding_method_db_id: str
        :param common_crop_name: The common_crop_name of this GermplasmSummary.  # noqa: E501
        :type common_crop_name: str
        :param country_of_origin_code: The country_of_origin_code of this GermplasmSummary.  # noqa: E501
        :type country_of_origin_code: str
        :param default_display_name: The default_display_name of this GermplasmSummary.  # noqa: E501
        :type default_display_name: str
        :param donors: The donors of this GermplasmSummary.  # noqa: E501
        :type donors: List[GermplasmDonors]
        :param entry_number: The entry_number of this GermplasmSummary.  # noqa: E501
        :type entry_number: str
        :param genus: The genus of this GermplasmSummary.  # noqa: E501
        :type genus: str
        :param germplasm_db_id: The germplasm_db_id of this GermplasmSummary.  # noqa: E501
        :type germplasm_db_id: str
        :param germplasm_name: The germplasm_name of this GermplasmSummary.  # noqa: E501
        :type germplasm_name: str
        :param germplasm_pui: The germplasm_pui of this GermplasmSummary.  # noqa: E501
        :type germplasm_pui: str
        :param institute_code: The institute_code of this GermplasmSummary.  # noqa: E501
        :type institute_code: str
        :param institute_name: The institute_name of this GermplasmSummary.  # noqa: E501
        :type institute_name: str
        :param pedigree: The pedigree of this GermplasmSummary.  # noqa: E501
        :type pedigree: str
        :param seed_source: The seed_source of this GermplasmSummary.  # noqa: E501
        :type seed_source: str
        :param species: The species of this GermplasmSummary.  # noqa: E501
        :type species: str
        :param species_authority: The species_authority of this GermplasmSummary.  # noqa: E501
        :type species_authority: str
        :param subtaxa: The subtaxa of this GermplasmSummary.  # noqa: E501
        :type subtaxa: str
        :param subtaxa_authority: The subtaxa_authority of this GermplasmSummary.  # noqa: E501
        :type subtaxa_authority: str
        :param synonyms: The synonyms of this GermplasmSummary.  # noqa: E501
        :type synonyms: List[str]
        :param taxon_ids: The taxon_ids of this GermplasmSummary.  # noqa: E501
        :type taxon_ids: List[TaxonID]
        :param type_of_germplasm_storage_code: The type_of_germplasm_storage_code of this GermplasmSummary.  # noqa: E501
        :type type_of_germplasm_storage_code: List[str]
        """
        self.swagger_types = {
            'accession_number': str,
            'acquisition_date': date,
            'biological_status_of_accession_code': int,
            'breeding_method_db_id': str,
            'common_crop_name': str,
            'country_of_origin_code': str,
            'default_display_name': str,
            'donors': List[GermplasmDonors],
            'entry_number': str,
            'genus': str,
            'germplasm_db_id': str,
            'germplasm_name': str,
            'germplasm_pui': str,
            'institute_code': str,
            'institute_name': str,
            'pedigree': str,
            'seed_source': str,
            'species': str,
            'species_authority': str,
            'subtaxa': str,
            'subtaxa_authority': str,
            'synonyms': List[str],
            'taxon_ids': List[TaxonID],
            'type_of_germplasm_storage_code': List[str]
        }

        self.attribute_map = {
            'accession_number': 'accessionNumber',
            'acquisition_date': 'acquisitionDate',
            'biological_status_of_accession_code': 'biologicalStatusOfAccessionCode',
            'breeding_method_db_id': 'breedingMethodDbId',
            'common_crop_name': 'commonCropName',
            'country_of_origin_code': 'countryOfOriginCode',
            'default_display_name': 'defaultDisplayName',
            'donors': 'donors',
            'entry_number': 'entryNumber',
            'genus': 'genus',
            'germplasm_db_id': 'germplasmDbId',
            'germplasm_name': 'germplasmName',
            'germplasm_pui': 'germplasmPUI',
            'institute_code': 'instituteCode',
            'institute_name': 'instituteName',
            'pedigree': 'pedigree',
            'seed_source': 'seedSource',
            'species': 'species',
            'species_authority': 'speciesAuthority',
            'subtaxa': 'subtaxa',
            'subtaxa_authority': 'subtaxaAuthority',
            'synonyms': 'synonyms',
            'taxon_ids': 'taxonIds',
            'type_of_germplasm_storage_code': 'typeOfGermplasmStorageCode'
        }

        self._accession_number = accession_number
        self._acquisition_date = acquisition_date
        self._biological_status_of_accession_code = biological_status_of_accession_code
        self._breeding_method_db_id = breeding_method_db_id
        self._common_crop_name = common_crop_name
        self._country_of_origin_code = country_of_origin_code
        self._default_display_name = default_display_name
        self._donors = donors
        self._entry_number = entry_number
        self._genus = genus
        self._germplasm_db_id = germplasm_db_id
        self._germplasm_name = germplasm_name
        self._germplasm_pui = germplasm_pui
        self._institute_code = institute_code
        self._institute_name = institute_name
        self._pedigree = pedigree
        self._seed_source = seed_source
        self._species = species
        self._species_authority = species_authority
        self._subtaxa = subtaxa
        self._subtaxa_authority = subtaxa_authority
        self._synonyms = synonyms
        self._taxon_ids = taxon_ids
        self._type_of_germplasm_storage_code = type_of_germplasm_storage_code

    @classmethod
    def from_dict(cls, dikt) -> 'GermplasmSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The germplasmSummary of this GermplasmSummary.  # noqa: E501
        :rtype: GermplasmSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accession_number(self) -> str:
        """Gets the accession_number of this GermplasmSummary.

        This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection  # noqa: E501

        :return: The accession_number of this GermplasmSummary.
        :rtype: str
        """
        return self._accession_number

    @accession_number.setter
    def accession_number(self, accession_number: str):
        """Sets the accession_number of this GermplasmSummary.

        This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection  # noqa: E501

        :param accession_number: The accession_number of this GermplasmSummary.
        :type accession_number: str
        """

        self._accession_number = accession_number

    @property
    def acquisition_date(self) -> date:
        """Gets the acquisition_date of this GermplasmSummary.

        The date this germplasm was aquired by the genebank (MCPD)  # noqa: E501

        :return: The acquisition_date of this GermplasmSummary.
        :rtype: date
        """
        return self._acquisition_date

    @acquisition_date.setter
    def acquisition_date(self, acquisition_date: date):
        """Sets the acquisition_date of this GermplasmSummary.

        The date this germplasm was aquired by the genebank (MCPD)  # noqa: E501

        :param acquisition_date: The acquisition_date of this GermplasmSummary.
        :type acquisition_date: date
        """

        self._acquisition_date = acquisition_date

    @property
    def biological_status_of_accession_code(self) -> int:
        """Gets the biological_status_of_accession_code of this GermplasmSummary.

        The 3 digit code representing the biological status of the accession (MCPD)  # noqa: E501

        :return: The biological_status_of_accession_code of this GermplasmSummary.
        :rtype: int
        """
        return self._biological_status_of_accession_code

    @biological_status_of_accession_code.setter
    def biological_status_of_accession_code(self, biological_status_of_accession_code: int):
        """Sets the biological_status_of_accession_code of this GermplasmSummary.

        The 3 digit code representing the biological status of the accession (MCPD)  # noqa: E501

        :param biological_status_of_accession_code: The biological_status_of_accession_code of this GermplasmSummary.
        :type biological_status_of_accession_code: int
        """

        self._biological_status_of_accession_code = biological_status_of_accession_code

    @property
    def breeding_method_db_id(self) -> str:
        """Gets the breeding_method_db_id of this GermplasmSummary.

        The unique identifier for the breeding method used to create this germplasm  # noqa: E501

        :return: The breeding_method_db_id of this GermplasmSummary.
        :rtype: str
        """
        return self._breeding_method_db_id

    @breeding_method_db_id.setter
    def breeding_method_db_id(self, breeding_method_db_id: str):
        """Sets the breeding_method_db_id of this GermplasmSummary.

        The unique identifier for the breeding method used to create this germplasm  # noqa: E501

        :param breeding_method_db_id: The breeding_method_db_id of this GermplasmSummary.
        :type breeding_method_db_id: str
        """

        self._breeding_method_db_id = breeding_method_db_id

    @property
    def common_crop_name(self) -> str:
        """Gets the common_crop_name of this GermplasmSummary.

        Common name for the crop (MCPD)  # noqa: E501

        :return: The common_crop_name of this GermplasmSummary.
        :rtype: str
        """
        return self._common_crop_name

    @common_crop_name.setter
    def common_crop_name(self, common_crop_name: str):
        """Sets the common_crop_name of this GermplasmSummary.

        Common name for the crop (MCPD)  # noqa: E501

        :param common_crop_name: The common_crop_name of this GermplasmSummary.
        :type common_crop_name: str
        """

        self._common_crop_name = common_crop_name

    @property
    def country_of_origin_code(self) -> str:
        """Gets the country_of_origin_code of this GermplasmSummary.

        3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)  # noqa: E501

        :return: The country_of_origin_code of this GermplasmSummary.
        :rtype: str
        """
        return self._country_of_origin_code

    @country_of_origin_code.setter
    def country_of_origin_code(self, country_of_origin_code: str):
        """Sets the country_of_origin_code of this GermplasmSummary.

        3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)  # noqa: E501

        :param country_of_origin_code: The country_of_origin_code of this GermplasmSummary.
        :type country_of_origin_code: str
        """

        self._country_of_origin_code = country_of_origin_code

    @property
    def default_display_name(self) -> str:
        """Gets the default_display_name of this GermplasmSummary.

        Human readable name used for display purposes  # noqa: E501

        :return: The default_display_name of this GermplasmSummary.
        :rtype: str
        """
        return self._default_display_name

    @default_display_name.setter
    def default_display_name(self, default_display_name: str):
        """Sets the default_display_name of this GermplasmSummary.

        Human readable name used for display purposes  # noqa: E501

        :param default_display_name: The default_display_name of this GermplasmSummary.
        :type default_display_name: str
        """

        self._default_display_name = default_display_name

    @property
    def donors(self) -> List[GermplasmDonors]:
        """Gets the donors of this GermplasmSummary.

        List of donor institutes (MCPD)  # noqa: E501

        :return: The donors of this GermplasmSummary.
        :rtype: List[GermplasmDonors]
        """
        return self._donors

    @donors.setter
    def donors(self, donors: List[GermplasmDonors]):
        """Sets the donors of this GermplasmSummary.

        List of donor institutes (MCPD)  # noqa: E501

        :param donors: The donors of this GermplasmSummary.
        :type donors: List[GermplasmDonors]
        """

        self._donors = donors

    @property
    def entry_number(self) -> str:
        """Gets the entry_number of this GermplasmSummary.

        ** Deprecated ** use /studies/{studyDbId/layout for positional germplasm relationships  # noqa: E501

        :return: The entry_number of this GermplasmSummary.
        :rtype: str
        """
        return self._entry_number

    @entry_number.setter
    def entry_number(self, entry_number: str):
        """Sets the entry_number of this GermplasmSummary.

        ** Deprecated ** use /studies/{studyDbId/layout for positional germplasm relationships  # noqa: E501

        :param entry_number: The entry_number of this GermplasmSummary.
        :type entry_number: str
        """

        self._entry_number = entry_number

    @property
    def genus(self) -> str:
        """Gets the genus of this GermplasmSummary.

        Genus name for taxon. Initial uppercase letter required. (MCPD)  # noqa: E501

        :return: The genus of this GermplasmSummary.
        :rtype: str
        """
        return self._genus

    @genus.setter
    def genus(self, genus: str):
        """Sets the genus of this GermplasmSummary.

        Genus name for taxon. Initial uppercase letter required. (MCPD)  # noqa: E501

        :param genus: The genus of this GermplasmSummary.
        :type genus: str
        """

        self._genus = genus

    @property
    def germplasm_db_id(self) -> str:
        """Gets the germplasm_db_id of this GermplasmSummary.

        The ID which uniquely identifies a germplasm within the given database server  # noqa: E501

        :return: The germplasm_db_id of this GermplasmSummary.
        :rtype: str
        """
        return self._germplasm_db_id

    @germplasm_db_id.setter
    def germplasm_db_id(self, germplasm_db_id: str):
        """Sets the germplasm_db_id of this GermplasmSummary.

        The ID which uniquely identifies a germplasm within the given database server  # noqa: E501

        :param germplasm_db_id: The germplasm_db_id of this GermplasmSummary.
        :type germplasm_db_id: str
        """

        self._germplasm_db_id = germplasm_db_id

    @property
    def germplasm_name(self) -> str:
        """Gets the germplasm_name of this GermplasmSummary.

        Name of the germplasm. It can be the prefered name and does not have to be unique.  # noqa: E501

        :return: The germplasm_name of this GermplasmSummary.
        :rtype: str
        """
        return self._germplasm_name

    @germplasm_name.setter
    def germplasm_name(self, germplasm_name: str):
        """Sets the germplasm_name of this GermplasmSummary.

        Name of the germplasm. It can be the prefered name and does not have to be unique.  # noqa: E501

        :param germplasm_name: The germplasm_name of this GermplasmSummary.
        :type germplasm_name: str
        """

        self._germplasm_name = germplasm_name

    @property
    def germplasm_pui(self) -> str:
        """Gets the germplasm_pui of this GermplasmSummary.

        The Permanent Unique Identifier which represents a germplasm  # noqa: E501

        :return: The germplasm_pui of this GermplasmSummary.
        :rtype: str
        """
        return self._germplasm_pui

    @germplasm_pui.setter
    def germplasm_pui(self, germplasm_pui: str):
        """Sets the germplasm_pui of this GermplasmSummary.

        The Permanent Unique Identifier which represents a germplasm  # noqa: E501

        :param germplasm_pui: The germplasm_pui of this GermplasmSummary.
        :type germplasm_pui: str
        """

        self._germplasm_pui = germplasm_pui

    @property
    def institute_code(self) -> str:
        """Gets the institute_code of this GermplasmSummary.

        The code for the Institute that has bred the material. (MCPD)  # noqa: E501

        :return: The institute_code of this GermplasmSummary.
        :rtype: str
        """
        return self._institute_code

    @institute_code.setter
    def institute_code(self, institute_code: str):
        """Sets the institute_code of this GermplasmSummary.

        The code for the Institute that has bred the material. (MCPD)  # noqa: E501

        :param institute_code: The institute_code of this GermplasmSummary.
        :type institute_code: str
        """

        self._institute_code = institute_code

    @property
    def institute_name(self) -> str:
        """Gets the institute_name of this GermplasmSummary.

        The name of the institution which bred the material (MCPD)  # noqa: E501

        :return: The institute_name of this GermplasmSummary.
        :rtype: str
        """
        return self._institute_name

    @institute_name.setter
    def institute_name(self, institute_name: str):
        """Sets the institute_name of this GermplasmSummary.

        The name of the institution which bred the material (MCPD)  # noqa: E501

        :param institute_name: The institute_name of this GermplasmSummary.
        :type institute_name: str
        """

        self._institute_name = institute_name

    @property
    def pedigree(self) -> str:
        """Gets the pedigree of this GermplasmSummary.

        The cross name and optional selection history.  # noqa: E501

        :return: The pedigree of this GermplasmSummary.
        :rtype: str
        """
        return self._pedigree

    @pedigree.setter
    def pedigree(self, pedigree: str):
        """Sets the pedigree of this GermplasmSummary.

        The cross name and optional selection history.  # noqa: E501

        :param pedigree: The pedigree of this GermplasmSummary.
        :type pedigree: str
        """

        self._pedigree = pedigree

    @property
    def seed_source(self) -> str:
        """Gets the seed_source of this GermplasmSummary.

        The source of the seed   # noqa: E501

        :return: The seed_source of this GermplasmSummary.
        :rtype: str
        """
        return self._seed_source

    @seed_source.setter
    def seed_source(self, seed_source: str):
        """Sets the seed_source of this GermplasmSummary.

        The source of the seed   # noqa: E501

        :param seed_source: The seed_source of this GermplasmSummary.
        :type seed_source: str
        """

        self._seed_source = seed_source

    @property
    def species(self) -> str:
        """Gets the species of this GermplasmSummary.

        Specific epithet portion of the scientific name in lowercase letters. (MCPD)  # noqa: E501

        :return: The species of this GermplasmSummary.
        :rtype: str
        """
        return self._species

    @species.setter
    def species(self, species: str):
        """Sets the species of this GermplasmSummary.

        Specific epithet portion of the scientific name in lowercase letters. (MCPD)  # noqa: E501

        :param species: The species of this GermplasmSummary.
        :type species: str
        """

        self._species = species

    @property
    def species_authority(self) -> str:
        """Gets the species_authority of this GermplasmSummary.

        The authority organization responsible for tracking and maintaining the species name (MCPD)  # noqa: E501

        :return: The species_authority of this GermplasmSummary.
        :rtype: str
        """
        return self._species_authority

    @species_authority.setter
    def species_authority(self, species_authority: str):
        """Sets the species_authority of this GermplasmSummary.

        The authority organization responsible for tracking and maintaining the species name (MCPD)  # noqa: E501

        :param species_authority: The species_authority of this GermplasmSummary.
        :type species_authority: str
        """

        self._species_authority = species_authority

    @property
    def subtaxa(self) -> str:
        """Gets the subtaxa of this GermplasmSummary.

        Subtaxon can be used to store any additional taxonomic identifier. (MCPD)  # noqa: E501

        :return: The subtaxa of this GermplasmSummary.
        :rtype: str
        """
        return self._subtaxa

    @subtaxa.setter
    def subtaxa(self, subtaxa: str):
        """Sets the subtaxa of this GermplasmSummary.

        Subtaxon can be used to store any additional taxonomic identifier. (MCPD)  # noqa: E501

        :param subtaxa: The subtaxa of this GermplasmSummary.
        :type subtaxa: str
        """

        self._subtaxa = subtaxa

    @property
    def subtaxa_authority(self) -> str:
        """Gets the subtaxa_authority of this GermplasmSummary.

         The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)  # noqa: E501

        :return: The subtaxa_authority of this GermplasmSummary.
        :rtype: str
        """
        return self._subtaxa_authority

    @subtaxa_authority.setter
    def subtaxa_authority(self, subtaxa_authority: str):
        """Sets the subtaxa_authority of this GermplasmSummary.

         The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)  # noqa: E501

        :param subtaxa_authority: The subtaxa_authority of this GermplasmSummary.
        :type subtaxa_authority: str
        """

        self._subtaxa_authority = subtaxa_authority

    @property
    def synonyms(self) -> List[str]:
        """Gets the synonyms of this GermplasmSummary.

        List of alternative names or IDs used to reference this germplasm  # noqa: E501

        :return: The synonyms of this GermplasmSummary.
        :rtype: List[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms: List[str]):
        """Sets the synonyms of this GermplasmSummary.

        List of alternative names or IDs used to reference this germplasm  # noqa: E501

        :param synonyms: The synonyms of this GermplasmSummary.
        :type synonyms: List[str]
        """

        self._synonyms = synonyms

    @property
    def taxon_ids(self) -> List[TaxonID]:
        """Gets the taxon_ids of this GermplasmSummary.

        The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as \"ncbiTaxon\" preferably with a purl. The rank of this ID should be species.  # noqa: E501

        :return: The taxon_ids of this GermplasmSummary.
        :rtype: List[TaxonID]
        """
        return self._taxon_ids

    @taxon_ids.setter
    def taxon_ids(self, taxon_ids: List[TaxonID]):
        """Sets the taxon_ids of this GermplasmSummary.

        The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as \"ncbiTaxon\" preferably with a purl. The rank of this ID should be species.  # noqa: E501

        :param taxon_ids: The taxon_ids of this GermplasmSummary.
        :type taxon_ids: List[TaxonID]
        """

        self._taxon_ids = taxon_ids

    @property
    def type_of_germplasm_storage_code(self) -> List[str]:
        """Gets the type_of_germplasm_storage_code of this GermplasmSummary.

        The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)  # noqa: E501

        :return: The type_of_germplasm_storage_code of this GermplasmSummary.
        :rtype: List[str]
        """
        return self._type_of_germplasm_storage_code

    @type_of_germplasm_storage_code.setter
    def type_of_germplasm_storage_code(self, type_of_germplasm_storage_code: List[str]):
        """Sets the type_of_germplasm_storage_code of this GermplasmSummary.

        The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)  # noqa: E501

        :param type_of_germplasm_storage_code: The type_of_germplasm_storage_code of this GermplasmSummary.
        :type type_of_germplasm_storage_code: List[str]
        """

        self._type_of_germplasm_storage_code = type_of_germplasm_storage_code
