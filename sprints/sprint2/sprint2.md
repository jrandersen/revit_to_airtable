# Sprint Two

### Establish an environments 'like' file, and update API endpoints
Now that we have a basic connection, let's start refining. At the same level as your ```.extension``` folder add a ```*your_extensions_name*.lib``` folder. Inside of that library folder create a file called ```env.py``` , then in that file put the following:
```
# NoCodAPI endpoints

# airtable base:
REVIT_SYNC="YOUR_NOCODE_API_ENDPOINT_IS_HERE"
```
Once all the files are saved, I would recommend navigating back to pyRevit ribbon and *reload* so that the library folder is recognized.

![image](reload_pyrevit.png)

Your folder structure should look something like this now. 

![image](folder_structure.png)

Now navigate back to your ```script.py``` file and add the import for the env file.
```python
import env
```

Then in your POST request update the url to.
```python
url = env.REVIT_SYNC
```

We have one last part, update the ```.gitignore``` file so that we *do NOT* push this env file to github. Once that is done, the file should be greyed out in the folder structure. Now this local environments file that can hold centralized information that will not get out. When distributing the app remember to walk your users through setting this file up, some repos do this in their main install instructions.

Environment variables can get somewhat complex with dev and production credentials, deployment options to users etc, but this tutorial is meant to be an entry point for people, so the goal is to demonstrate concepts first. 

### Some app clean up and re-factoring
As next steps here, I have added a ```harvest.py``` & ```airtable.py``` to the library folder. This starts to encapsulate some similar classes and functions. In the harvest file I have added
```python
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
```

and to the airtable file I have added:
```python
import requests

def postData(url, data):
    r = requests.post(url = url, params = {}, json = data)
    result = r.json()
    return result
```

Notice that I moved all the imports there too. This significantly cleans up the main ```script.py``` file in the Revit ribbon too, as it is just calling to functions in other files:
```python
# pyRevit
from pyrevit import forms

# our library files
import env, harvest, airtable

# use pyRevit forms to show progress.
with forms.ProgressBar(title='Exporting room data Aitable base', indeterminate=True):
 
    # instantiate def, get room info
    airtableData = harvest.roomInfo()

    # do a basic post request to airtable through nocode api
    postRoomData = airtable.postData(env.REVIT_SYNC, airtableData)

    print(postRoomData)
```
### Establish a sync table in AirTable.
Create a new table called ```modelSync```; in there create columns: 
- numberOfSyncs 
- userName 
- modelPath 
- modelName 

Then make the first column a formula that concatenates both the path & model ```modelPath&"/"&modelName```. We will use this to identify our model for now.

![image](modelSync_table.png)


Now we need update the code in our app do the following, in psuedo-code:
```python
# first does a GET request to sync table,
# then compares the response to the modelPath + modelName to see if the record exists. 
# If it *does not* exist the function does a POST request with the new model info to the sync table 
# then stores the recordId of the modelSync response to use later.
# then proceeds with the export of rooms as before, but the function adds the modelSync recordId to the room element (we will update existing function and airtable to do this).
# Else if a record *does* exist, 
# the function makes a list if the rooms recordIds & the stores modelSync recordId for use later. 
# then the function does a DELETE request to the rooms table, with the recordIds above (I know, we could also do an UPDATE request to the rooms table, maybe try that too, making sure to add or take away a rooms in revit to see if all records are correct)
# finally at last, the function does a POST request to add the room data and the modelSync recordIds
```

This should do it, I opted to go ahead with the DELETE request for a couple of reasons. 
- First when a person deletes a room in revit, if a record in airtable still existed and we would have to parse the new and old to then delete any difference in airtable anyway, then do the update on the remaining records, so I am electing to gather all rooms in airtable associated with this model and wipe them out with each new sync.
- This also has the side-benefit of keeping line count low in the free tier of airtable.
- One disadvantage is that we do not get 'historical' data. If that were the case we would have to set up a different function (i'll do this in other tutorials when interacting directly with PostgreSQL or MongoDB, it is much easier there). 


### Write functions to manage sync events
Here are updates to the function in the harvest file. This provides some functions to get the model path if a file is either workshared or not workshared. In addition I am getting username & simple model name for later.
```python
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
```


Here are the updates to the functions in the airtable file. I have added some code here to deal with large responses from NoCodeAPI. It is buried in the documentation but the response are bundles of 100 lines, this is a result of airtable throttling. To deal with that on our side; I am creating a list ```result``` then each 100 line ```r.json``` is appended to it, finally in the return I am flattening the list with the ```utils.listSmash```. 
```python
def getData(url):
    result = []
    r = requests.get(url = url, params = {})
    result.append(r.json())
    return utils.listSmash(result)
```

Instantiating the GET request function and feeding our url from the env file such as ```getSyncs = airtable.getData(env.MODELSYNCS)``` gets us a response from airtable like:

![image](get_request_doc_data.png)

In the response notice the records and ```id:``` of each row in the model sync table. In addition, this has all of the record ids from ```Rooms``` table (they are now linked tables in airtable). 

Next, let's parse this info out. We iterate over the response to get the items we need, all the while adding in some cases for if there are no linked tables (somehow this could happen, I'm sure.).
```python
    for sync in getSyncs:
        for record in sync['records']:
            print(record['id'])
            if record['fields']['roomsCount'] != 0:
                print(record['fields']['Rooms'])
            else:
                print("No Rooms!")
```

