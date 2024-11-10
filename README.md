# Meron Gedrago miniproject Week 10
[![CI](https://github.com/nogibjj/Meron_Gedrago_mini_Week10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Meron_Gedrago_mini_Week10/actions/workflows/cicd.yml)

## Structure for this project 

```
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│        └──cicd.yml
├── mylib/lib/
├── mydata/data/
├── .gitignore
├── visuals
├── main.py
├── test_main.py
├── visuals
├── Makefile
└── README.md

```

## Purpose of the project  

This project aims to use PySpark using a large dataset where we extract the dataset from a link into a local csv, load the csv into a local database and perform a SQL query on the the dataset.  


### extracting and loading data

Through codespaces, we extract and load the csv data, while displaying few lines below. 

<img src="visuals/Screenshot 2024-11-10 at 2.22.20 AM.png">

### Describe the data 

After loading the data, we pull summary on the data through 'describe'. Find the output below 

<img src="visuals/Screenshot 2024-11-10 at 2.24.06 AM.png">


###  Query the data 

We create a table that aggregate the births in a year and displays it in a table as the output is pictured below

<img src="visuals/Screenshot 2024-11-10 at 2.25.51 AM.png">

