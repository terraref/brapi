import logging

import api.germplasm
import api.locations
import helper


def search(commonCropName=None, studyTypeDbId=None, programDbId=None, locationDbId=None, seasonDbId=None,
           trialDbId=None, studyDbId=None, active=None, sortBy=None, sortOrder=None, pageSize=None, page=None):
    params = list()

    query = "SELECT DISTINCT experiments.id as studyDbId, " \
            "   experiments.name as studyName, " \
            "   experiments.start_date as startDate, " \
            "   experiments.end_date as endDate, " \
            "   experiments.description as studyDescription, " \
            "   sitegroups.id as location_id " \
            "FROM experiments, experiments_sites, sitegroups, sitegroups_sites " \
            "WHERE experiments.id = experiments_sites.experiment_id " \
            "AND sitegroups_sites.site_id = experiments_sites.site_id " \
            "AND sitegroups_sites.sitegroup_id = sitegroups.id"

    if studyDbId:
        query += " AND experiments.id = %s "
        # query = query % studyDbId
        params.append(studyDbId)

    logging.debug(query)

    # count first
    count = helper.query_count(query, params)

    # execute query
    results = helper.query_result(query, params, pageSize, page)

    # wrap result
    data = []
    for row in results:
        study = dict()
        study['studyDbId'] = str(row_pop(row, 'studydbid', ''))
        study['studyName'] = row_pop(row, 'studyname', '')
        study['startDate'] = row_pop(row, 'startdate', '')
        study['endDate'] = row_pop(row, 'enddate', '')

        current_descrption = row_pop(row, 'studydescription', '')
        current_descrption = current_descrption.replace('\n', ' ')
        current_descrption = current_descrption.replace('\r', '')
        study['statisticalDesign'] = {'description': current_descrption }

        if row.has_key('location_id'):
            location = api.locations.query(dataOnly=True, locationDbId=row['location_id'])
            if location:
                study['location'] = location

        data.append(study)
    return helper.create_result({"data": data}, count, pageSize, page)


def get(studyDbId):
    return search(studyDbId=studyDbId)


def germplasm_search(studyDbId, pageSize=None, page=None):
    params = list()

    query = "SELECT DISTINCT sites_cultivars.cultivar_id AS cultivar_id " \
            "FROM experiments_sites, sites_cultivars " \
            "WHERE experiments_sites.site_id = sites_cultivars.site_id "

    if studyDbId:
        query += "AND experiments_sites.experiment_id = %s "
        params.append(studyDbId)

    logging.debug(query)

    # count first
    count = helper.query_count(query, params)

    # execute query
    results = helper.query_result(query, params, pageSize, page)

    # wrap result
    data = []
    for row in results:
        entry = api.germplasm.get_result(dataonly=True, germplasmDbId=row['cultivar_id'])
        if entry:
            data.append(entry[0])

    return helper.create_result({"data": data}, count)


def layout_search(studyDbId, pageSize=None, page=None):
    params = list()

    query = "SELECT DISTINCT experiments.id as studyDbId, " \
            "   experiments.name as studyName, " \
            "   experiments_sites.site_id as observation_unit_db_id, " \
            "   sites.sitename as location_abbreviation, " \
            "   sites_cultivars.cultivar_id as germPlasmDbId, " \
            "   cultivars.id as cultivarid, " \
            "   cultivars.name as germplasmName " \
            "FROM experiments, experiments_sites, sites, sites_cultivars, cultivars " \
            "WHERE experiments.id = experiments_sites.experiment_id " \
            "AND sites.id = experiments_sites.site_id " \
            "AND sites_cultivars.site_id = experiments_sites.site_id " \
            "AND sites_cultivars.cultivar_id = cultivars.id "

    if studyDbId:
        query += "AND experiments.id = %s "
        params.append(studyDbId)

    logging.debug(query)

    # count first
    count = helper.query_count(query, params)

    # execute query
    results = helper.query_result(query, params)
    # wrap result
    data = []

    for row in results:
        entry = dict()
        entry['germplasmName'] = row['germplasmname']
        entry['germPlasmDbId'] = row['cultivarid']
        entry['observationUnitDbId'] = row['observation_unit_db_id']
        entry['observationUnitName'] = row['location_abbreviation']
        data.append(entry)

    return helper.create_result({"data": data}, count)


def row_pop(row, key, dflt):
    if row.has_key(key):
        return row[key]
    else:
        return dflt
