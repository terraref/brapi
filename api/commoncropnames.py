import helper

def search(pageSize=None, page=None):

    query = "SELECT DISTINCT commonname FROM species ORDER BY commonname"
    count = helper.query_count(query)
    res = helper.query_result(query, [], pageSize, page)

    data = [r[0] for r in res]

    return helper.create_result({"data": data}, count, pageSize, page)
