import os
import requests
import re
from typing import Dict, List
from dotenv import load_dotenv
import pandas as pd

class SearchClient:
    def __init__(self):
        """Initialize the search client with API key from environment variables."""
        load_dotenv()
        self.api_key = os.getenv('SERPAPI_KEY')
        if not self.api_key:
            raise ValueError("SERPAPI_KEY not found in environment variables")
        self.base_url = "https://serpapi.com/search"

    def process_query(self, data: pd.DataFrame, main_column: str, query_template: str) -> Dict[str, pd.DataFrame]:
        """
        Process search queries for each value in the specified column and print the results.
        
        Args:
            data (pd.DataFrame): Input dataframe containing the data
            main_column (str): Column name containing values to search
            query_template (str): Query template with {category} placeholder
            
        Returns:
            Dict[str, pd.DataFrame]: Dictionary mapping values to their formatted search results
        """
        results_dict = {}
        query_count = 0 
        for value in data[main_column]:
            if query_count >= 3: 
                break
            
           
            query = query_template.replace(f"{{category}}", str(value))
            results = self.search(query)
            formatted_results = self.extract_results(results)
            results_dict[value] = formatted_results
            
           
            print(f"Search results for {value}:")
            print(formatted_results)
            print()
            
            query_count += 1 
        
        return results_dict

    def search(self, query: str, location: str = "United States") -> List[Dict]:
        """
        Perform a Google search using SerpApi.
        
        Args:
            query (str): Search query
            location (str): Search location (default: United States)
            
        Returns:
            List[Dict]: List of search results
        """
        params = {
            "q": query,
            "location": location,
            "api_key": self.api_key,
            "engine": "google"
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            results = response.json()
            
            if "error" in results:
                raise Exception(f"API Error: {results['error']}")
            
            return results.get("organic_results", [])
            
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {str(e)}")
            return []
        except Exception as e:
            print(f"Error performing search: {str(e)}")
            return []

    @staticmethod
    def extract_results(results: List[Dict]) -> pd.DataFrame:
        """
        Extract useful information from search results.
        
        Args:
            results (List[Dict]): List of search results from SerpApi
            
        Returns:
            pd.DataFrame: DataFrame with relevant results
        """
        formatted_results = []
        
        # Extract information from the snippet and link (based on the query type)
        for result in results:
            snippet = result.get('snippet', '')
            link = result.get('link', '')
            formatted_results.append({
                'title': result.get('title', ''),
                'link': link,
                'snippet': snippet
            })
        
        # Return the results in a DataFrame
        return pd.DataFrame(formatted_results)

def get_search_results(data: pd.DataFrame, main_column: str, query_template: str) -> Dict[str, pd.DataFrame]:
    """
    Main function to get search results for a dataset.
    
    Args:
        data (pd.DataFrame): Input dataframe containing the data
        main_column (str): Column name containing values to search
        query_template (str): Query template with {category} placeholder
        
    Returns:
        Dict[str, pd.DataFrame]: Dictionary mapping values to their formatted search results
    """
    try:
        client = SearchClient()
        return client.process_query(data, main_column, query_template)
    except Exception as e:
        print(f"Error in get_search_results: {str(e)}")
        return {}
