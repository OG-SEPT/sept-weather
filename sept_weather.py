#!/usr/bin/python
from flask import Flask, render_template, request, g
from bs4 import BeautifulSoup as bs
import requests
import re
import json
import sqlite3
from time import sleep
from geopy.geocoders import Nominatim
import urllib2

app = Flask(__name__)

#######################################################
# Database handling below
#######################################################

# for database connection
@app.before_request
def before_request():
    g.db = sqlite3.connect("data/septweather_db")


# for database close connection
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


########################################################
# page routes handled below
########################################################

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/favorite')
def favorites():
    favorite = g.db.execute("SELECT url, name FROM Favorites").fetchall()

    return render_template('favorite.html', favorite=favorite) 
    

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
    url = "climate/dwo/IDCJDW0100.shtml"
    stations_links = get_station_links(url) 
    
    return render_template('act.html', stations_links=stations_links)


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
    url = "climate/dwo/IDCJDW0920.shtml"
    stations_links = get_station_links(url) 
    
    return render_template('antarctica.html', stations_links=stations_links)


@app.route('/projectpage')
def get_projectpage():

    return render_template('projectpage.html')
        

@app.route('/chart')
def chart():
    
    return render_template('chart.html')
	

##############################################################
# Our API is handled below
##############################################################

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


# adds a station to favorite
@app.route('/station_fav', methods=['GET'])
def add_favorite():
    url = request.args.get('url')
    name = request.args.get('name')
    
    g.db.execute("INSERT INTO Favorites (url, name) VALUES (?, ?);", [url, name])
    g.db.commit()

    return json.dumps(url)


@app.route('/reset_database', methods=['GET'])
def reset_database():
    g.db.execute("DELETE FROM Favorites;")
    g.db.commit()
    
    return "Successful Reset"


# adds a station to favorite
@app.route('/forecast', methods=['GET'])
def get_forecast():
    name = request.args.get('name')
    
    location = getCoordinates(name)
    print "name: "+ name
    print "locataion: "+location
    return location
    

##########################################################
# Utility functions for scraping data below
##########################################################

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
        mslp3 = ""
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
    
    
# geopy module
def getCoordinates(location):
    geolocator = Nominatim()
    geoLocation = geolocator.geocode(location)
    
    coordinates = [geoLocation.latitude, geoLocation.longitude]
    
    return coordinates
    
def callForecastApi(coordinates):
    # call the api url
    forcastKey = "29ada930e694bf8f1b277802c4dc5b82"
    url = "https://api.forecast.io/forecast/"+forcastKey+"/"+str(coordinates[0])+","+str(coordinates[1])
    response = urllib2.urlopen(url)
    
    # store the json data
    json = response.read()
    json_data = json.loads(json)
    
    # stores list of lists of forecast data
    forecast_daily = []
    
    for row in range(7)):
        # assigning relevant values to variables
        time = json_data['daily']['data'][row]['time']
        summary = json_data['daily']['data'][row]['summary']
        icon = json_data['daily']['data'][row]['icon']
        sunriseTime = json_data['daily']['data'][row]['sunriseTime']
        sunsetTime = json_data['daily']['data'][row]['sunsetTime']
        moonPhase = json_data['daily']['data'][row]['moonPhase']
        preciIntensity = json_data['daily']['data'][row]['preciIntensity']
        preciIntensityMax = json_data['daily']['data'][row]['preciIntensityMax']
        preciIntensityMaxTime = json_data['daily']['data'][row]['preciIntensityMaxTime']
        preciProbability = json_data['daily']['data'][row]['preciProbability']
        precipType = json_data['daily']['data'][row]['precipType']
        temperatureMin = json_data['daily']['data'][row]['temperatureMin']
        temperatureMinTime = json_data['daily']['data'][row]['temperatureMinTime']
        temperatureMax = json_data['daily']['data'][row]['temperatureMax']
        temperatureMaxTime = json_data['daily']['data'][row]['temperatureMaxTime']
        apparentTemperatureMin = json_data['daily']['data'][row]['apparentTemperatureMin']
        apparentTemperatureMinTime = json_data['daily']['data'][row]['apparentTemperatureMinTime']
        apparentTemperatureMax = json_data['daily']['data'][row]['apparentTemperatureMax']
        apparentTemperatureMaxTime = json_data['daily']['data'][row]['apparentTemperatureMaxTime']
        dewPoint = json_data['daily']['data'][row]['dewPoint']
        humidity = json_data['daily']['data'][row]['humidity']
        windSpeed = json_data['daily']['data'][row]['windSpeed']
        windBearing = json_data['daily']['data'][row]['windBearing']
        cloudCover = json_data['daily']['data'][row]['cloudCover']
        pressure = json_data['daily']['data'][row]['pressure']
        ozone = json_data['daily']['data'][row]['ozone']
        
        forecast_daily.append(time, summary, icon, sunriseTime, sunsetTime, moonPhase, preciIntensity, preciIntensityMax, preciIntensityMaxTime, preciProbability, precipType, temperatureMin, temperatureMax, apparentTemperatureMin, apparentTemperatureMinTime, apparentTemperatureMax, apparentTemperatureMaxTime, dewPoint, humidity, windSpeed, windBearing, cloudCover, pressure, ozone)

    return forecast_daily

#ownKey = "5c34314ddb1be6e455c7de090a947858";  

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    
