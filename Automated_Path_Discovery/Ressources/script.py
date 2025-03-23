import requests
from bs4 import BeautifulSoup

BASE_URL = "http://10.11.100.236/.hidden/"

visited = set()

def crawl(url, depth=0, max_depth=10):
    """Recursively visit each path until the flag is found."""
    if url in visited or depth > max_depth:
        return
    
    visited.add(url)
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return
        
        # Check if the page contains the flag
        if "flag" in response.text.lower():
            print(f"Flag found at: {url}")
            print(response.text)
            return

        # Parse links from the page
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and not href.startswith(".."):  # Ignore parent directory links
                crawl(url + href, depth + 1)

    except Exception as e:
        print(f"Error visiting {url}: {e}")

# Start crawling
print("Looking for the flag...")
crawl(BASE_URL)
