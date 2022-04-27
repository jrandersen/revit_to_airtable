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

    # get information from the modelSync table in airtable
    getSyncs = airtable.getData(env.MODELSYNCS)
    print('modelsync response:'.format(getSyncs))

    # get the model information needed
    path = harvest.getModelPath
    user = harvest.getUserName
    modelName = harvest.getModelName

    print('path:'.format(path))
    print('user:'.format(user))
    print('model name:'.format(modelName))

    
    # post request to airtable through nocode api
    #postRoomData = airtable.postData(env.ROOMS, airtableData)