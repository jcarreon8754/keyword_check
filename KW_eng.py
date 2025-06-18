import re

def keyword_search(text, keywords, mode='partial'):
    results = {}

    for keyword in keywords:
        keyword_clean = keyword.strip()
        if mode == 'partial':
            count = len(re.findall(re.escape(keyword_clean), text, re.IGNORECASE))
        elif mode == 'whole':
            pattern = r'\b' + re.escape(keyword_clean) + r'\b'
            count = len(re.findall(pattern, text, re.IGNORECASE))
        elif mode == 'exact':
            count = text.count(keyword_clean)
        else:
            raise ValueError('Unknown mode')
        results[keyword_clean] = count
    return results