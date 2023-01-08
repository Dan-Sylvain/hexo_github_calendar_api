# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler
import json

def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]
    
    
    
def getdata(name):
    gitpage = requests.get("https://github.com/" + name)
    data = gitpage.text
    # print('---------------------------------------')
#     print(data)
#     print('---------------------------------------')
    datadatereg = re.compile(r'data-date="(.*?)" data-level')
    # datacountreg = re.compile(r'data-count="(.*?)" data-date')
    # datacountreg = re.compile(r'>"(.*?)" contribution on')
    datacountreg = re.compile(r'(\d+)\s+contributio')
    datacountreg = re.compile(r'ry="2">(.+?) contributions')
    datadate = datadatereg.findall(data)
    print(datadate)
 
    datacount = datacountreg.findall(data)

    datacount = [x if x !='No' else '0' for x in datacount]
    print(datacount)  
    
    datacount = list(map(int, datacount))
    print(datacount)
    contributions = sum(datacount)
    print(contributions)
    datalist = []

    for index, item in enumerate(datadate):
        itemlist = {"date": item, "count": datacount[index]}
        datalist.append(itemlist)
    datalistsplit = list_split(datalist, 7)
    returndata = {
        "total": contributions,
        "contributions": datalistsplit
    }
    return returndata
    

    
def findbug():
    path='https://github.com/api?Dan-Sylvain'
    print(path)
    user = path.split('?')[1]
    print(user)
    data = getdata(user)
    print(data)
   
  
getdata('Dan-Sylvain')   
# findbug()
        
    
    
# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         path = self.path
#         user = path.split('?')[1]
#         data = getdata(user)
#         self.send_response(200)
#         self.send_header('Access-Control-Allow-Origin', '*')
#         self.send_header('Content-type', 'application/json')
#         self.end_headers()
#         self.wfile.write(json.dumps(data).encode('utf-8'))
#         return
