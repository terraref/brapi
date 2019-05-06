import json
import helper


def search(commonCropName=None, programName=None, abbreviation=None,  pageSize=None, page=None):
    # load all the data
    data = json.load(open('data/programs.json', 'r'))

    # filter data
    if commonCropName:
        data = [ x for x in data if x['commonCropName'] == commonCropName]
    if programName:
        data = [ x for x in data if x['programName'] == programName]
    if abbreviation:
        data = [ x for x in data if x['abbreviation'] == abbreviation]

    # split data if needed, remembering total number
    count = len(data)
    if not pageSize:
        pageSize = helper.DEFAULT_PAGE_SIZE
    if not page:
        page = 0
    data = data[page * pageSize:(page+1) * pageSize]

    # return the resulting data
    return helper.create_result({"data": data}, count, pageSize, page)
