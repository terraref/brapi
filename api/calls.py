import helper

VERSIONS_1_2 = ["1.2"]
VERSIONS_1_3 = ["1.3"]
VERSIONS_2_0 = ["2.0"]
VERSIONS_ALL = VERSIONS_1_2 + VERSIONS_1_3
VERSIONS_LATEST = VERSIONS_1_3


def search(datatype=None, dataType=None, pageSize=None, page=None):
    """
    Return a list of all calls that are implemented
    """

    # create the full list of all calls implemented.
    data = [
        calls_get_helper('calls'),
        calls_get_helper('commoncropnames'),
        calls_get_helper('crops'),
#        calls_get_helper('events', VERSIONS_2_0),
        calls_get_helper('germplasm', versions=VERSIONS_LATEST),
        calls_get_helper('locations'),
        calls_get_helper('locations/{locationDbId}'),
        calls_get_helper('observationunits', versions=VERSIONS_LATEST),
        calls_get_helper('phenotypes-search', versions=VERSIONS_1_2),
        calls_get_helper('programs'),
        calls_get_helper('seasons'),
        calls_get_helper('studies'),
        calls_get_helper('studies/{studyDbId}'),
        calls_get_helper('studies/{studyDbId}/germplasm'),
        calls_get_helper('studies/{studyDbId}/layouts'),
        calls_get_helper('trials')
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
        versions = VERSIONS_ALL
    return {
        "call": api_call,
        "dataTypes": dataTypes,
        "methods": methods,
        "versions": versions
    }
