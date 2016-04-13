#!/usr/bin/python
from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
import requests
import re
import json

app = Flask(__name__)


@app.route('/')
def home():
    station_url = request.args.get('station_url')

    return render_template('index.html')


@app.route('/victoria')
def get_victoria():
    url = "http://www.bom.gov.au/climate/dwo/IDCJDW0300.shtml"
    stations = get_stations(url) 
    
    return render_template('victoria.html', stations=stations)


def get_stations(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    
    content = soup.find_all('a')
   
    links = []
    for con in content:
        link = con.get('href')
        link = re.search(r'climate/dwo/I(.*)', link)
        if link:
            found_link = link.group(0)
            
            item = { 
                    'url': found_link,
            }

            links.append(item)

    all_links = []
    for link in links:
        link = "http://www.bom.gov.au/" + link['url']
        page = requests.get(link)
        soup = bs(page.text, 'html.parser')
        
        content = soup.find('div', {'class': 'content'})
        content = content.find_all('a')
        
        for con in content:
            link = con.get('href') 
            link = re.search(r'(.*)latest.shtml', link)
            if link:
                location = con.get_text()
                found_link = link.group(0)
                
                item = {
                        'loction': location,
                        'url': found_link,
                }
            
                all_links.append(item)
    
    return all_links


if __name__ == "__main__":
    app.run(debug=True)
