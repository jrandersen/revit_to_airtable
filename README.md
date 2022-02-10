# Revit to Airtable Tutorial

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
&nbsp;

## How to build a Revit exporter and store the information in an Airtable base.

Technologies used:
 - PyRevit
 - NoCodeAPI

## Intention
 We will cover building functions in IronPython in PyRevit to harvest revit elements and attributes, translate that into json format. We will then write functions for NoCodeAPI to do CRUD (create, read, update, delete) operations in an Airtable base. This workflow is intended to be an entry level, fast, nimble workflow that can extract and agregate information quickly. We will work to write a sync table to keep track of model sync to the base, segregate api endpoints in an environemts file (to 'gitignore') for basic security. 

# Get Started Using pyRevit

[Install pyRevit](https://www.notion.so/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d)

**↓** More guides are available here

[HOW TO Guides](https://www.notion.so/HOW-TO-Guides-dc20e0e227b74d9bbc775699904152cb)

## Get Started Developing for pyRevit

[Create Your First Command](https://www.notion.so/Create-Your-First-Command-2509b43e28bd498fba937f5c1be7f485)

**↓** Read the docs to know everything about pyRevit scripts, extensions, ...

[Developer Docs](https://www.notion.so/Developer-Docs-2c88f3ecccde422d9504e20b6b9e04f8)

![Made with love in Asheville, NC](https://madewithlove.now.sh/us?colorA=%23575757&colorB=%2344cbd5&template=for-the-badge&text=Asheville%2C+NC)

Copyright © 2021 by Jason Andersen. All Rights Reserved