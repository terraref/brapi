from bety_brapi import helper
import calendar
import connexion

app = connexion.App(__name__, specification_dir='./swagger/')
logger = app.app.logger

def seasons_get(year=None, pageSize=None, page=None):
    """
    Return a list of all seasons. Right now this will return the seasons as the
    year and month of the startdate. The database-id that is returned will be of
    the format YYYYMM.
    :param year: filter the seasons on the yaer
    :param pageSize: number of elements to return
    :param page: which page to return
    :return: all seasons in the page
    """
    params = list()
    query = "SELECT DISTINCT extract(month from start_date) as month," \
            "                extract(year from start_date) as year" \
            "   FROM experiments "

    # add a filter on the year
    if year:
        query += "   WHERE extract(year from start_date) = %s"
        params.append(year)

    query += "   ORDER BY year, month"

    # count first
    count = helper.query_count(query, params)

    # execute query
    result = helper.query_result(query, params, pageSize, page)

    # wrap result
    data = list()
    for row in result:
        data.append({
            "season": calendar.month_name[int(row["month"])],
            "year": str(int(row["year"])),
            "seasonDbId": "%04d%02d" % (row["year"], row["month"])
        })

    return helper.create_result({"data": data}, count, pageSize, page)


def studies_study_db_id_get(studyDbId):
    params = list()

    query = "SELECT experiments.id as studyDbId, " \
            "   experiments.name as studyName, " \
            "   experiments.start_date as startDate, " \
            "   experiments.end_date as endDate, " \
            "   experiments.description as studyDescription, " \
            "   experiments_sites.site_id as location_name, " \
            "   sites.sitename as location_abbreviation " \
            "FROM experiments, experiments_sites, sites " \
            "WHERE experiments.id = experiments_sites.experiment_id " \
            "AND sites.id = experiments_sites.site_id " \
            # "AND experiments.id = " + studyDbId

    if studyDbId:
        query += " AND experiments.id = %s "
        # query = query % studyDbId
        params.append(studyDbId)

    logger.debug(query)

    # count first
    count = helper.query_count(query, params)

    # execute query
    results = helper.query_result(query, params)

    # wrap result
    data = []
    for row in results:
        experiment = dict()
        location = dict()
        experiment['studyDbId'] = row['studydbid']
        experiment['studyName'] = row['studyname']
        experiment['startDate'] = row['startdate']
        experiment['endDate'] = row['enddate']
        current_descrption = row['studydescription']
        current_descrption = current_descrption.replace('\n', '')
        current_descrption = current_descrption.replace('\r', '')
        experiment['studyDescription'] = current_descrption

        experiment['locationName'] = row['location_abbreviation']
        experiment['locationDbId'] = row['location_name']
        # location['name'] = row['location_name']
        # location['abbreviation'] = row['location_abbreviation']
        #
        # experiment['location'] = location

        data.append(experiment)
    return helper.create_result({"study": data}, count)


def studies_study_db_id_germplasm_get(studyDbId, pageSize=None, page=None):
    params = list()

    query = "SELECT experiments.id as studyDbId, " \
            "   experiments.name as studyName, " \
            "   experiments.start_date as startDate, " \
            "   experiments.end_date as endDate, " \
            "   experiments.description as studyDescription, " \
            "   experiments_sites.site_id as location_name, " \
            "   sites.sitename as location_abbreviation, " \
            "   sites_cultivars.cultivar_id as germPlasmDbId, " \
            "   cultivars.specie_id as species, " \
            "   cultivars.id as cultivarid, " \
            "   cultivars.name as germplasmName, " \
            "   species.scientificname as scientificname, " \
            "   species.commonname as commonname " \
            "FROM experiments, experiments_sites, sites, sites_cultivars, cultivars, species " \
            "WHERE experiments.id = experiments_sites.experiment_id " \
            "AND sites.id = experiments_sites.site_id " \
            "AND sites_cultivars.site_id = experiments_sites.site_id " \
            "AND species.id = cultivars.specie_id " \
            # "AND experiments.id = " + studyDbId

    if studyDbId:
        query += " and experiments.id = %s "
        params.append(studyDbId)

    logger.debug(query)
    # count first
    count = helper.query_count(query, params)



    # execute query
    results = helper.query_result(query, params)
    # wrap result
    data = []

    for row in results:
        entry = dict()
        entry['commonCropName'] = row['commonname']
        entry['germplasmName'] = row['germplasmname']
        entry['germPlasmDbId'] = row['cultivarid']
        data.append(entry)

    # for row in results:
    #
    #     experiment = dict()
    #     location = dict()
    #     germplasm = dict()
    #
    #     experiment['studyDbId'] = row['studydbid']
    #     experiment['studyType'] = row['studyname']
    #     experiment['startDate'] = row['startdate']
    #     experiment['endDate'] = row['enddate']
    #     current_descrption = row['studydescription']
    #     current_descrption = current_descrption.replace('\n', '')
    #     current_descrption = current_descrption.replace('\r', '')
    #     experiment['studyDescription'] = current_descrption
    #
    #     location['name'] = row['location_name']
    #     location['abbreviation'] = row['location_abbreviation']
    #
    #     germplasm['germplasmName'] = row['germplasmname']
    #     germplasm['scientific_name'] = row['scientificname']
    #     germplasm['common_name'] = row['commonname']
    #
    #     location['germplasm'] = germplasm
    #     experiment['location'] = location
    #
    #     data.append(experiment)
    return helper.create_result({"data": data}, count)