import helper


def search(commonCropName=None, studyTypeDbId=None, programDbId=None, locationDbId=None, seasonDbId=None,
           trialDbId=None, studyDbId=None, active=None, sortBy=None, sortOrder=None, pageSize=None, page=None):
    """

    :param locationType:
    :param pageSize: number of elements to return
    :param page: which page to return
    :return: all locations in the page
    """

    # TODO map locationType to something
    params = list()

    query = "SELECT * FROM experiments"

    # location as [join locations schemas sitegroups_sites join sites join experiments_sites]

    # order query
    #query += "ORDER BY locationDbId"

    # TODO add a filter on the locationType
    # if locationType:
    #     # wrap query in a sub select to allow us to use locationType in WHERE clause
    #     query = "SELECT * FROM (" + query + ") locations WHERE locationType = %s "
    #     params.append(locationType)

    # count first
    count = helper.query_count(query, params)

    # execute query
    results = helper.query_result(query, params, pageSize, page)

    # get all sitegroups and sites
    # create temporary table studies (
    # select
    #   id as studyDbId,
    #   name as studyName,
    #   description as studyDescription,
    #   start_date as startDate,
    #   end_date as endDate
    #   design as statisticalDesign.description
    #  from experiments);

    # wrap result
    data = []
    for row in results:
        study = dict()
        study['studyDbId'] = str(row_pop(row, 'id', ''))
        study['studyName'] = row_pop(row, 'name', '')
        study['studyDescription'] = row_pop(row, 'description', '')
        study['startDate'] = row_pop(row, 'start_date', '')
        study['endDate'] = row_pop(row, 'end_date', '')
        study['statisticalDesign'] = {
            'description': row_pop(row, 'design', '')
        }
        data.append(study)
    return helper.create_result({"data": data}, count, pageSize, page)


def row_pop(row, key, dflt):
    if row.has_key(key):
        return row[key]
    else:
        return dflt
