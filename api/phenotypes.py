
import helper

def post(germplasmDbId=None, observationVariableDbId=None, studyDbId=None, locationDbId=None, trialDbId=None, programDbId=None, seasonDbId=None, observationLevel=None, observationTimeStampRangeStart=None, observationTimeStampRangeEnd=None, pageSize=None, page=None):

    if observationTimeStampRangeStart:
        observationTimeStampRangeStart = deserialize_datetime(observationTimeStampRangeStart)

    if observationTimeStampRangeEnd:
        observationTimeStampRangeEnd = deserialize_datetime(observationTimeStampRangeEnd)


    params = []
    query = "select v.id as observationVariableDbId,  \
                    v.name as observationVariableName,  \
                    t.id as observationDbId, \
                    t.mean as value, \
                    t.date as observationTimeStamp, \
                    s.sitename as location_abbreviation, \
                    es.experiment_id as studyDbId, \
                    et.treatment_id as treatments, \
                    treatments.name as season, \
                    treatments.definition as observationtreatment \
             from traits t, variables v, sites s, experiments_sites es, experiments_treatments et, treatments treatments  \
             where v.id = t.variable_id \
             and t.site_id = s.id \
             and es.site_id = t.site_id \
             and et.experiment_id = es.experiment_id \
             and treatments.id=et.treatment_id"

    # For not, observationVariable is variable
    # e.g.,  6000000007 plant_height 
    if observationVariableDbId:
        query += " and v.id = %s "
        params.append(observationVariableDbId)

    # For now, location is site
    if locationDbId:
        query += " and t.site_id = %s "
        params.append(locationDbId)

    if studyDbId:
        query += " and es.experiment_id = %s "
        params.append(studyDbId)

    # For now, germplasm is cultivar
    if germplasmDbId:
        query += " and t.cultivar_id = %s "
        params.append(germplasmDbId)

    if (observationTimeStampRangeStart and observationTimeStampRangeEnd):
        query += " and (date >= %s and date <= %s)"
        params.append(observationTimeStampRangeStart)
        params.append(observationTimeStampRangeEnd)
    elif observationTimeStampRangeStart:
        query += " and date >= %s"
        params.append(observationTimeStampRangeStart)
    elif observationTimeStampRangeEnd:
        query += " and date <= %s"
        params.append(observationTimeStampRangeEnd)

    if not pageSize:
        pageSize = helper.DEFAULT_PAGE_SIZE
    if not page:
        page = 0

    count = helper.query_count(query, params)
    res = helper.query_result(query, params, pageSize, page)
    data = {"observations": [dict(r) for r in res]}

    return helper.create_result({"data": data}, count, pageSize, page)


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


