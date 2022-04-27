# Revit to AirTable Tutorial

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
&nbsp;
## Write a Revit exporter and store the information in AirTable.
Technologies used:
 - PyRevit
 - NoCodeAPI

### Learning objectives
 This workflow is intended to be an entry level, fast, nimble workflow to allow someone to extract and aggregate information quickly.
 - We will start by building functions in IronPython for PyRevit to harvest model elements and attributes.
 - We then translate the element data into dictionary format needed for the API. 
 - We will then write functions for NoCodeAPI to do CRUD (create, read, update, delete) operations in an AirTable base.
 - We will create in AirTable, and write functions to manage a sync table to keep track of model sync events. 
 - We will learn to encapsulate and obfuscate API endpoints in an environments like file for basic security. 

### Get Started Using pyRevit
Go here to learn how to [install pyRevit.](https://www.notion.so/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d)

More guides are available here: [Create Your First Command](https://www.notion.so/Create-Your-First-Command-2509b43e28bd498fba937f5c1be7f485)

&nbsp;

## Tutorial, Getting our application up and running
### Sprint One

- [Sprint](sprints/sprint1/sprint1.md) - Get a custom tab, panel & button wired up in Revit UI 
- [Sprint](https://github.com/jrandersen/revit_to_airtable/blob/main/sprints/sprint1/sprint1.md#write-a-basic-function-to-extract-rooms-then-print-them-in-the-pyrevit-output-window) - Write functions to extract rooms output
- [Sprint](https://github.com/jrandersen/revit_to_airtable/blob/main/sprints/sprint1/sprint1.md#write-function-for-a-put-request-through-nocodeapi) - Establish a rooms table in AirTable, write function for a put request through NoCodeAPI. .

### Sprint Two
- [Sprint](sprints//sprint2/sprint2.md) - Establish an environments like file, update API endpoints.
- [Sprint](sprints//sprint2/sprint2.md) - Establish a 'sync' table in AirTable.
- [Sprint](sprints/sprint2/sprint2.md) - Write functions to manage 'sync' events.

### Sprint Three
- [Sprint](sprints//sprint3/sprint3.md) - Establish a levels table, update functions to pull level element info.
- [Sprint](sprints/sprint3//sprint3.md) - Write functions to manage linking rooms to levels in airtable.

&nbsp;

### Credits
* [Ehsan Iran-Nejad](https://github.com/eirannejad) for developing pyRevit
* [Icons8](https://icons8.com/) and its contributors for the sweet free icons
* Everyone else  [listed on the pyRevit Repo](https://github.com/eirannejad/pyRevit/blob/master/README.md#credits)

![Made with love in Asheville, NC](https://madewithlove.now.sh/us?colorA=%23575757&colorB=%2344cbd5&template=for-the-badge&text=Asheville%2C+NC)

Tutorial portion Copyright © 2022 by Jason Andersen. All Rights Reserved