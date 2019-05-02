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

    nd = _ensure_arrays(_convert_to_string(_flatten_data(data)))

    # return the resulting data
    return helper.create_result({"data": nd}, count, pageSize, page)

no_flatten_names = []
ensure_array_names = ["donors", "synonyms"]
int_to_str_names = ["germplasmDbId", "typeOfGermplasmStorageCode"]
str_to_int_names = ["biologicalStatusOfAccessionCode"]

def _flatten_data(data):
    if isinstance(data, list):
        if len(data) == 1:
            return _flatten_data(data[0])
        else:
            return [_flatten_data(x) for x in data]
    if isinstance(data, dict):
        return {k: _flatten_data(v) for k, v in data.items()}
    return data

def _convert_to_string(data):
    if isinstance(data, list):
        return [_convert_to_string(x) for x in data]
    if isinstance(data, dict):
        return {k: \
              _convert_to_string(v) if not k in int_to_str_names else \
              str(v) if not k in str_to_int_names else \
              _make_int(v) for k, v in data.items()}

    if isinstance(data, int):
        return str(data)

    return data

def _ensure_arrays(data):
    if isinstance(data, list):
        return [_ensure_arrays(x) for x in data]
    if isinstance(data, dict):
        return {k: v if not k in ensure_array_names or v is None or isinstance(v, list) else [v] for k, v in data.items()}
    return data

def _make_int(data):
    if data is None:
        return None
    if isinstance(data, int):
        return data

    try:
         return int(data)
    except Exception as ex:
        pass

    return data

