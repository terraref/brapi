import helper

observation_names = [
    "collector",
    "observationDbId",
    "observationTimeStamp",
    "observationVariableDbId",
    "observationVariableName",
    "season",
    "value",
    "quality",
    "operator",
    "replicate"
]

treatment_names = [
    "factor",
    "modality"
]

names_map = {
    "observationvariabledbid": "observationVariableDbId",
    "observationvariablename": "observationVariableName",
    "observationunitdbid": "observationunitDbId",
    "observationdbid": "observationDbId",
    "observationtimestamp": "observationTimeStamp",
    "germplasmdbid": "germplasmDbId",
    "germplasmname": "germplasmName",
    "studydbid": "studyDbId",
    "observationtreatment": "observationTreatment",
    "treatmentdbid": "treatmentDbId",
    "observationunitname": "observationUnitName",
    "seasondbid": "seasonDbId"
}

def search(germplasmDbId=None, observationVariableDbId=None, studyDbId=None, locationDbId=None, trialDbId=None,
           programDbId=None, seasonDbId=None, observationUnitDbId=None,
           observationLevel=None, observationTimeStampRangeStart=None, observationTimeStampRangeEnd=None,
           pageSize=None, page=None):

    if observationTimeStampRangeStart:
        observationTimeStampRangeStart = deserialize_datetime(observationTimeStampRangeStart)

    if observationTimeStampRangeEnd:
        observationTimeStampRangeEnd = deserialize_datetime(observationTimeStampRangeEnd)

    query = """
select
  t.treatment_id :: text as treatmentDbId,
  t.site_id :: text as observationUnitDbId, 
  t.variable_id :: text as observationVariableDbId, 
  v.name as observationVariableName, 
  t.id :: text as observationDbId, 
  t.mean :: text as value, 
  t.date as observationTimeStamp, 
  s.sitename as observationUnitName, 
  t.cultivar_id :: text as germplasmDbId, 
  cv.name as germplasmName, 
  e.id :: text as studyDbId, 
  seasons.id :: text as seasonDbId, 
  tr.name as factor, 
  tr.definition as modality, 
  t.entity_id :: text as replicate, 
  c.author as operator, 
  t.checked as quality 
from 
  traits t 
  left join variables v on t.variable_id = v.id 
  left join sites s on t.site_id = s.id 
  left join treatments tr on t.treatment_id = tr.id 
  left join citations c on t.citation_id = c.id 
  left join cultivars cv on t.cultivar_id = cv.id 
  left join experiments_sites es on t.site_id = es.site_id 
  left join experiments_treatments et on t.treatment_id = et.treatment_id
  left join experiments e on es.experiment_id = e.id,
  (select distinct extract (year from start_date) as year, 
      LTRIM(RTRIM(SPLIT_PART(name, ': ', 1))) as season, 
      md5(LTRIM(RTRIM(SPLIT_PART(name, ': ', 1)))):: varchar(255) as id 
    from experiments) seasons 
where 
  t.treatment_id = tr.id
  and t.checked > -1 
  and t.access_level = 4 
  and seasons.season = LTRIM(RTRIM(SPLIT_PART(e.name, ': ', 1))) 
"""


    params = []

    if observationVariableDbId is not None:
        query += " and v.id = %s "
        params.append(observationVariableDbId)

    if locationDbId is not None:
        query += " and t.site_id = %s "
        params.append(locationDbId)

    if studyDbId is not None:
        query += " and e.id = %s "
        params.append(studyDbId)

    if germplasmDbId is not None:
        query += " and t.cultivar_id = %s "
        params.append(germplasmDbId)

    if seasonDbId is not None:
        query += " AND seasons.id = %s "
        params.append(seasonDbId)

    if observationUnitDbId is not None:
        query += " AND s.sitename = %s "
        params.append(observationUnitDbId)

    if (observationTimeStampRangeStart and observationTimeStampRangeEnd):
        query += " and (date >= %s and date <= %s) "
        params.append(observationTimeStampRangeStart)
        params.append(observationTimeStampRangeEnd)
    elif observationTimeStampRangeStart:
        query += " and date >= %s "
        params.append(observationTimeStampRangeStart)
    elif observationTimeStampRangeEnd:
        query += " and date <= %s "
        params.append(observationTimeStampRangeEnd)

    count = helper.query_count(query, params)
    res = helper.query_result(query, params, pageSize, page)
    data = _conform_data([dict(r) for r in res])

    if observationUnitDbId is not None:
        # Group observations together under the same ObservationUnit
        grouped_data = {}
        for obs in data:
            obs_name = obs["observationUnitName"]
            if obs_name not in grouped_data:
                grouped_data[obs_name] = obs
            else:
                grouped_data[obs_name]["observations"] += obs["observations"]
        final_data = []
        for obs_name in grouped_data:
            final_data.append(grouped_data[obs_name])
    else:
        final_data = data

    # split data if needed, remembering total number
    if not pageSize:
        pageSize = helper.DEFAULT_PAGE_SIZE
    if not page:
        page = 0

    return helper.create_result({"data": final_data}, count, pageSize, page)


def deserialize_datetime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
         return string

def _conform_data(data):
    if not isinstance(data, list):
        return data

    return [_conform_element(x) for x in data]

def _conform_element(ele):
    if not isinstance(ele, dict):
        return ele

    res_obs = {}
    res_treat = {}
    res = {}
    for k,v in ele.items():
        if k in names_map:
            k = names_map[k]

        if k in observation_names:
            if k == "quality":
                if v == 0:
                    res_obs[k] = "unchecked"
                elif v == 1:
                    res_obs[k] = "checked"
                else:
                    res_obs[k] = v
            else:
                res_obs[k] = v
        elif k in treatment_names:
            res_treat[k] = v
        else:
            res[k] = v

    if len(res_obs.keys()) > 0:
        res["observations"] = [res_obs]
    if len(res_treat.keys()) > 0:
        res["treatments"] = [res_treat]

    return res
