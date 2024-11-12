# app.py
import streamlit as st
from modules.file_handler import load_csv_data, load_google_sheet_data
from config.config import GOOGLE_SHEETS_API_KEY

def main():
    st.title("Dashboard for File Upload and Google Sheets Connection")

    #for csv file
    option = st.sidebar.selectbox(
        "Data Input Source", 
        ("Upload CSV File", "Connect to Google Sheets")
    )

   
    if option == "Upload CSV File":
        st.subheader("Upload a CSV File")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            
            data = load_csv_data(uploaded_file)
            st.write("Preview of the uploaded data:")
            st.dataframe(data.head())

            
            main_column = st.selectbox("Select the main column (e.g., company names):", data.columns)
            st.write(f"Selected column: {main_column}")

    # for google sheets connection
    elif option == "Connect to Google Sheets":
        st.subheader("Connect to a Google Sheet")
        sheet_url = st.text_input("Enter Google Sheets URL")
        
        if st.button("Load Google Sheet Data"):
            if sheet_url:
                
                data = load_google_sheet_data(sheet_url, GOOGLE_SHEETS_API_KEY)
                if data is not None:
                    st.write("Preview of the Google Sheets data:")
                    st.dataframe(data.head())
                    
                   
                    main_column = st.selectbox("Select the main column (e.g., company names):", data.columns)
                    st.write(f"Selected column: {main_column}")
            else:
                st.error("Please enter a valid Google Sheets URL.")

if __name__ == "__main__":
    main()
