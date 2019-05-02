import json
import helper


def search(germplasmPUI=None, germplasmDbId=None, germplasmName=None, commonCropName=None, pageSize=None, page=None):

    # load all the data
    # TODO this does not work if pakcage is installed, need to use pkgutil
    filename = 'data/germplasm.json'
    data = json.load(open(filename, 'r'))

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

    nd = _flatten_data(data)

    # return the resulting data
    return helper.create_result({"data": nd}, count, pageSize, page)

def _flatten_data(data):
    if isinstance(data, list):
        if len(data) == 1:
            return data[0]
        else:
            return [_flatten_data(x) for x in data]
    if isinstance(data, dict):
        return {k: _flatten_data(v) for k, v in data.items()}
    return data

