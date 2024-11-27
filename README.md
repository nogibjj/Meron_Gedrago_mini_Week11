# Meron Gedrago miniproject Week 11
[![CI](https://github.com/nogibjj/Meron_Gedrago_mini_Week11/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Meron_Gedrago_mini_Week11/actions/workflows/cicd.yml)

## Structure for this project 

```
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│        └──cicd.yml
├── mylib/
├── Notebook_Folder/
├── visuals
├── .gitignore
├── main.py
├── test_main.py
├── visuals
├── Makefile
└── README.md

```

## Purpose of the project  

This project aims to create a Databricks pipeline using Databricks. 


### Introduction to project and background 

This project implements a Databricks ETL pipeline for retrieving and processing an airline safety dataset. Key features include a well-documented ETL notebook, Delta Lake for storage, Spark SQL for data transformations, and robust error handling with data validation. It incorporates data visualizations for insights and leverages an automated Databricks API trigger for continuous processing.

The workflow utilizes a Makefile to automate tasks such as installation, testing, formatting (Python Black), linting (Ruff), and an all-in-one operation via GitHub Actions, enhancing efficiency and code quality.

The dataset, airline-safety.csv, sourced from the Aviation Safety Network, contains safety records for 56 airlines. It details seat kilometers flown weekly and segregates incidents, fatal accidents, and fatalities into two periods: 1985–1999 and 2000–2014.

### Steps taken in Databricks 

1. Connect GitHub account to Databricks Workspace
2. Create global init script for cluster start to store environment variables
3. Establishes a connection to the Databricks environment using environment variables for authentication (SERVER_HOSTNAME, ACCESS_TOKEN and JOB_ID).
4. Create a Databricks cluster that supports Pyspark
5. Clone Github repo into Databricks workspace
6. Create a job on Databricks to build an ETL pipeline
7. Run the job and ensure that it has been completed (we should see the picture below)
8. Push to github 

<img src="visuals/Screenshot 2024-11-26 at 7.45.11 PM.png">

