import calendar

import helper


def search(year=None, pageSize=None, page=None):
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
    query = "SELECT DISTINCT extract(month from start_date) as month," \
            "                extract(year from start_date) as year" \
            "   FROM experiments "

    # add a filter on the year
    if year:
        query += "   WHERE extract(year from start_date) = %s"
        params.append(year)

    query += "   ORDER BY year, month"

    # count first
    count = helper.query_count(query, params)

    # execute query
    result = helper.query_result(query, params, pageSize, page)

    # wrap result
    data = list()
    for row in result:
        data.append({
            "season": calendar.month_name[int(row["month"])],
            "year": str(int(row["year"])),
            "seasonDbId": "%04d%02d" % (row["year"], row["month"])
        })

    return helper.create_result({"data": data}, count, pageSize, page)
