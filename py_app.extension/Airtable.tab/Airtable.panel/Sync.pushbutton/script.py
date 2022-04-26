""" Revit to Airtable Tutorial
Jason Andersen
----------------------------------
PyRevit Notice:
Copyright (c) 2014-2022 Ehsan Iran-Nejad
pyRevit: repository at https://github.com/eirannejad/pyRevit
"""

# pyRevit
from pyrevit import DB
import rpw

#general
import requests

revitRoomCollector = rpw.db.Collector(of_category=DB.BuiltInCategory.OST_Rooms, is_not_type=True)

def roomInfo(collector):
    roomInfo = []
    for e in collector:
        roomInfo.append({
            'Name': e.Parameter[DB.BuiltInParameter.ROOM_NAME].AsString(),\
             'Number': int(e.Number)})
    return roomInfo

airtableData = roomInfo(revitRoomCollector)

url = "https://v1.nocodeapi.com/jrandersen/airtable/NBknQBAnYLitRlTH?tableName=rooms"
params = {}
data = airtableData
r = requests.post(url = url, params = params, json = data)
result = r.json()
print(result)