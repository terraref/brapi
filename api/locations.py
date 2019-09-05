import helper


def search(locationType=None, pageSize=None, page=None):
    """

    :param locationType:
    :param pageSize: number of elements to return
    :param page: which page to return
    :return: all locations in the page
    """

    return query(locationType=locationType, pageSize=pageSize, page=page)


def get(locationDbId):
    data = query(single_row=True, locationDbId=locationDbId)
    return helper.create_result({"location": data}, 1)


def query(single_row=False, locationDbId=None, locationType=None, pageSize=None, page=None):
    """

    :param single_row: return a single row back, not wrapped
    :param locationDbId:
    :return:
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

    if locationDbId:
        query += "AND sitegroups.id = %s"
        params.append(locationDbId)

    # compute the bounding box
    query = "SELECT locationDbId, " \
            "       name, " \
            "       countryCode, " \
            "       ST_Extent(geometry) AS geometry " \
            "FROM (" + query + ") ss1 " \
            "GROUP BY locationDbId, name, countryCode "
    # compute center point
    query = "SELECT DISTINCT locationDbId::text, " \
            "       name, " \
            "       countryCode, " \
            "       ST_X(ST_CENTROID(geometry)) AS longitude, " \
            "       ST_Y(ST_CENTROID(geometry)) AS latitude, " \
            "       ST_Z(ST_CENTROID(geometry)) AS altitude " \
            "FROM (" + query + ") ss2"

    # order query
    query += " ORDER BY locationDbId"

    # count first
    if single_row:
        count = 1
    else:
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
        if single_row:
            break

    if single_row:
        if data:
            return data[0]
        return {}
    else:
        return helper.create_result({"data": data}, count, pageSize, page)
