from flask import Flask, jsonify, render_template, request
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import time
from selenium import webdriver

app = Flask(__name__)

@app.route('/')
def getMain():
    return render_template('DownloadVideos.html')

@app.route('/main', methods = ['POST', 'GET'])
def getURL():
    url = request.form['flink']
    driver = webdriver.Chrome('C:\chromedriver')
    driver.get(url)
    page = driver.page_source
    Soup = BeautifulSoup(page, 'html.parser')
    html = ''
    vid = Soup.find_all('iframe', {"class": "metaframe rptss"})
    videos = {}
    videos['videos'] = []
    lista = list()
    for i in vid:
        html = i['src']
    print(html)
    if html != "":
        driver2 = webdriver.Chrome('C:\chromedriver')
        driver2.get(html)
        page2 = driver2.page_source
        Soup2 = BeautifulSoup(page2, 'html.parser')
        video = Soup2.find_all('video', {"class":"jw-video jw-reset"})
        
        for j in video:
            videos['videos'].append(
                {"url": j['src']
            })
            lista.append(j['src'])
    return "<video id = 'video' width='852' height='480' controls> <source id = 'ruta'  type = 'video/mp4' src = '"  + lista[0] +"'></video>"


if __name__ == "__main__":
    app.run(debug=True)