import logging

import api.germplasm
import api.locations
import api.seasons
import helper


def search(commonCropName=None, studyTypeDbId=None, programDbId=None, locationDbId=None,
           seasonDbId=None, trialDbId=None, studyDbId=None,
           active=None, sortBy=None, sortOrder=None, pageSize=None, page=None):
    params = list()

    query = "SELECT DISTINCT experiments.id as studyDbId, " \
            "   LTRIM(RTRIM(SPLIT_PART(experiments.name, ': ', 2))) as studyName, " \
            "   experiments.start_date as startDate, " \
            "   experiments.end_date as endDate, " \
            "   experiments.description as studyDescription, " \
            "   sitegroups.id as location_id, " \
            "   seasonids.id as season_id " \
            "FROM experiments, experiments_sites, sitegroups, sitegroups_sites, " \
            "(select * from (select distinct extract(year from start_date) as year, " \
            "LTRIM(RTRIM(SPLIT_PART(name, ': ', 1))) as season," \
            "md5(LTRIM(RTRIM(SPLIT_PART(name, ': ', 1))))::varchar(255) as id from experiments) season_list) seasonids " \
            "WHERE experiments.id = experiments_sites.experiment_id " \
            "AND sitegroups_sites.site_id = experiments_sites.site_id " \
            "AND sitegroups_sites.sitegroup_id = sitegroups.id " \
            "AND seasonids.season = LTRIM(RTRIM(SPLIT_PART(experiments.name, ': ', 1))) "

    if studyDbId:
        query += " AND experiments.id = %s "
        params.append(studyDbId)
    if seasonDbId:
        query += " AND seasonids.id = %s "
        params.append(seasonDbId)

    if sortBy:
        if sortBy == "studyDbId":
            query += " ORDER BY experiments.id"
        elif sortBy == "locationDbId":
            query += " ORDER BY sitegroups.id"
        elif sortBy == "seasonDbId":
            query += " ORDER BY seasonids.id"
        elif sortBy == "studyName":
            query += " ORDER BY LTRIM(RTRIM(SPLIT_PART(experiments.name, ': ', 2)))"
        elif sortBy == "studyLocation":
            query += " ORDER BY sitegroups.name"
        else:
            # programDbId, trialDbId, studyTypeDbId, programName - unsupported
            pass
        if sortOrder:
            # do this here, params will add apostrophes around it
            if sortOrder.lower() == "asc":
                query += " ASC"
            elif sortOrder.lower() == "desc":
                query += " DESC"

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

        # get seasons data
        if row.has_key('season_id'):
            season = api.seasons.search(row['season_id'])
            study['seasons'] = season['result']['data']

        # check location ID
        if row.has_key('location_id'):
            if locationDbId and locationDbId != str(row['location_id']):
                continue
            location = api.locations.query(single_row=True, locationDbId=row['location_id'])
            if location:
                study['location'] = location

        data.append(study)
    return helper.create_result({"data": data}, count, pageSize, page)


def get(studyDbId):
    full_result = search(studyDbId=studyDbId)

    # fix the result so that the 'data' block is omitted in the case of a single result
    if "data" in full_result["result"] and len(full_result["result"]["data"]) > 0:
        full_result["result"] = full_result["result"]["data"][0]
    else:
        full_result["result"] = {}

    return full_result


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
        else:
            logging.warning("Missing germplasm for " + str(row['cultivar_id']))
            count -= 1

    return helper.create_result({"data": data}, count)


def layouts_search(studyDbId, pageSize=None, page=None):
    params = list()

    query = "SELECT DISTINCT experiments.id as studyDbId, " \
            "   experiments.name as studyName, " \
            "   experiments_sites.site_id as observation_unit_db_id, " \
            "   sites.sitename as location_abbreviation, " \
            "   cultivars.id as germPlasmDbId, " \
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
    results = helper.query_result(query, params, pageSize, page)
    # wrap result
    data = []

    for row in results:
        entry = dict()
        entry['studyDbId'] = str(row['studydbid'])
        entry['studyName'] = row['studyname']
        entry['germplasmName'] = row['germplasmname']
        entry['germPlasmDbId'] = str(row['germplasmdbid'])
        entry['observationLevel'] = 'plot'
        entry['observationUnitDbId'] = str(row['observation_unit_db_id'])
        entry['observationUnitName'] = row['location_abbreviation']
        data.append(entry)

    return helper.create_result({"data": data}, count, pageSize, page)


def row_pop(row, key, dflt):
    if row.has_key(key):
        return row[key]
    else:
        return dflt
