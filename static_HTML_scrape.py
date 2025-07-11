import requests
from bs4 import BeautifulSoup
from KW_eng import keyword_search

def static_scraper(url, keywords, mode='partial'):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f'Error fetching: {e}')
        return {}

    soup = BeautifulSoup(response.text, 'lxml')
    paragraphs = soup.find_all('p')
    all_text = " ".join(p.get_text(separator=" ", strip=True) for p in paragraphs)

    results = keyword_search(all_text, keywords, mode=mode)
    return results