Search Query Builder with LLM Integration:-
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
 SERPAPI_KEY=b7d***************
 GOOGLE_SHEETS_API_KEY=AIzaSy************
 GROQ_KEY=gsk_9h1Wl******************

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


ALSO HERE IS THE LINK OF VIDEO :-https://www.loom.com/share/90254c29d6b54f85b7f81e5f1a1c6ff8?sid=6e95b618-374a-4a5c-9e6e-3340f2df7db8

https://github.com/user-attachments/assets/ecb6ccb3-fd02-468e-b8cf-9f19c15971cf

