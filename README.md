# Web Keyword Finder
This project is a web scraper that allows you to check if certain keywords exist in the desired webpages, as well as detailing how many times they appear

## Project Description
The app allows users to:
  Enter any URL
  Provide multiple keywords to search
  Choose between different matching modes (partial, whole, or exact)
  Select whether to scrape with requests + BeautifulSoup or with a full browser engine (Playwright)

## File Overview
### 'main.py'
The main Streamlit frontend app
Provides user interface for entering URL, keywords, search mode, and scraper engine
Calls the backend scraper functions and displays results interactively

### 'static_HTML_scrape.py'
Static scraper module
Uses requests to fetch webpages and BeautifulSoup to parse HTML with lxml
Extracts <p> text and sends it the keyword search engine from main.py

### 'js_HTML_scrape.py'
Scraper module for JavaScript rendered HTML
Uses Playwright to extract all <p> text and send it to the keyword search engine

### 'KW_eng.py'
The resuable keyword search engine
Handles flexible matching of keywords from extracted text
Three match modes
    'partial': matches substrings anywhere (case-insensitive)
    'whole': matches full words only (case-insensitive)
    'exact': matches exact chararacter sequence (case-sensitive)
## Technology used
Python 3
  Requests
  BeautifulSoup
  Playwright
  Regex
Streamlit
Lxml
