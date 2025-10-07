import requests
import pandas as pd
from bs4 import BeautifulSoup

get_links = pd.read_csv("https://docs.google.com/spreadsheets/d/1nE_v4AFkLM76TdWcAbU1HRWgQ-gGKYa9ZMBbm7MM0V0/export?gid=0&format=csv")
get_links = get_links[['Kategori', 'Link']]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/', # The 'Referer' header tells the server where you came from
    'DNT': '1', # Do Not Track
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}
data = []
link_len = len(get_links['Link'])
try:
    for i, link in enumerate(get_links['Link'], start=1):
        response = requests.get(link, headers=headers)
        response.raise_for_status() 

        soup = BeautifulSoup(response.content, 'html.parser')
        article_title = soup.find('title').text if soup.find('title') else "Title not found"

        paragraphs = soup.find_all('p')
        article_text = "\n".join(list(map(lambda x : x.get_text(), paragraphs))) if paragraphs else "Article Content not Found"
        data.append((article_title, article_text))
        
        print(f"({i}/{link_len}) {link} SUCCESS")
    get_links[['article_title', 'article_text']] = data 
    get_links.to_csv("notebook/data/articles_raw.csv", index=False)
except requests.exceptions.RequestException as e:
    print(e)



