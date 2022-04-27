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

Your folder structure should look something like this now 

![image](folder_structure.png)

Now navigate back to your ```script.py``` file and add teh import for the env file
```python
import env
```

Then in your POST request update your url to
```python
url = env.REVIT_SYNC
```

We have one last import part, update your ```.gitignore``` file to *NOT* save your env file. Once that is done you should see teh file greyed out in the folder structure. Now you have a local file that can hold centralized information that will not get out of your org. When distrusting this app remember to walk your user through setting this file up. In larger orgs this can be automated.

Environment variables can get quite complex with dev and production versions, deploying them to uses etc, but this tutorial is meant to be an entry point for people, so it is kept as easy entry to demonstrate concepts first. 

### Establish a sync table in AirTable.

### Write functions to manage sync events