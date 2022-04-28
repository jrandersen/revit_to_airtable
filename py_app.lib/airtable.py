#Airtable function through NoCodeAPI
import requests
import utils
import harvest


def postData(url, data):
    result = []
    r = requests.post(url = url, params = {}, json = data)
    result.append(r.json())
    return utils.listSmash(result)

def getData(url):
    result = []
    r = requests.get(url = url, params = {})
    result.append(r.json())
    return result

def putData(url, data):
    result = []
    r = requests.put(url = url, params = {}, json = data)
    result.append(r.json())
    return result

def deleteData(url, recordIds):
    data = recordIds
    params = {}
    try:
        r = requests.delete(url = url, params = params, json = data)
        return r
    except Exception as msg:
        print(msg)
        pass

# ---------------- MANAGING SYNC TABLE
def setModelSync(url, modelSyncs):
    syncRecordId = ''
    roomRecordId = []
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
    #print('recordId: {}'.format(syncRecordId))
    #print('roomIds: {}'.format(roomRecordId))
    
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