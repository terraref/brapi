from bety_brapi import helper
import connexion
app = connexion.App(__name__, specification_dir='./swagger/')


def common_crop_names_get(pageSize=None, page=None):

    query = "SELECT DISTINCT commonname FROM species ORDER BY commonname"
    count = helper.query_count(query)
    res = helper.query_result(query, [], pageSize, page)

    data = [r[0] for r in res]

    return helper.create_result({"data": data}, count, pageSize, page)

def crops_get(pageSize=None, page=None):
    # deprecated function name
    return common_crop_names_get(pageSize, page)
