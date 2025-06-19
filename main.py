import streamlit as st
import asyncio
from static_HTML_scrape import static_scraper
from js_HTML_scrape import playwright_scraper
from KW_eng import keyword_search

st.title("Web Keyword Scraper")

url  = st.text_input("Enter URL to scrape:")
keywords_input = st.text_input("Enter keywords (comma separated):")
mode = st.selectbox("Search Mode", ['partial', 'whole', 'exact'])
engine = st.radio("Select Scraper Engine:", ["Static (requests + bs4)", "JS-rendered (Playwright"])

if st.button("Run Scraper"):
    if not url or not keywords_input:
        st.warning("Please enter both URL and keywords")
    else:
        keywords = [k.strip() for k in keywords_input.split(',')]
        if engine == "Static (requests + bs4)":
            st.write("Checking static HTML...")
            results = static_scraper(url, keywords, mode)
        else:
            st.write("Checking Dynamic HTML Loads...")
            results = asyncio.run(playwright_scraper(url, keywords, mode))

        st.subheader("Results:")
        for keyword, count in results.items():
            st.write(f"**{keyword}**: {count} matches")