import calendar

import helper


def search(seasonDbId=None, season=None, year=None, pageSize=None, page=None):
    """
    Return a list of all seasons. Right now this will return the seasons as the
    year and month of the startdate. The database-id that is returned will be of
    the format YYYYMM.
    :param year: filter the seasons on the yaer
    :param pageSize: number of elements to return
    :param page: which page to return
    :return: all seasons in the page
    """
    params = list()
    query = "select * from (with season_list as (select distinct extract(year from start_date) as year, " \
            "LTRIM(RTRIM(SPLIT_PART(name, ': ', 1))) as season from experiments) " \
            "select year, season, ROW_NUMBER () over (order by year, season) as id from season_list) seasons "

    # add a filter on the season ID
    if seasonDbId:
        query += " WHERE id = %s "
        params.append(int(seasonDbId))
    # add a filter on the year
    if year:
        if seasonDbId:
            query += " AND year = %s"
        else:
            query += " WHERE year = %s"
        params.append(year)
    if season:
        if year or seasonDbId:
            query += " AND season = %s"
        else:
            query += " WHERE season = %s"
        params.append(season)

    query += " ORDER BY id"

    # count first
    count = helper.query_count(query, params)

    # execute query
    result = helper.query_result(query, params, pageSize, page)

    # wrap result
    data = list()
    for row in result:
        data.append({
            "season": row["season"],
            "year": str(int(row["year"])),
            "seasonDbId": str(row["id"])
        })

    return helper.create_result({"data": data}, count, pageSize, page)
