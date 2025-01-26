# Basic-ETL-Pipeline-in-Python-with-OOP

This repository contains a Python-based ETL (Extract, Transform, Load) pipeline designed to process Colombian coffee export data. The pipeline extracts data from an Excel file, transforms it by cleaning and structuring it, and loads it into an SQLite database for further analysis.

#Features

Extract: Reads data from an Excel file.

Transform: Cleans and formats the data, removing unnecessary rows and ensuring correct data types.

Load: Stores the transformed data into an SQLite database, appending a timestamp for each run.

#Prerequisites

Python 3.8 or higher

#Project Structure

.
├── etl_pipeline.py        # Main ETL pipeline script
├── test_data/             # Folder for test datasets (not included in the repo)
    ├── data_downloader.py # Downloads the XLSX file from an external URL
├── requirements.txt       # List of required dependencies

Dependencies

#This project uses the following Python libraries:

pandas: Data manipulation and analysis.

sqlalchemy: Database connection and interaction.

python-dotenv: Loading environment variables from a .env file.

openpyxl: Reading Excel files.

#Example Workflow

Extract: The pipeline reads data from the specified Excel file.

Transform: Data is cleaned by removing metadata rows and ensuring proper formatting.

Load: The cleaned data is stored in an SQLite database.

