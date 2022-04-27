""" Revit to Airtable Tutorial
Jason Andersen
----------------------------------
PyRevit Notice:
Copyright (c) 2014-2022 Ehsan Iran-Nejad
pyRevit: repository at https://github.com/eirannejad/pyRevit
"""

# pyRevit
from pyrevit import forms

# our library files
import env, harvest, airtable

# use pyRevit forms to show progress.
with forms.ProgressBar(title='Exporting room data to Aitable base', indeterminate=True):
 
    # instantiate def, get room info
    #airtableData = harvest.roomInfo()

    # get the model information needed
    path = harvest.getModelPath()
    user = harvest.getUserName()
    modelName = harvest.getModelName()

    # get information from the modelSync table in airtable
    getSyncs = airtable.getData(env.MODELSYNCS)
    
    syncRecordId = []
    roomRecordId = []
    for sync in getSyncs:
        for record in sync['records']:
            if path == record['fields']['modelPath']:
                syncRecordId = record['id']
                if record['fields']['roomsCount'] != 0:
                    roomRecordId = record['fields']['Rooms']
                print("updating existing records...")
                consecutiveSyncData = [{'id':record['id'],"fields":{"numberOfSyncs":int(record['fields']['numberOfSyncs'] + 1)}}]
                updateModelSync = airtable.putData(env.MODELSYNCS, consecutiveSyncData)
                print('updated record {}'.format(updateModelSync))       
    if len(syncRecordId)  == 0:
        print('posting new model records...')
        newSyncData = [{"modelName":modelName,\
             "numberOfSyncs":1,\
                'modelPath':path,\
                    'userName':user}]
        postModelSync = airtable.postData(env.MODELSYNCS, newSyncData)
        print('new record {}'.format(postModelSync))




    # post request to airtable through nocode api
    #postRoomData = airtable.postData(env.ROOMS, airtableData)