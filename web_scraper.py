import sys
import requests
from bs4 import BeautifulSoup


def find_integration_pages(url: str) -> list[str]:
        links = []
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
        try:
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            soup = BeautifulSoup(r.content, 'lxml' if 'lxml' in sys.modules else 'html.parser')
            for link in soup.find_all('a'):
                links.append(link.get('href'))
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        return links


def extract_text_from_website(website: str) -> str:
    text = ""
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    try:
        r = requests.get(website, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.content, 'lxml' if 'lxml' in sys.modules else 'html.parser')
        for element in soup.find_all(["p", "em", "div", "h1"], class_=['entry-title mw-medium', 'description mw-medium', "grid-container medium"]):
            text += str(element.get_text()) + ". "
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return text