![image](parse_response.png)

&nbsp;
---

And it works, it performs teh logic to identify a new model to teh list! 
I had to create a ```roomsCount``` column in the table, so that I could query it in the code to grab the recordIds of Rooms table rows. If you notice ```record['fields']['Rooms']``` is a List, which is great, in addition the ```record['id']``` is simple to get.

![image](revitModelSync_Table.gif)

I now have to re-factor quite a bit in this next section. First in the ```harvest.py``` file we add:

```python
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
```

The ```getModelId()``` function pulls the value from the parameter *Project Number*. I decided to store (for now) the airtable RECORD_ID() here. I will follow up with a tutorial on extensible storage at a later date. If this param does not work for you just select another that works, I just wanted something that will be consistent with all new started projects, and project information is always there. The ```setModelId()``` will be used to set it, once received back our response from airtable. we'll pass it through and update the param.


Second is the ```airtable.py``` file we add:
```python
def setModelSync(url, modelSyncs):
    syncRecordId = ''
    roomRecordId = []
    # parsing the response here to find match between modelId <--> recordId
    for record in modelSyncs[0]['records']:
        modelid = harvest.getModelId()
        if harvest.getModelId() == record['id']:
            print("updating existing records...")
            syncRecordId = record['id']
            # This preping data for airtable
            numberOfSyncs = int(record['fields']['numberOfSyncs'] + 1)
            if record['fields']['roomsCount'] != 0:
                roomRecordId = record['fields']['Rooms']
            else:
                roomRecordId = []
            consecutiveSyncData = [{'id': syncRecordId,\
                "fields":{"numberOfSyncs": numberOfSyncs,\
                    'modelPath':harvest.getModelPath(),\
                        'userName':harvest.getUserName(),\
                            "modelName":harvest.getModelName()}}]
            # airtable api call
            updateModelSync = putData(url, consecutiveSyncData)
            print('put response: {}'.format(updateModelSync))
        else:
            pass       
    # if no match was found, we assume it is new and add a new record
    if syncRecordId  == '':
        print('posting new model records...')
        newSyncData = [{"modelName":harvest.getModelName(),\
             "numberOfSyncs":1,\
                'modelPath':harvest.getModelPath(),\
                    'userName':harvest.getUserName()}]
        postModelSync = postData(url, newSyncData)
        print('updating revit param with recordId, remember to Save...')
        for record in postModelSync:
            syncRecordId = record['id']
            # set project number in model
            harvest.setModelId(syncRecordId)
        print('post response: {}'.format(postModelSync))
    return syncRecordId, roomRecordId
```

The ```setModelSync()``` function handles the logic for managing all changes to eth model sync table. It first looks for a match between teh modelId and RecordId from airtable, if it is found it walks through getting new info, iterating sync numbers and finally does put request. The second half is if there is no match, it gathers all info and does a post request to add a new line, then updates teh model to set the recordId in teh project number parameter. 
The function returns both the recordId of the modelSync and room recordIds for use later.


Now for the ```script.py``` file, we add:

```python
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
```

This has all the major moves, get request on ModelSync table, compare model and model sync data & update, delete request on Rooms table, gate all new rooms from model, then finally post request with new room data.

![image](revitModelSync_Full.gif)

In the .gif above notice that the model sync table updates along with the deletion and creation of new linked files in the rooms table, oh, and I set it up to not pull unplaced rooms. There are certainly some more things to work out, but that wraps it up for this workflow.

Let me know if you have any feedback!