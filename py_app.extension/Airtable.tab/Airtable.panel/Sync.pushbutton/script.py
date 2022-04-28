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
with forms.ProgressBar(title='Exporting room data to Airtable base', indeterminate=True):
    # get information from the modelSync table in airtable, returns all model syncs
    getSyncs = airtable.getData(env.MODELSYNCS)

    #check and set model sync table, returns model sync record id and room list.
    setModelSyncTable = airtable.setModelSync(env.MODELSYNCS, getSyncs)
    #print(setModelSyncTable)

    deleteData = airtable.deleteData(env.ROOMS, setModelSyncTable[1])
    print('delete data response: {}'.format(deleteData))
   
    # instantiate def, get room info
    airtableData = harvest.roomInfo(setModelSyncTable[0])
    #print('room data from airtable: {}'.format(airtableData))

    # post request to airtable through nocode api
    postRoomData = airtable.postData(env.ROOMS, airtableData)
    print('room data response: {}'.format(postRoomData))