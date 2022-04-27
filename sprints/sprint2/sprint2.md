# Sprint Two

### Establish an environments 'like' file, and update API endpoints
Now that we have a basic connection, let's start refining. At the same level as your ```.extension``` folder add a ```*your_extensions_name*.lib``` folder. Inside of that library folder create a file called ```env.py``` , then in that file put the following:
```
# NoCodAPI endpoints

# airtable base:
REVIT_SYNC="YOUR_NOCODE_API_ENDPOINT_IS_HERE"
```
Once all teh files are saved, I recommend going back to pyRevit ribbon and *reload* so that the library folder is recognized.

![image](reload_pyrevit.png)

Your folder structure should look something like this now 

![image](folder_structure.png)

### Establish a sync table in AirTable.

### Write functions to manage sync events