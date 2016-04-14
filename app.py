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

@app.route('/queensland')	
def get_qld():
    url = "http://www.bom.gov.au/climate/dwo/IDCJDW0400.shtml"
    stations_a_z = get_station_links_a_z(url) 
    
    return render_template('qld.html', stations_a_z=stations_a_z)
 

@app.route('/south_australia')
def get_sa():
   url = "http://www.bom.gov.au/climate/dwo/IDCJDW0500.shtml"
   stations_a_z = get_station_links_a_z(url) 

   return render_template('sa.html', stations_a_z=stations_a_z)
	
@app.route('/western_australia')
def get_wa():
    url = "http://www.bom.gov.au/climate/dwo/IDCJDW0600.shtml"
    stations_a_z = get_station_links_a_z(url) 
    
    return render_template('wa.html', stations_a_z=stations_a_z)
	
@app.route('/act')
def get_act():
    url = "http://www.bom.gov.au/climate/dwo/IDCJDW0100.shtml"
    stations_a_z = get_station_links_a_z(url) 
    
    return render_template('act.html', stations_a_z=stations_a_z)
	
@app.route('/tasmania')
def get_tas():
    url = "http://www.bom.gov.au/climate/dwo/IDCJDW0700.shtml"
    stations_a_z = get_station_links_a_z(url) 
    
    return render_template('tas.html', stations_a_z=stations_a_z)
	
@app.route('/northern_territory')
def get_nt():
    url = "http://www.bom.gov.au/climate/dwo/IDCJDW0800.shtml"
    stations_a_z = get_station_links_a_z(url) 
    
    return render_template('nt.html', stations_a_z=stations_a_z)
	
@app.route('/antarctica')
def get_antarctica():
    url = "http://www.bom.gov.au/climate/dwo/IDCJDW0920.shtml"
    stations_a_z = get_station_links_a_z(url) 
    
    return render_template('antarctica.html', stations_a_z=stations_a_z)
	

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
    
    content = soup.find('tbody')
    content = content.find_all('tr')
    
    for con in content:
        date = con.find('th').get_text()
        td = con.find_all('td')
        day = td[0]
        min_temp = td[1]
        

        print "date: " + date
        print "day:" + day
        print "min_temp" + min_temp
        print '\n'
         
    

    return content


if __name__ == "__main__":
    app.run(debug=True, port=5001)
