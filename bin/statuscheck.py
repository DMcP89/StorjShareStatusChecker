#!/usr/bin/python
######################################################
# Orignally written by: Dave McPherson, 2017
# https://github.com/DMcP89/StorjShareStatusChecker
#######################################################

import demjson
import requests
import subprocess
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("conf/properties.ini")



### Local Functions ####
def runStorjShareStatus():
 result = subprocess.check_output(['storjshare-status', '-j'])
 parsed_result = demjson.decode(result.replace("[","").replace("]",""))
 return parsed_result

def sendIFTTTRequest(json):
 key = config.get('IFTTTKey', 'KEY')
 url = 'https://maker.ifttt.com/trigger/storjcheck/with/key/'+key
 response = requests.post(url, data=json)
 return response

########################

def main():
 result = subprocess.check_output(['storjshare-status', '-j'])
 input = runStorjShareStatus()
 value1 = str(input[config.get('StorjValues', 'v1')])
 value2 = str(input[config.get('StorjValues', 'v2')])
 value3 = str(input[config.get('StorjValues', 'v3')])
 json = {"value1" : value1, "value2" : value2, "value3" : value3} 
 sendIFTTTRequest(json) 
 return

main()
