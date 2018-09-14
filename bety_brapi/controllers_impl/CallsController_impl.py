from bety_brapi import helper

VERSIONS_ALL = ["1.0", "1.1", "1.2"]
VERSIONS_LATEST = ["1.2"]


def calls_get(datatype, pageSize, page):
    """
    Return a list of all calls that are implemented
    """

    # create the full list of all calls implemented.
    data = [
        calls_get_helper('calls'),
        calls_get_helper('commonCropNames', versions=['1.2']),
        calls_get_helper('crops'),
        calls_get_helper('germplasm-search'),
        calls_get_helper('locations'),
        calls_get_helper('locations/{locationDbId}'),
        calls_get_helper('phenotypes-search'),
        calls_get_helper('seasons')
    ]

    # filter on datatype
    if datatype:
        data = [d for d in data if datatype in d['datatypes']]

    # total number of rows
    count = len(data)

    # add a limit
    if not pageSize:
        pageSize = len(data)
    if not page:
        page = 0
    data = data[page * pageSize:(page+1) * pageSize]

    # return the resulting data
    return helper.create_result({"data": data}, count, pageSize, page)


def calls_get_helper(api_call, datatypes=None, methods=None, versions=None):
    """
    Helper function to return a brapi call information.
    """
    if not datatypes:
        datatypes = ["json"]
    if not methods:
        methods = ['GET']
    if not versions:
        versions = VERSIONS_ALL
    return {
            "call": api_call,
            "datatypes": datatypes,
            "methods": methods,
            "versions": versions
        }
