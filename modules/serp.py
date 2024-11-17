import os
import requests
import pandas as pd
from typing import Dict, List, Optional
from dotenv import load_dotenv
import json

class SearchClient:
    def __init__(self):
      
        load_dotenv()
        self.api_key = os.getenv('SERPAPI_KEY')
        if not self.api_key:
            raise ValueError("SERPAPI_KEY not found in environment variables")
        self.base_url = "https://serpapi.com/search"

    def search(self, query: str, location: str = "United States") -> List[Dict]:
       
        params = {
            "q": query,
            "location": location,
            "api_key": self.api_key,
            "engine": "google"
        }

        try:
            print(f"\nMaking request to SerpAPI:")
            print(f"URL: {self.base_url}")
            print(f"Query: {query}")
            
            response = requests.get(self.base_url, params=params, timeout=30)
            print(f"Response status code: {response.status_code}")
            
            if response.status_code != 200:
                print(f"Error response from API: {response.text}")
                return []

            results = response.json()
            print("API Response structure:")
            print(json.dumps(list(results.keys()), indent=2))
            
            if "error" in results:
                raise Exception(f"API Error: {results['error']}")

            organic_results = results.get("organic_results", [])
            print(f"Found {len(organic_results)} organic results")
            
            return organic_results
            
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {str(e)}")
            return []
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {str(e)}")
            print(f"Response content: {response.text[:200]}...") 
            return []
        except Exception as e:
            print(f"Error performing search: {str(e)}")
            return []

    @staticmethod
    def extract_results(results: List[Dict]) -> pd.DataFrame:
       
        formatted_results = []

        for result in results:
            formatted_results.append({
                'title': result.get('title', ''),
                'link': result.get('link', ''),
                'snippet': result.get('snippet', ''),
                'position': result.get('position', None),
                'domain': result.get('domain', '')
            })

        return pd.DataFrame(formatted_results)

def get_search_results(query: str) -> pd.DataFrame:
    """
    Main function to get search results for a single query.
    Returns a DataFrame of results.
    """
    try:
        client = SearchClient()
        results = client.search(query)
        if results:
            return client.extract_results(results)
        return pd.DataFrame()
    except Exception as e:
        print(f"Error in get_search_results: {str(e)}")
        return pd.DataFrame()