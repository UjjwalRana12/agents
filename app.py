import streamlit as st
from modules.file_handler import load_csv_data, load_google_sheet_data
from config.config import GOOGLE_SHEETS_API_KEY

def dynamic_query_input():
   
    prompt_template = st.text_input(
        "Enter your query :", 
        placeholder="Get me the email address of {company}"
    )

    if prompt_template:
        st.write("Generated Queries:")
        query=prompt_template
        st.write(f"- {query}")

def upload_csv_file():
   
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = load_csv_data(uploaded_file)
        st.write("Preview of the uploaded data:")
        st.dataframe(data.head())
        
        
        main_column = st.selectbox("Select the main column (e.g., company names):", data.columns)
        st.write(f"Selected column: {main_column}")

        
        dynamic_query_input()

def connect_to_google_sheets():
   
    sheet_url = st.text_input("Enter Google Sheets URL")
    if st.button("Load Google Sheet Data"):
        if sheet_url:
            data = load_google_sheet_data(sheet_url, GOOGLE_SHEETS_API_KEY)
            if data is not None:
                st.write("Preview of the Google Sheets data:")
                st.dataframe(data.head())
                
                
                main_column = st.selectbox("Select the main column (e.g., company names):", data.columns)
                st.write(f"Selected column: {main_column}")

                
                dynamic_query_input(data, main_column)
        else:
            st.error("Please enter a valid Google Sheets URL.")

def main():
    st.title("Dashboard for File Upload and Google Sheets Connection")

    option = st.sidebar.selectbox(
        "Data Input Source", 
        ("Upload CSV File", "Connect to Google Sheets")
    )

    if option == "Upload CSV File":
        st.subheader("Upload a CSV File")
        upload_csv_file()

    elif option == "Connect to Google Sheets":
        st.subheader("Connect to a Google Sheet")
        connect_to_google_sheets()

if __name__ == "__main__":
    main()
