from bety_brapi import helper
from flask import jsonify
from flask import current_app as app


def phenotypes_search_get(germplasmDbId=None, observationVariableDbId=None, 
        studyDbId=None, locationDbId=None, trialDbId=None, programDbId=None, 
        seasonDbId=None, observationLevel=None, observationTimeStampRangeStart=None, 
        observationTimeStampRangeEnd=None, pageSize=None, page=None):

    # TODO: Map additional parameters
    # studyDbId = experiment?
    # trialDbId = ?
    # programDbId = always terra
    # seasonDbId = we don't track?
    # observationLevel =?
    # pageSize
    # page

    params = []
    query = "select v.id as observationVariableDbId,  \
                    v.name as observationVariableName,  \
                    t.id as observationDbId, \
                    t.mean as value, \
                    t.date as observationTimeStamp, \
                    s.sitename as location_abbreviation, \
                    es.experiment_id as studyDbId, \
                    et.treatment_id as treatments, \
                    treatments.name as treatment_factor, \
                    treatments.definition as treatment_definition \
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

    count = helper.query_count(query, params)
    res = helper.query_result(query, params, pageSize, page)
    data = {"observations": [dict(r) for r in res]}

    return helper.create_result({"data": data}, count, pageSize, page)
