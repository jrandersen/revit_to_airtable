""" Revit to Airtable Tutorial
Jason Andersen
----------------------------------
PyRevit Notice:
Copyright (c) 2014-2022 Ehsan Iran-Nejad
pyRevit: repository at https://github.com/eirannejad/pyRevit
"""

# pyRevit
from pyrevit import DB, forms
import rpw

# our library files
import env

#general
import requests

# create definition to parse room collectors
def roomInfo(collector):
    roomInfo = []   
    for e in collector:
        roomInfo.append({
            'Name': e.Parameter[DB.BuiltInParameter.ROOM_NAME].AsString(),\
             'Number': int(e.Number)})
    return roomInfo

# use pyRevit forms to show progress.
with forms.ProgressBar(title='Exporting Workorders to Aitable base', indeterminate=True):
    # make a list of rooms
    revitRoomCollector = rpw.db.Collector(of_category=DB.BuiltInCategory.OST_Rooms, is_not_type=True)

    # instantiate def, get room info
    airtableData = roomInfo(revitRoomCollector)

    # do a basic post request to airtable through nocode api
    url = env.REVIT_SYNC
    params = {}
    data = airtableData
    r = requests.post(url = url, params = params, json = data)
    result = r.json()
    print(result)