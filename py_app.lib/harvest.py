# Libraray file to contain revit model harvesting class / functions
from pyrevit import DB
import rpw

# room info
def roomInfo():
    roomInfo = []
    revitRoomCollector = rpw.db.Collector(of_category=DB.BuiltInCategory.OST_Rooms, is_not_type=True)   
    for e in revitRoomCollector:
        roomInfo.append({
            'Name': e.Parameter[DB.BuiltInParameter.ROOM_NAME].AsString(),\
             'Number': int(e.Number)})
    return roomInfo