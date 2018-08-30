#!/usr/bin/env python3
# ShibaSearch.py - Goes to imgur.com and downloads random pictures of "Shiba Inus"

import requests, os, bs4

url = 'https://imgur.com' # starting url
os.makedirs('shiba', exist_ok=True) # store pictures in ./shiba
while not url.endswith('#'):
    pass

#TODO: Download The Page
#TODO: Find URL of shiba image
#TODO: Download the Image
#TODO: Save image to ./shiba

print('Done.')