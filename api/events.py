import json

import helper

events_data = None

def load_data():
    global germplasm_data

    raw_data = json.load(open('data/events.json', 'r'))
    events_data = _ensure_arrays(_convert_strings(_flatten_data(_convert_types(raw_data))))

def search(studyDbId=None, observationUnitDbId=None, eventDbId=None, eventType=None, dateRangeStart=None,
           dateRangeEnd=None, pageSize=None, page=None):
    return get_result(dataonly=False, studyDbId=None, observationUnitDbId=None, eventDbId=None, eventType=None, dateRangeStart=None,
           dateRangeEnd=None, pageSize=None, page=None)


def get_result(dataonly=False,
               studyDbId=None, observationUnitDbId=None, eventDbId=None, eventType=None, dateRangeStart=None,
               dateRangeEnd=None, pageSize=None, page=None):
    if not cultivar_data:
        load_data()
    else:
        pass

    query = "WITH event_parameters as ( select " \
            "m.id as id, array_agg(array[m.level::text, m.units, null]) as events " \
            "from managements m " \
            "where " \
            "m.id in (select m.id from experiments ex join experiments_treatments et on ex.id = et.experiment_id " \
            "join treatments t on et.treatment_id = t.id " \
            "join managements_treatments mt on t.id = mt.treatment_id " \
            "join managements m on mt.management_id = m.id) " \
            "group by m.id) " \
            "select DISTINCT" \
            "  m.date as date," \
            "  m.id::text as eventDbId," \
            "  m.mgmttype as eventType," \
            "  m.notes as eventDescription, " \
            "  array_agg(s.id::text) as observationUnitDbIds, " \
            "  ex.id::text as studyDbId," \
            "  ev.events as events " \
            "from" \
            "  experiments ex" \
            "  join experiments_treatments et on ex.id = et.experiment_id" \
            "  join treatments t on et.treatment_id = t.id" \
            "  join managements_treatments mt on t.id = mt.treatment_id" \
            "  join managements m on mt.management_id = m.id" \
            "  join experiments_sites es on ex.id = es.experiment_id" \
            "  join sites s on es.site_id = s.id " \
            "  join event_parameters ev on ev.id = m.id"

    params = []

    where_clause = " WHERE"
    # add a filter on the study ID
    if studyDbId:
        query += where_clause + " ex.id = %s "
        params.append(studyDbId)
        where_clause = " AND"

    # add a filter on the observationUnitDbId
    if observationUnitDbId:
        query += where_clause + " s.id = %s "
        params.append(observationUnitDbId)
        where_clause = " AND"
    # add a filter on the eventDbId
    if eventDbId:
        query += where_clause + " m.id = %s "
        params.append(eventDbId)
        where_clause = " AND"
    # add a filter on the eventType
    if eventType:
        query += where_clause + " m.mgmttype = %s " #could use like for, e.g. fertilizer
        params.append(eventType)
        where_clause = " AND"
    if (dateRangeStart and dateRangeEnd):
        query += where_clause + " (date > = %s and date <= %s) "
        params.append(dateRangeStart)
        params.append(dateRangeEnd)
    elif dateRangeStart:
        query += where_clause + " m.date >= %s "
        params.append(dateRangeStart)
    elif dateRangeEnd:
        query += where_clause + " m.date <= %s "
        params.append(dateRangeEnd)

    query += " GROUP BY m.date, m.id, m.mgmttype, m.notes, ex.id, ev.events ORDER BY date"

    # count first
    count = helper.query_count(query, params)

    # execute query
    result = helper.query_result(query, params, pageSize, page)

    # wrap result
    data = list()
    for row in result:
        events = []
        for item in row['events']:
            new_item = [{
                "key": "level",
                "value": item[0]
            },{
                "key": "units",
                "value": item[1]
            }]

            events.append(new_item)
        data.append({
             "date": {"discreteDates": row["date"]},
             "eventDbId": row["eventdbid"],
             "eventType": row["eventtype"],
             "eventDescription": row["eventdescription"],
             "studyDbId": row["studydbid"],
             "eventParameters": events,
             "observationUnitDbIds": row["observationunitdbids"]
        })

    return helper.create_result({"data": data}, count, pageSize, page)
