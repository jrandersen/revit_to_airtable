## Sprint One
### Create the plugin structure for a base application in pyRevit.

Basic folder structure, py scripts, icons, and yaml files. Find great selection of royalty free icons on [ICON8](https://icons8.com/icons).
![image](base_app_code.png)


Write some really simple code to test out the app in Revit to see that it works.
```python
# base extension

param = "Hello World"
print(param)
```


Test it... okay, it is up and running.
![image](base_app.png)

---
<br>

### Write a basic functions to extract rooms and print them in the PyRevit output
Use RPW to get all rooms
![image](collector_roomInfo.png)

```python
# pyRevit
from pyrevit import DB
import rpw

revitRoomCollector = rpw.db.Collector(of_category=DB.BuiltInCategory.OST_Rooms, is_not_type=True)

def roomInfo(collector):
    roomInfo = []
    for e in collector:
        roomInfo.append({'name': e.Parameter[DB.BuiltInParameter.ROOM_NAME].AsString(), 'number': e.Number})
    return roomInfo

print(roomInfo(revitRoomCollector))
```

Organize them

print rooms in pyRevit window

---
<br>

### Write function for a put request through NoCodeAPI
Set up NoCodeAPI account

Create post command

Enjoy