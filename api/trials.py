import json

import helper
from api.programs import search as search_programs

trial_data = None

def search(programDbId=None, trialDbId=None, trialName=None, commonCropName=None, locationDbId=None,
           active=None, sortBy=None, sortOrder=None, pageSize=None, page=None):
    return get_result(dataonly=False,
                      programDbId=programDbId, trialDbId=trialDbId, trialName=trialName,
                      commonCropName=commonCropName, locationDbId=locationDbId, active=active,
                      sortBy=sortBy, sortOrder=sortOrder, pageSize=pageSize, page=page)

def get_result(dataonly=False,
               programDbId=None, trialDbId=None, trialName=None, commonCropName=None, locationDbId=None,
               active=None, sortBy=None, sortOrder=None, pageSize=None, page=None):

    if not trial_data:
        load_data()

    # load program data for commonCropName check
    programs = search_programs(commonCropName=commonCropName)["result"]["data"]

    def filter_func(x):
        if programDbId and x.get('programDbId', '') != programDbId:
            return False
        if trialDbId and x.get('trialDbId', '') != str(trialDbId):
            return False
        if trialName and x.get('trialName', '') != trialName:
            return False
        if commonCropName:
            found_ccn = False
            for p in programs:
                if (x.get('programDbId', '') == p.get('programDbId') and
                        p.get('commonCropName') == commonCropName):
                    found_ccn = True
            if not found_ccn:
                return False
        return True

    # TODO: How can this be filtered by locationDbId?
    # TODO: How can this be filtered by active?

    # filter the data
    data = list(filter(lambda x: filter_func(x), trial_data))

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
    global trial_data

    raw_data = json.load(open('data/trials.json', 'r'))
    trial_data = _ensure_arrays(_convert_strings(_flatten_data(_convert_types(raw_data))))

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
