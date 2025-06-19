from playwright.async_api import async_playwright
from bs4 import BeautifulSoup as Bs
from KW_eng import keyword_search

async def playwright_scraper(url, keywords, mode='partial'):
    async with async_playwright() as ap:
        browser = await ap.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, timeout=5000)
        html = await page.content()
        await browser.close()
    soup = Bs(html, 'lxml')
    paragraphs = soup.find_all('p')
    all_text = " ".join([p.get_text(separator=" ", strip=True) for p in paragraphs])
    results = keyword_search(all_text, keywords, mode=mode)
    return results