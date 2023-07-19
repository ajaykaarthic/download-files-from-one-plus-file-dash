from bs4 import BeautifulSoup
import requests

html = open("download.html","r")

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all anchor tags (links)
anchor_tags = soup.find_all('a')

# Download the links
for tag in anchor_tags:
    link = tag.get('href')
    if link.startswith('/'):  # Handle relative URLs
        link = 'http://192.168.153.212:5678' + link
    response = requests.get(link)
    if response.status_code == 200:
        filename = link.split('/')[-1]  # Extract the filename from the URL
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {link}")
