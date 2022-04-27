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

#general
import requests

# use pyRevit forms to show progress.
with forms.ProgressBar(title='Exporting Workorders to Aitable base', indeterminate=True):
 
    # instantiate def, get room info
    airtableData = harvest.roomInfo()

    # do a basic post request to airtable through nocode api
    postRoomData = airtable.postData(env.REVIT_SYNC, airtableData)

    print(postRoomData)