Search Query Builder with LLM Integration
Project Summary
This project simplifies the process of executing dynamic search queries, retrieving structured results, and analyzing data using a Language Learning Model (LLM).
It allows users to connect to data sources, generate queries, process search results, and directly update Google Sheets with LLM-processed insights

SETUP INSTRUCTIONS

1) Create and activate the virtual environment
    (verify if conda is installed)
   use command - conda create --name myenv python=3.12
                 conda activate myenv

2) run command :- pip install -r requiremnts.txt
  (it will install the all requiremnets)

3) create a .env file in root folder
  and paste the api keys
 SERPAPI_KEY=b7d564dd6042cadd79d1af24f6314ce51fb6bb0a0531e4d45818186425a9a6ad
 GOOGLE_SHEETS_API_KEY=AIzaSyBgPvxlbJaHUIWHqYhiJ0jd_spTEMMFEgA
 GROQ_KEY=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

4)-->Configure Google Sheets API
-->Enable the Google Sheets API:

-->Go to the Google Cloud Console.
Create a project 
Enable the "Google Sheets API" and "Google Drive API."
Download the Credentials File:

-->Go to the Credentials section.
a)Navigate to the Credentials section in the Google Cloud Console.
b)Create a Service Account Key.
c)Download the .json file.
d)Rename the file to google.json and place it in the root directory of your project.

5) go to the root directory and run the command
    streamlit run app.py


USAGE GUIDE
Option 1: Upload a CSV File

1)Select Upload CSV File from the sidebar.
2)Upload your CSV file.
3)Choose the column containing the search terms.
4)Enter a query template (e.g., "What is the meaning of {column_name}?").
5)Run the search to get results.
6)Process the results with the integrated LLM.

Option 2: Connect to Google Sheets

1)Select Connect to Google Sheets from the sidebar.
2)Enter the URL of your Google Sheet.
3)Choose the column containing the search terms.
4)Follow steps similar to Option 1 to process data.


THIRD PARTY TOOL
1)groq mistral model
2)serp Api
