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

@app.route('/projectpage')
def get_projectpage():

        return render_template('projectpage.html')
	


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

    return json.dumps(data)


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
    
    scraped = []
    
    for con in content:
        date = con.find('th').get_text()
        td = con.find_all('td')
     
        day = td[0].get_text()
        minT = td[1].get_text()
        maxT = td[2].get_text()
        
        rain = td[3].get_text()
        evap = td[4].get_text()
        sun = td[5].get_text()
       
        dirW = td[6].get_text()
        spdW = td[7].get_text()
        timeW = td[8].get_text()
    
        temp9 = td[9].get_text()
        rh9 = td[10].get_text()
        cld9 = td[11].get_text()
        dir9 = td[12].get_text()
        spd9 = td[13].get_text()
        mslp9 = td[14].get_text()
        
        temp3 = td[15].get_text()
        rh3 = td[16].get_text()
        cld3 = td[17].get_text()
        dir3 = td[18].get_text()
        spd3 = td[19].get_text()
        mslp9 = ""
        try: 
            mslp3 = td[20].get_text()
        except:
            pass
            
        item = {
            "date": date,
            "day": day,
            "minT": minT,
            "maxT": maxT,
            "rain": rain,
            "evap": evap,
            "sun": sun,
            "dirW": dirW,
            "spdW": spdW,
            "timeW": timeW,
            "temp9": temp9,
            "rh9": rh9,
            "cld9": cld9,
            "dir9": dir9,
            "spd9": spd9,
            "mslp9": mslp9,
            "temp3": temp3,
            "rh3": rh3,
            "cld3": cld3,
            "dir3": dir3,
            "spd3": spd3,
            "mslp3": mslp3
        }
        scraped.append(item)
        
    return scraped


if __name__ == "__main__":
    app.run(debug=True, port=5001)
