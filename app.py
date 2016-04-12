#!/usr/bin/python
from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
import requests
import re
import json
from time import sleep

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/victoria')
def get_victoria():
    url = "http://www.bom.gov.au/climate/dwo/IDCJDW0300.shtml"
    stations_a_z = get_station_links_a_z(url)
    
    return render_template('victoria.html', stations_a_z=stations_a_z)


@app.route('/new_south_wales')
def get_nsw():
    url = "http://www.bom.gov.au/climate/dwo/IDCJDW0200.shtml"
    stations_a_z = get_station_links_a_z(url) 
    
    return render_template('nsw.html', stations_a_z=stations_a_z)


# called from the site to return sation locations as json. 
@app.route('/stations', methods=['GET'])
def get_stations():
    url = request.query_string
    
    links = get_station_links(url)
    
    return json.dumps(links)


# called from the site to return station info as json.
@app.route('/stations_info', methods=['GET'])
def get_stations_info():
    url = request.query_string
    
    data = get_station_data(url)

    print url

    return "hello"


# returns the links to pages that contain the stations,  A-C, D-E, ect
def get_station_links_a_z(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    
    content = soup.find('h2')
    content = content.find_all('a')
    
    links_a_z = []
    for con in content:
        link = con.get('href')
        link = re.search(r'climate/dwo/I(.*)', link)
        
        if link:
            found_link = link.group(0)
            letter = con.get_text()
            
            item = {
                    'letter': letter,
                    'url': found_link,
            }

            links_a_z.append(item)
    
    return links_a_z 


# returns all the links 
def get_station_links(url):  
    url = "http://bom.gov.au/" + url
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    
    content = soup.find('div', {'class': 'content'})
    content = content.find_all('th', {'scope': 'row'})
    
    links = []
    for con in content:
        station_name = con.get_text()
        url = con.find('a').get('href')
        
        item = {
                'station_name': station_name,
                'url': url,
        }
        
        links.append(item)
    

    return links


def get_station_data(url):
    url = "http://bom.gov.au/" + url
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    
    content = soup.find('table', {'class':'data'})
    print content
    
    return content


if __name__ == "__main__":
    app.run(debug=True, port=5001)
    
