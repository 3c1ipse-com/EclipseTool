import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from colorama import Fore, Back, Style, init

def get_links(url):
    domain = urlparse(url).netloc
    visited = set()
    to_visit = set([url])
    all_links = set()

    while to_visit:
        current_url = to_visit.pop()
        if current_url in visited:
            continue

        try:
            response = requests.get(current_url)
            visited.add(current_url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {current_url}: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(current_url, href)
            parsed_url = urlparse(full_url)

            if href.startswith("javascript:"):
                continue

            if parsed_url.netloc == domain:
                if full_url not in visited:
                    to_visit.add(full_url)
            all_links.add(full_url)

    print(f"{Fore.GREEN}All links in {url}:{Style.RESET_ALL} \n=========================")

    for link in all_links:
        print(f"{Fore.BLUE}{link}{Style.RESET_ALL}")
