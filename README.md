# Revit to Airtable Tutorial

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
&nbsp;

### How to write a Revit exporter and store the information in Airtable.
Technologies used:
 - PyRevit
 - NoCodeAPI

### Learning objectives
 This workflow is intended to be an entry level, fast, nimble workflow that can extract and agregate information quickly.
 - We will start by building functions in IronPython for PyRevit to harvest model elements and attributes.
 - We then translate the element data into json format. 
 - We will then write functions for NoCodeAPI to do CRUD (create, read, update, delete) operations in an Airtable base.
 - We will write functions to manage a sync table to keep track of model sync events 
 - we will learn to segregate API endpoints in an environemts file for basic security. 

### Get Started Using pyRevit

[Install pyRevit](https://www.notion.so/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d)

**↓** More guides are available here

[How-to-guides](https://www.notion.so/HOW-TO-Guides-dc20e0e227b74d9bbc775699904152cb)

[Create Your First Command](https://www.notion.so/Create-Your-First-Command-2509b43e28bd498fba937f5c1be7f485)

&nbsp;

## Tutorial
## Getting our application up and running

- [Sprint](sprints/sprint1/sprint1.md) - Get a custom tab, panel & button wired up in Revit UI 
- [Sprint](https://github.com/jrandersen/revit_to_airtable/blob/main/sprints/sprint1/sprint1.md#write-a-basic-function-to-extract-rooms-then-print-them-in-the-pyrevit-output-window) - Write functions to extract rooms output
- [Sprint](https://github.com/jrandersen/revit_to_airtable/blob/main/sprints/sprint1/sprint1.md#write-function-for-a-put-request-through-nocodeapi) - Display room info in pyRevit output

## More advanced topics
- [Sprint](sprints/sprint2.md) - Establish a rooms table in AirTable.
- [Sprint](sprints/sprint2.md) - Write function for a put request through NoCodeAPI. 
- [Sprint](sprints/sprint2.md) - Establish an environments file, update API endpoints.
- [Sprint](sprints/sprint2.md) - Establish a 'sync' table in AirTable.
- [Sprint](sprints/sprint2.md) - Write functions to manage sync events.
- [Sprint](sprints/sprint2.md) - Establish a levels table, write functions to pull model elements.
- [Sprint](sprints/sprint2.md) - Write functions to manage linking from levels table to rooms table. This will use, get, put and update functions

&nbsp;


## Credits
* [Ehsan Iran-Nejad](https://github.com/eirannejad) for developing pyRevit
* [Icons8](https://icons8.com/) and its contributors for the sweet free icons
* Everyone else  [listed on the pyRevit Repo](https://github.com/eirannejad/pyRevit/blob/master/README.md#credits)

![Made with love in Asheville, NC](https://madewithlove.now.sh/us?colorA=%23575757&colorB=%2344cbd5&template=for-the-badge&text=Asheville%2C+NC)

Tutorial portion Copyright © 2022 by Jason Andersen. All Rights Reserved