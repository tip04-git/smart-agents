import requests

def fetch_web_data(query):
    """Fetch real-time data from Wikipedia's OpenSearch API for better accuracy."""
    search_url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={query.replace(' ', '_')}&limit=1&format=json"

    try:
        response = requests.get(search_url)
        print(f"🟡 DEBUG: Wikipedia API Response Code → {response.status_code}")

        if response.status_code != 200:
            return "No relevant data found"

        data = response.json()
        if not data[1]:  # If no relevant title found
            print("🟡 DEBUG: No relevant Wikipedia results found!")
            return "No relevant data found"

        top_result_title = data[1][0]  # Get the best match
        print(f"🟡 DEBUG: Best Wikipedia Match → {top_result_title}")

        # Fetch summary from Wikipedia
        summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{top_result_title.replace(' ', '_')}"
        summary_response = requests.get(summary_url)

        if summary_response.status_code != 200:
            return "No relevant data found"

        summary_data = summary_response.json()
        if "extract" in summary_data:
            print(f"🟡 DEBUG: Extracted Wikipedia Data → {summary_data['extract'][:200]}...")  # Print first 200 chars
            return summary_data["extract"]

        return "No relevant data found"
    
    except requests.exceptions.RequestException as e:
        print(f"❌ DEBUG: Wikipedia API Error → {str(e)}")
        return "Error fetching data"

# Example Test
if __name__ == "__main__":
    print(fetch_web_data("Solar panel"))
