import os 
import requests
from bs4 import BeautifulSoup
import csv

def cnn_headlines_func(url):
    """ This function gets request from CNN homepage, scraps using BeautifulSoup
      and returns its headline and description"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = [headline.text.strip() for headline in soup.find_all('item')]
            descriptions = [description.text.strip() for description in soup.find_all('item')]
            return headlines, descriptions
        else:
            return print("CNN data extraction failure,", response.status_code)
    except Exception as e:
        return print("Error occured:", e)

def save_to_csv(headlines, descriptions, file_name):
    """ This function stores the healines and description in csv file"""
    try:
        cwd = os.getcwd() # Get the current working directory
        file_path = os.path.join(cwd, file_name)
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Headline', 'description'])
            for headline, description in zip(headlines, descriptions):
                writer.writerow([headline, description])
        print("Data saved to", file_path)
    except Exception as e:
        print("Error saving data to CSV:", e)


cnn_urls_and_filenames = {
    'http://rss.cnn.com/rss/cnn_topstories.rss': 'cnn_topstories.csv',
    'http://rss.cnn.com/rss/cnn_us.rss': 'cnn_us.csv'
}
# Loop through each CNN feed URL and filename pair, scrape headlines and descriptions, and save them to CSV
for cnn_url, file_name in cnn_urls_and_filenames.items():
    headlines, descriptions = cnn_headlines_func(cnn_url)
    if headlines and descriptions:
        save_to_csv(headlines, descriptions, file_name)
