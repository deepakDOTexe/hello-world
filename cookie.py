#!/usr/bin/env python

import requests

url = 'http://172.19.14.89/newlife/'

cookies = {'Upset' : 'True'}

r = requests.get(url, cookies = cookies)

print (r.text)