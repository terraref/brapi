import json
import logging

import helper

dict_to_array_names = ["seedSource"]
ensure_array_names = ["donors", "synonyms", "typeOfGermplasmStorageCode"]
int_to_str_names = ["germplasmDbId"]
str_to_int_names = ["biologicalStatusOfAccessionCode"]

germplasm_data = None


def search(germplasmPUI=None, germplasmDbId=None, germplasmName=None, commonCropName=None, pageSize=None, page=None):
    return get_result(dataonly=False, germplasmPUI=germplasmPUI, germplasmDbId=germplasmDbId,
                      germplasmName=germplasmName, commonCropName=commonCropName, pageSize=pageSize, page=page)


def get_result(dataonly=False,
               germplasmPUI=None, germplasmDbId=None, germplasmName=None, commonCropName=None,
               pageSize=None, page=None):

    if not germplasm_data:
        load_data()

    def filter_func(x):
        if germplasmPUI and x.get('germplasmPUI', '') != germplasmPUI:
            return False
        if germplasmDbId and x.get('germplasmDbId', '') != str(germplasmDbId):
            return False
        if germplasmName and x.get('germplasmName', '') != germplasmName:
            return False
        if commonCropName and x.get('commonCropName', '') != commonCropName:
            return False
        return True

    # filter the data
    data = list(filter(lambda x: filter_func(x), germplasm_data))

    # split data if needed, remembering total number
    count = len(data)
    if not pageSize:
        pageSize = helper.DEFAULT_PAGE_SIZE
    if not page:
        page = 0
    data = data[page * pageSize:(page+1) * pageSize]

    # return the resulting data
    if dataonly:
        return data
    else:
        return helper.create_result({"data": data}, count, pageSize, page)


def load_data():
    global germplasm_data

    raw_data = json.load(open('data/germplasm.json', 'r'))
    germplasm_data = _ensure_arrays(_convert_strings(_flatten_data(_convert_types(raw_data))))


def _convert_types(data):
    if isinstance(data, list):
        return [_convert_types(x) for x in data]
    if isinstance(data, dict):
        return {k: _convert_types(v) if not isinstance(v, dict) or not k in dict_to_array_names else \
                        [_convert_types(j) for _, j in v.items()] \
            for k, v in data.items()}
            
    return data


def _flatten_data(data):
    if isinstance(data, list):
        if len(data) == 0:
            return None
        elif len(data) == 1:
            return _flatten_data(data[0])
        else:
            return [_flatten_data(x) for x in data]
    if isinstance(data, dict):
        return {k: _flatten_data(v) for k, v in data.items()}
    return data


def _convert_strings(data):
    if isinstance(data, list):
        return [_convert_strings(x) for x in data]
    if isinstance(data, dict):
        return {k: \
              _make_int(v) if k  in str_to_int_names else \
              str(v) if k in int_to_str_names else \
              _convert_strings(v) for k, v in data.items()}

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

