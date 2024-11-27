"""
Main cli or app entry point
"""

from mylib.extract import extract
from Notebook_Folder.transform_load import load
from Notebook_Folder.query_viz import query_transform, viz
import os


if __name__ == "__main__":
    current_directory = os.getcwd()
    print(current_directory)
    extract()
    load()
    query_transform()
    viz()