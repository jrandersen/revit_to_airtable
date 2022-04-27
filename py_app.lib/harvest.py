# Library file to contain revit model harvesting class / functions
from pyrevit import DB
import rpw
doc = __revit__.ActiveUIDocument.Document

# room info
def roomInfo():
    roomInfo = []
    revitRoomCollector = rpw.db.Collector(of_category=DB.BuiltInCategory.OST_Rooms, is_not_type=True)   
    for e in revitRoomCollector:
        roomInfo.append({
            'Name': e.Parameter[DB.BuiltInParameter.ROOM_NAME].AsString(),\
             'Number': int(e.Number)})
    return roomInfo

# =============== GET MODEL DATA
def getModelPath():
    modelPath = []
    if doc.IsWorkshared:
        modelPath = DB.ModelPathUtils.ConvertModelPathToUserVisiblePath(doc.GetWorksharingCentralModelPath())
    else:
        modelPath = doc.PathName
    return modelPath

def getUserName():
    userName = doc.Application.Username
    return userName

def getModelName():
    modelName = doc.Title
    return modelName  