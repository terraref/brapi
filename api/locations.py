import helper


def search(locationType=None, pageSize=None, page=None):
    """

    :param locationType:
    :param pageSize: number of elements to return
    :param page: which page to return
    :return: all locations in the page
    """

    # TODO map locationType to something
    params = list()

    # get all sitegroups and sites
    query = "SELECT sitegroups.id AS locationDbId, " \
            "       sitegroups.name AS name, " \
            "       sites.country AS countryCode, " \
            "       sites.geometry AS geometry " \
            "FROM sites, sitegroups, sitegroups_sites " \
            "WHERE sitegroups_sites.site_id = sites.id " \
            "      AND sitegroups_sites.sitegroup_id = sitegroups.id "
    # compute the bounding box
    query = "SELECT locationDbId, " \
            "       name, " \
            "       countryCode, " \
            "       ST_Extent(geometry) AS geometry " \
            "FROM (" + query + ") ss1 " \
            "GROUP BY locationDbId, name, countryCode "
    # compute center point
    query = "SELECT locationDbId::text, " \
            "       name, " \
            "       countryCode, " \
            "       ST_X(ST_CENTROID(geometry)) AS longitude, " \
            "       ST_Y(ST_CENTROID(geometry)) AS latitude, " \
            "       ST_Z(ST_CENTROID(geometry)) AS altitude " \
            "FROM (" + query + ") ss2"

    # order query
    query += "   ORDER BY locationDbId"

    # TODO add a filter on the locationType
    # if locationType:
    #     # wrap query in a sub select to allow us to use locationType in WHERE clause
    #     query = "SELECT * FROM (" + query + ") locations WHERE locationType = %s "
    #     params.append(locationType)

    # count first
    count = helper.query_count(query, params)

    # execute query
    results = helper.query_result(query, params, pageSize, page)

    # wrap result
    data = []
    for row in results:
        location = {k: v for k, v in row.items() if v}
        if 'countryCode' not in location:
            location['countryCode'] = location.pop('countrycode', '')
        if 'altitude' not in location:
            location['altitude'] = 0
        if 'locationDbId' not in location:
            location['locationDbId'] = location.pop('locationdbid', '')
        data.append(location)
    return helper.create_result({"data": data}, count, pageSize, page)


def get(locationDbId):
    """

    :param locationDbId:
    :return:
    """

    params = list()

    # get all sitegroups and sites
    query = "SELECT sitegroups.id AS locationDbId, " \
            "       sitegroups.name AS name, " \
            "       sites.geometry AS geometry " \
            "FROM sites, sitegroups, sitegroups_sites " \
            "WHERE sitegroups.id = %s " \
            "      AND sitegroups_sites.site_id = sites.id " \
            "      AND sitegroups_sites.sitegroup_id = sitegroups.id "
    params.append(int(locationDbId))
    # compute the bounding box
    query = "SELECT locationDbId, " \
            "       name, " \
            "       ST_Extent(geometry) AS geometry " \
            "FROM (" + query + ") ss1 " \
            "GROUP BY locationDbId, name "
    # compute center point
    query = "SELECT locationDbId::text, " \
            "       name, " \
            "       ST_X(ST_CENTROID(geometry)) AS longitude, " \
            "       ST_Y(ST_CENTROID(geometry)) AS latitude " \
            "FROM (" + query + ") ss2"

    # order query
    query += "   ORDER BY locationDbId"

    # count first
    count = helper.query_count(query, params)

    # execute query
    results = helper.query_result(query, params)

    # wrap result
    data = []
    for row in results:
        data.append({k: v for k, v in row.items() if v})
    return helper.create_result({"location": data}, count)
