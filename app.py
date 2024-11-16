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
        return
    
    for query, df in results_dict.items():
        with st.expander(f"Results for query: {query}"):
            if not df.empty:
                st.write(f"Search results for: {query}")
                st.dataframe(df)
            else:
                st.write("No results found")
    
    if results_dict:
        # Combine all results with query information
        all_results = []
        for query, df in results_dict.items():
            if not df.empty:
                df = df.copy()
                df['search_query'] = query
                all_results.append(df)
        
        if all_results:
            combined_results = pd.concat(all_results, ignore_index=True)
            csv = combined_results.to_csv(index=False)
            st.download_button(
                label="Download All Results",
                data=csv,
                file_name="search_results.csv",
                mime="text/csv"
            )

def execute_search(data, main_column, query_template):
    """Execute search with the exact query template."""
    results_dict = {}
    
    # Get unique values from the selected column
    unique_values = data[main_column].unique()
    
    with st.status("Performing searches...") as status:
        total = len(unique_values)
        for i, value in enumerate(unique_values, 1):
            # Format the query template with the current value
            formatted_query = query_template.replace(f"{{{main_column}}}", str(value))
            status.update(label=f"Searching {i}/{total}: {formatted_query}")
            
            try:
                # Call SERP API with the formatted query
                results = get_search_results(formatted_query)  # This should be your actual SERP API call
                results_dict[formatted_query] = results
            except Exception as e:
                st.error(f"Error searching for '{formatted_query}': {str(e)}")
    
    return results_dict

def dynamic_query_input(data, main_column):
    """Handle query input and search execution."""
    query_template = st.text_input(
        "Enter your query template:", 
        placeholder=f"Example: what is the name of this {{{main_column}}}"
    )

    if query_template:
        st.write("Generated Query:")
        # Show an example of how the query will look
        example_value = data[main_column].iloc[0] if not data.empty else "example"
        example_query = query_template.replace(f"{{{main_column}}}", str(example_value))
        st.write(f"* {example_query}")
        
        if st.button("Run Search"):
            results = execute_search(data, main_column, query_template)
            process_search_results(results)

def handle_data_loading(data):
    """Process loaded data and display column selection."""
    if data is not None:
        st.write("Preview of the loaded data:")
        st.dataframe(data.head())
        
        main_column = st.selectbox(
            "Select the column containing search terms:", 
            data.columns
        )
        
        if main_column:
            st.write(f"Selected column: {main_column}")
            unique_values = data[main_column].unique()
            st.write(f"Found {len(unique_values)} unique values in {main_column}")
            
            dynamic_query_input(data, main_column)
            return True
    return False

def upload_csv_file():
    """Handle CSV file upload."""
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        try:
            data = load_csv_data(uploaded_file)
            handle_data_loading(data)
        except Exception as e:
            st.error(f"Error loading CSV: {str(e)}")

def connect_to_google_sheets():
    """Handle Google Sheets connection."""
    sheet_url = st.text_input("Enter Google Sheets URL")
    if st.button("Load Google Sheet Data"):
        if sheet_url:
            try:
                data = load_google_sheet_data(sheet_url, GOOGLE_SHEETS_API_KEY)
                if not handle_data_loading(data):
                    st.error("Failed to load Google Sheets data.")
            except Exception as e:
                st.error(f"Failed to load Google Sheet: {str(e)}")
        else:
            st.error("Please enter a valid Google Sheets URL.")

def main():
    """Main application function."""
    st.title("Search Query Builder")

    option = st.sidebar.selectbox(
        "Data Input Source", 
        ("Upload CSV File", "Connect to Google Sheets")
    )

    if option == "Upload CSV File":
        st.subheader("Upload a CSV File")
        upload_csv_file()
    else:
        st.subheader("Connect to a Google Sheet")
        connect_to_google_sheets()

if __name__ == "__main__":
    main()