# Revit to Airtable Tutorial

## How to build a Revit exporter and store the information in an Airtable base.

Technologies used:
 - PyRevit
 - NoCodeAPI

## Intension
 We will cover building functions in IronPython in PyRevit to harvest revit elements and attributes, translate that into json format. We will then write functions for NoCodeAPI to do CRUD (create, read, update, delete) operations in an Airtable base. This workflow is intended to be an entry level, fast, nimble workflow that can extract and agregate information quickly. We will work to write a sync table to keep track of model sync to the base, segregate api endpoints in an environemts file (to 'gitignore') for basic security. 

