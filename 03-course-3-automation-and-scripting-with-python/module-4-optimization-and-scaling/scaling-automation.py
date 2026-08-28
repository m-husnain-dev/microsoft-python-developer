import concurrent.futures
import requests

def fetch_data(api_url):
    """Fetches data from a given API URL."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return None

if __name__ == "__main__":
    api_urls = [
        "https://api.example.com/data1",
        "https://api.another-example.com/data2",
        "https://api.yet-another-example.com/data3"
        # Add more API URLs as needed
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit API requests concurrently
        future_to_url = {executor.submit(fetch_data, url): url for url in api_urls}

        # Process results as they become available
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()   
                if data:
                    print(f"Data from {url}: {data}")
            except Exception as exc:
                print(f"Exception while fetching data from {url}: {exc}")