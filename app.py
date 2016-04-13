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


@app.route('/stations', methods=['GET'])
def get_stations():
    text = request.query_string
    
    stations = get_stations_links(text)

    return text


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


def get_all_station_links(url):   
    page = request.get(url)
    soup = bs(page.text, 'html.parser')

    return all_links


if __name__ == "__main__":
    app.run(debug=True)
