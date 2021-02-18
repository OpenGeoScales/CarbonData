# CarbonData 2

# What is CarbonData for?

- Identifying and documenting GHG elmissions data sources
- Collect and share raw data (in github repo if data is less than 100MB otherwise kaggle datasets)
- Analyse raw data and provide insights
- Compare vairous sources
- Combine data sources
- Develop API to query normalized data source
- Develpop dashs to explore it

# How can I contribute?

- A data detective: 
    - I found a new data source that is not referenced
- 

## Sharing Data on GHG emissions

There are multiple data sources on GHG emissions. This data is provided in various platforms, formats, frequencies, scales...

Our goal here is 

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
