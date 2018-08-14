# coding: utf-8

# flake8: noqa
from __future__ import absolute_import
# import models into model package
from bety_brapi.models.allele_matrix_details import AlleleMatrixDetails
from bety_brapi.models.allele_matrix_details_response import AlleleMatrixDetailsResponse
from bety_brapi.models.allele_matrix_search_request import AlleleMatrixSearchRequest
from bety_brapi.models.allele_matrix_values import AlleleMatrixValues
from bety_brapi.models.allele_matrix_values_response import AlleleMatrixValuesResponse
from bety_brapi.models.body import Body
from bety_brapi.models.body1 import Body1
from bety_brapi.models.breeding_method import BreedingMethod
from bety_brapi.models.breeding_method_response import BreedingMethodResponse
from bety_brapi.models.breeding_methods_response import BreedingMethodsResponse
from bety_brapi.models.breeding_methods_response_result import BreedingMethodsResponseResult
from bety_brapi.models.call import Call
from bety_brapi.models.calls_response import CallsResponse
from bety_brapi.models.calls_response_result import CallsResponseResult
from bety_brapi.models.common_crop_names_response import CommonCropNamesResponse
from bety_brapi.models.common_crop_names_response_result import CommonCropNamesResponseResult
from bety_brapi.models.contact import Contact
from bety_brapi.models.data_link import DataLink
from bety_brapi.models.data_types_response import DataTypesResponse
from bety_brapi.models.data_types_response_result import DataTypesResponseResult
from bety_brapi.models.genome_map import GenomeMap
from bety_brapi.models.genome_maps_response import GenomeMapsResponse
from bety_brapi.models.genome_maps_response_result import GenomeMapsResponseResult
from bety_brapi.models.germplasm import Germplasm
from bety_brapi.models.germplasm_attribute import GermplasmAttribute
from bety_brapi.models.germplasm_attribute_categories_response import GermplasmAttributeCategoriesResponse
from bety_brapi.models.germplasm_attribute_categories_response_result import GermplasmAttributeCategoriesResponseResult
from bety_brapi.models.germplasm_attribute_category import GermplasmAttributeCategory
from bety_brapi.models.germplasm_attribute_def import GermplasmAttributeDef
from bety_brapi.models.germplasm_attribute_defs_response import GermplasmAttributeDefsResponse
from bety_brapi.models.germplasm_attribute_defs_response_result import GermplasmAttributeDefsResponseResult
from bety_brapi.models.germplasm_attribute_list import GermplasmAttributeList
from bety_brapi.models.germplasm_attribute_list_response import GermplasmAttributeListResponse
from bety_brapi.models.germplasm_donors import GermplasmDonors
from bety_brapi.models.germplasm_markerprofiles_list import GermplasmMarkerprofilesList
from bety_brapi.models.germplasm_markerprofiles_list_response import GermplasmMarkerprofilesListResponse
from bety_brapi.models.germplasm_response import GermplasmResponse
from bety_brapi.models.germplasm_response1 import GermplasmResponse1
from bety_brapi.models.germplasm_response_result import GermplasmResponseResult
from bety_brapi.models.germplasm_search_request import GermplasmSearchRequest
from bety_brapi.models.germplasm_summary import GermplasmSummary
from bety_brapi.models.germplasm_summary_list import GermplasmSummaryList
from bety_brapi.models.germplasm_summary_list_response import GermplasmSummaryListResponse
from bety_brapi.models.linkage_group import LinkageGroup
from bety_brapi.models.location import Location
from bety_brapi.models.location_response import LocationResponse
from bety_brapi.models.locations_response import LocationsResponse
from bety_brapi.models.locations_response_result import LocationsResponseResult
from bety_brapi.models.map_details import MapDetails
from bety_brapi.models.map_details_response import MapDetailsResponse
from bety_brapi.models.marker import Marker
from bety_brapi.models.marker_profile import MarkerProfile
from bety_brapi.models.marker_profile_description import MarkerProfileDescription
from bety_brapi.models.marker_profile_descriptions_response import MarkerProfileDescriptionsResponse
from bety_brapi.models.marker_profile_descriptions_response_result import MarkerProfileDescriptionsResponseResult
from bety_brapi.models.marker_profiles_response import MarkerProfilesResponse
from bety_brapi.models.marker_response import MarkerResponse
from bety_brapi.models.marker_summary_linkage_group import MarkerSummaryLinkageGroup
from bety_brapi.models.marker_summary_map import MarkerSummaryMap
from bety_brapi.models.markers_response import MarkersResponse
from bety_brapi.models.markers_response1 import MarkersResponse1
from bety_brapi.models.markers_response1_result import MarkersResponse1Result
from bety_brapi.models.markers_response2 import MarkersResponse2
from bety_brapi.models.markers_response2_result import MarkersResponse2Result
from bety_brapi.models.markers_response_result import MarkersResponseResult
from bety_brapi.models.markers_search_request import MarkersSearchRequest
from bety_brapi.models.metadata import Metadata
from bety_brapi.models.metadata_pagination import MetadataPagination
from bety_brapi.models.method import Method
from bety_brapi.models.new_observation_db_ids import NewObservationDbIds
from bety_brapi.models.new_observation_db_ids_observations import NewObservationDbIdsObservations
from bety_brapi.models.new_observation_db_ids_response import NewObservationDbIdsResponse
from bety_brapi.models.new_observation_unit_db_ids import NewObservationUnitDbIds
from bety_brapi.models.new_observation_unit_db_ids_response import NewObservationUnitDbIdsResponse
from bety_brapi.models.new_observation_unit_request import NewObservationUnitRequest
from bety_brapi.models.new_observations_request import NewObservationsRequest
from bety_brapi.models.new_observations_request_deprecated import NewObservationsRequestDeprecated
from bety_brapi.models.new_observations_request_deprecated_data import NewObservationsRequestDeprecatedData
from bety_brapi.models.new_observations_request_observations import NewObservationsRequestObservations
from bety_brapi.models.new_observations_request_wrapper_deprecated import NewObservationsRequestWrapperDeprecated
from bety_brapi.models.new_observations_table_request import NewObservationsTableRequest
from bety_brapi.models.new_sample_db_id import NewSampleDbId
from bety_brapi.models.new_sample_db_id_result import NewSampleDbIdResult
from bety_brapi.models.observation import Observation
from bety_brapi.models.observation_levels_response import ObservationLevelsResponse
from bety_brapi.models.observation_levels_response_result import ObservationLevelsResponseResult
from bety_brapi.models.observation_summary import ObservationSummary
from bety_brapi.models.observation_summary_phenotype import ObservationSummaryPhenotype
from bety_brapi.models.observation_treatment import ObservationTreatment
from bety_brapi.models.observation_unit import ObservationUnit
from bety_brapi.models.observation_unit_phenotype import ObservationUnitPhenotype
from bety_brapi.models.observation_unit_position import ObservationUnitPosition
from bety_brapi.models.observation_unit_positions_response import ObservationUnitPositionsResponse
from bety_brapi.models.observation_unit_positions_response_result import ObservationUnitPositionsResponseResult
from bety_brapi.models.observation_unit_study import ObservationUnitStudy
from bety_brapi.models.observation_unit_xref import ObservationUnitXref
from bety_brapi.models.observation_units_response import ObservationUnitsResponse
from bety_brapi.models.observation_units_response1 import ObservationUnitsResponse1
from bety_brapi.models.observation_units_response1_result import ObservationUnitsResponse1Result
from bety_brapi.models.observation_units_response_result import ObservationUnitsResponseResult
from bety_brapi.models.observation_units_table_response import ObservationUnitsTableResponse
from bety_brapi.models.observation_units_table_response1 import ObservationUnitsTableResponse1
from bety_brapi.models.observation_variable import ObservationVariable
from bety_brapi.models.observation_variable_response import ObservationVariableResponse
from bety_brapi.models.observation_variable_search_request import ObservationVariableSearchRequest
from bety_brapi.models.observation_variables_response import ObservationVariablesResponse
from bety_brapi.models.observation_variables_response_result import ObservationVariablesResponseResult
from bety_brapi.models.observations_response import ObservationsResponse
from bety_brapi.models.observations_response_result import ObservationsResponseResult
from bety_brapi.models.observations_table import ObservationsTable
from bety_brapi.models.ontologies_response import OntologiesResponse
from bety_brapi.models.ontologies_response_result import OntologiesResponseResult
from bety_brapi.models.ontology import Ontology
from bety_brapi.models.pedigree import Pedigree
from bety_brapi.models.pedigree_response import PedigreeResponse
from bety_brapi.models.pedigree_siblings import PedigreeSiblings
from bety_brapi.models.phenotypes_request import PhenotypesRequest
from bety_brapi.models.phenotypes_request_data import PhenotypesRequestData
from bety_brapi.models.phenotypes_request_observation import PhenotypesRequestObservation
from bety_brapi.models.phenotypes_search_request import PhenotypesSearchRequest
from bety_brapi.models.progeny import Progeny
from bety_brapi.models.progeny_progeny import ProgenyProgeny
from bety_brapi.models.progeny_response import ProgenyResponse
from bety_brapi.models.program import Program
from bety_brapi.models.programs_response import ProgramsResponse
from bety_brapi.models.programs_response_result import ProgramsResponseResult
from bety_brapi.models.programs_search_request import ProgramsSearchRequest
from bety_brapi.models.sample import Sample
from bety_brapi.models.sample_response import SampleResponse
from bety_brapi.models.sample_search_request import SampleSearchRequest
from bety_brapi.models.samples_response import SamplesResponse
from bety_brapi.models.samples_response_result import SamplesResponseResult
from bety_brapi.models.scale import Scale
from bety_brapi.models.season import Season
from bety_brapi.models.seasons_response import SeasonsResponse
from bety_brapi.models.seasons_response_result import SeasonsResponseResult
from bety_brapi.models.status import Status
from bety_brapi.models.studies_response import StudiesResponse
from bety_brapi.models.studies_response_result import StudiesResponseResult
from bety_brapi.models.study import Study
from bety_brapi.models.study_last_update import StudyLastUpdate
from bety_brapi.models.study_layout_request import StudyLayoutRequest
from bety_brapi.models.study_layout_request_layout import StudyLayoutRequestLayout
from bety_brapi.models.study_observation_variables_response import StudyObservationVariablesResponse
from bety_brapi.models.study_observation_variables_response_result import StudyObservationVariablesResponseResult
from bety_brapi.models.study_response import StudyResponse
from bety_brapi.models.study_search_request import StudySearchRequest
from bety_brapi.models.study_summary import StudySummary
from bety_brapi.models.study_type import StudyType
from bety_brapi.models.study_types_response import StudyTypesResponse
from bety_brapi.models.study_types_response_result import StudyTypesResponseResult
from bety_brapi.models.studyobservations_table_response import StudyobservationsTableResponse
from bety_brapi.models.taxon_id import TaxonID
from bety_brapi.models.trait import Trait
from bety_brapi.models.trait_response import TraitResponse
from bety_brapi.models.trait_summary import TraitSummary
from bety_brapi.models.traits_response import TraitsResponse
from bety_brapi.models.traits_response_result import TraitsResponseResult
from bety_brapi.models.trial import Trial
from bety_brapi.models.trial_dataset_authorship import TrialDatasetAuthorship
from bety_brapi.models.trial_response import TrialResponse
from bety_brapi.models.trial_studies import TrialStudies
from bety_brapi.models.trial_summary import TrialSummary
from bety_brapi.models.trials_response import TrialsResponse
from bety_brapi.models.trials_response_result import TrialsResponseResult
from bety_brapi.models.valid_values import ValidValues
from bety_brapi.models.vendor_plate import VendorPlate
from bety_brapi.models.vendor_plate_file import VendorPlateFile
from bety_brapi.models.vendor_plate_request import VendorPlateRequest
from bety_brapi.models.vendor_plate_request_plates import VendorPlateRequestPlates
from bety_brapi.models.vendor_plate_request_samples import VendorPlateRequestSamples
from bety_brapi.models.vendor_plate_response import VendorPlateResponse
from bety_brapi.models.vendor_plate_search_request import VendorPlateSearchRequest
from bety_brapi.models.vendor_plates_response import VendorPlatesResponse
from bety_brapi.models.vendor_plates_response1 import VendorPlatesResponse1
from bety_brapi.models.vendor_plates_response1_result import VendorPlatesResponse1Result
from bety_brapi.models.vendor_plates_response_result import VendorPlatesResponseResult
from bety_brapi.models.vendor_sample import VendorSample
from bety_brapi.models.vendor_specification import VendorSpecification
from bety_brapi.models.vendor_specification_platform import VendorSpecificationPlatform
from bety_brapi.models.vendor_specification_platform_deliverables import VendorSpecificationPlatformDeliverables
from bety_brapi.models.vendor_specification_platform_statuses import VendorSpecificationPlatformStatuses
from bety_brapi.models.vendor_specification_reference_system import VendorSpecificationReferenceSystem
from bety_brapi.models.vendor_specification_response import VendorSpecificationResponse
from bety_brapi.models.vendor_specification_standard_requirement import VendorSpecificationStandardRequirement
from bety_brapi.models.vendor_specification_standard_requirement_blank_well_position import VendorSpecificationStandardRequirementBlankWellPosition
