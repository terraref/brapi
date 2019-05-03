
from api.phenotypes import post

def search(germplasmDbId=None, observationVariableDbId=None, studyDbId=None, locationDbId=None, trialDbId=None, programDbId=None, seasonDbId=None, observationLevel=None, observationTimeStampRangeStart=None, observationTimeStampRangeEnd=None, pageSize=None, page=None):
    res = post(germplasmDbId, observationVariableDbId, studyDbId, locationDbId, trialDbId, programDbId, seasonDbId, observationLevel, observationTimeStampRangeStart, observationTimeStampRangeEnd, pageSize, page)

    return _replace_keynames(res)

keyname_map = {
    "observationtreatment": "treatment_definition",
    "season": "treatment_factor"
}

def _replace_keynames(data):

    if isinstance(data, list):
        return [_replace_keynames(x) for x in data]

    if isinstance(data, dict):
        return {_map_key(k): _replace_keynames(v) for k, v in data}

    return data

def _map_key(name):
    if name in keyname_map.keys():
        return keyname_map[name]
    return name
