import json

from bety_brapi import helper

def germplasm_search_get(germplasmPUI, germplasmDbId, germplasmName, commonCropName, pageSize, page):
    """
    Search for a specific germplasm. Right now this will use an external file to get all the information.
    :param germplasmPUI:
    :param germplasmDbId:
    :param germplasmName:
    :param commonCropName:
    :param pageSize:
    :param page:
    :return:
    """

    # load all the data
    # TODO this does not work if pakcage is installed, need to use pkgutil
    file = 'data/germplasm.json'
    data = json.load(open(file, 'r'))

    # filter the data
    if germplasmPUI:
        data = [x for x in data if x.get('germplasmPUI', '') == germplasmPUI]
    if germplasmDbId:
        data = [x for x in data if x.get('germplasmDbId', '') == int(germplasmDbId)]
    if germplasmName:
        data = [x for x in data if x.get('germplasmName', '') == germplasmName]
    if commonCropName:
        data = [x for x in data if x.get('commonCropName', '') == commonCropName]

    # split data if needed, remembering total number
    count = len(data)
    if not pageSize:
        pageSize = helper.DEFAULT_PAGE_SIZE
    if not page:
        page = 0
    data = data[page * pageSize:(page+1) * pageSize]

    # return the resulting data
    return helper.create_result({"data": data}, count, pageSize, page)
