from typing import List

import helper

VERSIONS_1_2 = ["1.2"]
VERSIONS_1_3 = ["1.3"]
VERSIONS_1_23 = VERSIONS_1_2 + VERSIONS_1_3
VERSIONS_2_0 = ["2.0"]

def search(datatype=None, dataType=None, pageSize=None, page=None):
    """
    Return a list of all calls that are implemented
    """

    # create the full list of all calls implemented.
    data = [
        calls_get_helper('calls', versions=VERSIONS_1_23),
        calls_get_helper('commoncropnames', versions=VERSIONS_1_23),
        calls_get_helper('crops', versions=VERSIONS_1_23),
        calls_get_helper('events', versions=VERSIONS_2_0),
        calls_get_helper('germplasm', versions=VERSIONS_1_3),
        calls_get_helper('locations', versions=VERSIONS_1_23),
        calls_get_helper('locations/{locationDbId}', versions=VERSIONS_1_23),
        calls_get_helper('observationunits', versions=VERSIONS_1_3),
        calls_get_helper('phenotypes-search', versions=VERSIONS_1_2),
        calls_get_helper('programs', versions=VERSIONS_1_23),
        calls_get_helper('seasons', versions=VERSIONS_1_23),
        calls_get_helper('studies', versions=VERSIONS_1_23),
        calls_get_helper('studies/{studyDbId}', versions=VERSIONS_1_23),
        calls_get_helper('studies/{studyDbId}/germplasm', versions=VERSIONS_1_23),
        calls_get_helper('studies/{studyDbId}/layouts', versions=VERSIONS_1_23),
        calls_get_helper('trials', versions=VERSIONS_1_23),
        calls_get_helper('variables', versions=VERSIONS_1_23),
        calls_get_helper('methods', versions=VERSIONS_1_23)
    ]

    # filter on datatype
    if dataType:
        data = [d for d in data if dataType in d['dataTypes']]
    elif datatype:
        data = [d for d in data if datatype in d['dataTypes']]

    # total number of rows
    count = len(data)

    # add a limit
    if not pageSize:
        pageSize = len(data)
    if not page:
        page = 0
    data = data[page * pageSize:(page + 1) * pageSize]

    # return the resulting data
    return helper.create_result({"data": data}, count, pageSize, page)


def calls_get_helper(api_call, dataTypes=None, methods=None, versions=None):
    """
    Helper function to return a brapi call information.
    """
    if not dataTypes:
        dataTypes = ["application/json"]
    if not methods:
        methods = ['GET']
    if not versions:
        versions = VERSIONS_1_23
    return {
        "call": api_call,
        "dataTypes": dataTypes,
        "methods": methods,
        "versions": versions
    }
