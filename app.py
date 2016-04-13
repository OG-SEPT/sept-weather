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
    return render_template('victoria.html')


@app.route('/api/get_weather', methods=['POST'])
def get_weather():
    station_url = request.get('station_url', '')
    print station_url

    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    answer = question

    return json.dumps({'answer': answer})


if __name__ == "__main__":
    app.run(debug=True)
