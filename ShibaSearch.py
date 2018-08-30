#!/usr/bin/env python3
# ShibaSearch.py - Goes to imgur.com and downloads random pictures of "Shiba Inus"

import requests, os, bs4, urllib

url = 'https://imgur.com/search?q=shiba%20inu' # starting url
os.makedirs('shiba', exist_ok=True) # store pictures in ./shiba
while not url.endswith('#'):
    # TODO: Download the page.
    print ('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    # TODO: Find The URL of the Shiba Image
    counter = 0
    for img in soup.find_all('img'):
        with open("image" + str(counter), 'wb') as f:
            f.write(urllib.request.urlopen(img['src']).read())
        counter += 1
print('Done.')