import helper


def search(observationVariableDbId=None, traitClass=None, pageSize=None, page=None):
    """Returns information on variables
    Arguments:
        observationVariableDbId: specific variable to return information on
        traitClass: not implemented
        pageSize: the desired size of return pages
        page: the number of the page to return (starting at zero)
    """
    query = "SELECT id, name, units, min, max FROM variables AS v"

    params = []

    where_clause = " WHERE"

    # add a filter on the variable ID
    if observationVariableDbId:
        query += where_clause + " v.id = %s "
        params.append(observationVariableDbId)
        where_clause = " AND"

    # add a filter on the trait class  - not implemented at this time
    #if traitClass:
    # NOTE: this code is invalid for filtering on traitClass, it's just a placeholder
    #    query += where_clause + " s.id = %s "
    #    params.append(traitClass)
    #    where_clause = " AND"

    query += " ORDER BY id"

    # count first
    count = helper.query_count(query, params)

    # execute query
    result = helper.query_result(query, params, pageSize, page)

    # wrap result
    data = list()
    for row in result:
        data.append({
             "name": row["name"],
             "observationVariableDbName": row["name"],
             "observationVariableDbId": row["id"],
             "scale": {
                "name": row["units"],
                "validValues": {
                    "min": row["min"],
                    "max": row["max"]
                }
             }
        })

    return helper.create_result({"data": data}, count, pageSize, page)
