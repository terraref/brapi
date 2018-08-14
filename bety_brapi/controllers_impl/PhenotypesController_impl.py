from bety_brapi import database
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

    query = "select v.id as observationVariableDbId,  \
                    v.name as observationVariableName,  \
                    t.id as observationDbId, \
                    t.mean as value, \
                    t.date as observationTimeStamp, \
                    s.sitename as sitename\
             from traits t, variables v, sites s \
             where v.id = t.variable_id \
             and t.site_id = s.id" 

    # For not, observationVariable is variable
    # e.g.,  6000000007 plant_height 
    if observationVariableDbId:
        query += " and v.id = %s " % observationVariableDbId

    # For now, location is site
    if locationDbId:
        query += " and t.site_id = %s " % locationDbId

    # For now, germplasm is cultivar
    if germplasmDbId:
        query += " and t.cultivar_id = %s " % germplasmDbId

    if (observationTimeStampRangeStart and observationTimeStampRangeEnd):
        query += " and (date >= '%s' and date <= '%s')" % (observationTimeStampRangeStart, observationTimeStampRangeEnd)
    elif observationTimeStampRangeStart:
        query += " and date >= %s" % observationTimeStampRangeStart
    elif observationTimeStampRangeEnd:
        query += " and date <= %s" % observationTimeStampRangeEnd

    # TODO: actual pagination
    query += " limit 100"     

    #app.logger.debug(query)
    res = database.get_engine().execute(query)

    response = {
        "metadata":  {
            "datafiles": [],
            "pagination": {
                "currentPage": 0,
                "pageSize": 100,
                "totalCount": 2,
                "totalPages": 1
           },
           "status": []
        },
        "result":  {
            "data": {
               "observations": [dict(r) for r in res]
            }
        }
    }

    return response
    #return jsonify([dict(r) for r in res])
