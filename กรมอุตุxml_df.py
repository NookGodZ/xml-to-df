import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import requests
import bs4
URL = 'https://data.tmd.go.th/api/doc/xml/ThailandMonthlyRainfall.xml'
data_list = []
response = urllib.request.urlopen(urllib.request.Request(URL))
data_xml = BeautifulSoup(response,'lxml-xml')
data_text = data_xml.text
start = 0
raw =''
for i in range(len(data_text)):
    if start == 1 :
        if data_text[i] == '\n':
            start = 0
            if raw == '' :
                pass
            else:
                data_list.append(raw)
            raw =''
        else:
            raw += data_text[i]
    if data_text[i] == '\n' :
        start = 1
df = pd.DataFrame([data_list])