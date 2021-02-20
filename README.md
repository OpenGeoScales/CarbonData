# CarbonData 

# What is CarbonData for?

##  Main goal

> Our main goal is to provide clean, verified, cross-checked and normalized datasets on GHG emissions.

## Features

- **Domain knowledge**
    - Tasks:
        -  Build a knowledge base on GHG emissions concepts, phenomenon, methods...
        - Share and explain main concepts to non-specialist
    - Outputs:
       - A report for synthesizing concepts related to GHG emissions data
       - A wiki for defning the main used concepts 

- **Data cartography**
    - Tasks:
        - Identify and document GHG emissions data sources
    - Outputs:
        - A cartography of relevant data sources on GHG emissions with documentation
        - A datacatalog for 

- **Data exploration reports**
    - Analyse raw data and provide insights
    - Compare various sources

- **Normalized GHG emissions database**
    - Combine and clean data sources
    - Model and maintain an aggregated data base

- **Normalized GHG emissions data sharing**
    -  Develop API to query normalized data source
    - Develpop dashs to explore it

# How can I contribute?

There are vaious ways to contribute to this project depending on your skills and motivation.

## Domain knowledge

Data are information collected by observation or measurements to capture and understand some phenomenon. Before exploring open GHG emissions data, we need to:
- Understand the phenomenon behind it: carbon cycle, greenhouse gazes, carbon budget, carbon sinks...
- Know how data is collected:  carbon inventories...
- Know why data is collected: carbon budget, carbon pricing...

This knowledge may be shared in the [wiki page](https://github.com/OpenGeoScales/CarbonData/wiki)


## Data sources cartography

- Identifying and referening new data srouces: 

You can find is [this page](https://github.com/OpenGeoScales/CarbonData/wiki/Data-sources) a list of identified GHG emissisons data soruces. If you identify a new data source, please add it in the list by specifying some metadata (provider, spatial coverage, format...). If you think that data sources content need to be investigated, please add an issue in the project backlog.

## Data source collection and sharing

There are several ways to collecte the data. Since we do not have data storage infrastructure, it would be prefereable to use data provided b

- API acesss: If data source can be queried by using an existing API, please document data collection method in the associated readme file. 
- http acccess: If data is stored for example in a git repo, please mention the http address used for collecting it.
- Bulk download: If data source is only accessible for download, wa can use kaggle datasets to store and document the raw data. Please, provide sample script fro accessing the data through Kaggle API.

## Raw data exploration 

## Data normalization

## Normalized Data exposure

- API: Develop API for querying the normalized data
- Viz: Develop dashboards for exploring contents.


# Collaboration process

# Structure

> Folder structure options and naming conventions for software projects

## Existing 

    project_name/
    ├── README.md             # overview of the project
    ├── data/                 # data files used in the project
        ├── README.md         # describes where data came from
        └── sub-folder/       # subdirectories by data source
    ├── notebooks/            # notebooks for exploring raw data
    

## future changes

    ├── processed_data/       # intermediate files from the analysis
    ├── manuscript/           # manuscript describing the results
    ├── app/                  # app to visualize the main dashs
    ├── results/              # results of the analysis (data, tables, figures)
    ├── src/                  # contains all code in the project
    │   ├── LICENSE           # license for your code
    │   ├── requirements.txt  # software requirements and dependencies
    │   └── ...
    └── doc/                  # documentation for your project
        ├── index
        └── ...

# License

# Contributors
