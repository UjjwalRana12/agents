import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load_csv_data(file):
   
    data = pd.read_csv(file)
    return data

def load_google_sheet_data(sheet_url, api_key):
    
    try:
        
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(api_key, scope)
        client = gspread.authorize(credentials)
        
        # Open Google Sheet
        sheet = client.open_by_url(sheet_url)
        worksheet = sheet.get_worksheet(0) 
        data = pd.DataFrame(worksheet.get_all_records())
        return data
    except Exception as e:
        print(f"Error loading Google Sheet: {e}")
        return None
