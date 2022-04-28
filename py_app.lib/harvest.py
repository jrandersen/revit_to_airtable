# Library file to contain revit model harvesting class / functions
from pyrevit import DB
import rpw
import uuid
doc = __revit__.ActiveUIDocument.Document

# room info
def roomInfo(recordId):
    roomInfo = []
    revitRoomCollector = rpw.db.Collector(of_category=DB.BuiltInCategory.OST_Rooms, is_not_type=True)   
    for e in revitRoomCollector:
        roomInfo.append({
            'Name': e.Parameter[DB.BuiltInParameter.ROOM_NAME].AsString(),\
             'Number': int(e.Number),\
                 'modelSync': [recordId]})
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

def getModelId():
    recordId = None
    pg_collector = DB.FilteredElementCollector(doc)\
    .WherePasses(DB.ElementCategoryFilter(DB.BuiltInCategory.OST_ProjectInformation))\
        .WhereElementIsNotElementType().ToElements()
    for i in pg_collector:
        recordId = i.Parameter[DB.BuiltInParameter.PROJECT_NUMBER].AsString()
    return recordId

# =============== SET MODEL DATA
def setModelId(recordId):
    pg_collector = DB.FilteredElementCollector(doc)\
    .WherePasses(DB.ElementCategoryFilter(DB.BuiltInCategory.OST_ProjectInformation))\
        .WhereElementIsNotElementType().ToElements()

    for i in pg_collector:
        t = DB.Transaction(doc, "Set recordId in Project Number")
        t.Start()
        orgName = i.Parameter[DB.BuiltInParameter.PROJECT_NUMBER]
        orgName.Set(recordId)
        t.Commit()        
    return recordId