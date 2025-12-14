import requests
import pandas as pd
import selenium.webdriver as webdriver

get_links = pd.read_csv("https://docs.google.com/spreadsheets/d/1nE_v4AFkLM76TdWcAbU1HRWgQ-gGKYa9ZMBbm7MM0V0/export?gid=0&format=csv")
get_links = get_links[['Kategori', 'Link', 'Label Sentimen']]