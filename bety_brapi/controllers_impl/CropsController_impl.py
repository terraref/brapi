from bety_brapi import database
from flask import jsonify
from flask import current_app as app

def common_crop_names_get(pageSize=None, page=None):

    query = "select distinct commonname from species"
    res = database.get_engine().execute(query)

    data = [r[0] for r in res]

    response = {
        "metadata": {
            "datafiles": [],
            "pagination": {
                "currentPage": 0,
                "pageSize": 100,
                "totalCount": 2,
                "totalPages": 1
            },
            "status": []
        },
        "result": {
            "data": data
            }
        }

    return response

def crops_get(pageSize=None, page=None):
    # deprecated function name
    return common_crop_names_get(pageSize=None, page=None)
