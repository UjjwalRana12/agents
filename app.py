import streamlit as st
import pandas as pd
from modules.file_handler import load_csv_data, load_google_sheet_data
from modules.serp import get_search_results
from config.config import GOOGLE_SHEETS_API_KEY

def process_search_results(results_dict):
    """Handle the display and download of search results."""
    st.subheader("Search Results")
    
    if not results_dict:
        st.write("No results found.")
    
    for value, df in results_dict.items():
        with st.expander(f"Results for: {value}"):
            if not df.empty:
                st.write(f"Showing results for search term: {value}")
                st.dataframe(df) 
            else:
                st.write("No results found")

    
    if results_dict:
        all_results = pd.concat([df.assign(search_term=value) for value, df in results_dict.items()])
        csv = all_results.to_csv(index=False)
        st.download_button(
            label="Download All Results",
            data=csv,
            file_name="search_results.csv",
            mime="text/csv"
        )


def dynamic_query_input(data, main_column):
    """Handle query input and search execution."""
    prompt_template = st.text_input(
        "Enter your query template:", 
        placeholder=f"Search for {{{main_column}}}"
    )

    if prompt_template:
        st.write("Generated Query:")
        st.write(f"- {prompt_template}")
        
        if st.button("Run Search"):
            with st.spinner("Performing searches..."):
                results_dict = get_search_results(data, main_column, prompt_template)
                process_search_results(results_dict)

def handle_data_loading(data):
    """Process loaded data and display column selection."""
    if data is not None:
        st.write("Preview of the loaded data:")
        st.dataframe(data.head())
        
        main_column = st.selectbox(
            "Select the main column (e.g., company names):", 
            data.columns
        )
        st.write(f"Selected column: {main_column}")
        
        dynamic_query_input(data, main_column)
        return True
    return False

def upload_csv_file():
    """Handle CSV file upload."""
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = load_csv_data(uploaded_file)
        handle_data_loading(data)

def connect_to_google_sheets():
    """Handle Google Sheets connection."""
    sheet_url = st.text_input("Enter Google Sheets URL")
    if st.button("Load Google Sheet Data"):
        if sheet_url:
            data = load_google_sheet_data(sheet_url, GOOGLE_SHEETS_API_KEY)
            if not handle_data_loading(data):
                st.error("Failed to load Google Sheets data.")
        else:
            st.error("Please enter a valid Google Sheets URL.")

def main():
    """Main application function."""
    st.title("Dashboard for File Upload and Google Sheets Connection")

    option = st.sidebar.selectbox(
        "Data Input Source", 
        ("Upload CSV File", "Connect to Google Sheets")
    )

    if option == "Upload CSV File":
        st.subheader("Upload a CSV File")
        upload_csv_file()
    else:  # Connect to Google Sheets
        st.subheader("Connect to a Google Sheet")
        connect_to_google_sheets()

if __name__ == "__main__":
    main()
