#!/usr/bin/python
######################################################
# Orignally written by: Dave McPherson, 2017
# https://github.com/DMcP89/StorjShareStatusChecker
#######################################################

import demjson
import requests
import sys
import ConfigParser
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
#print d

config = ConfigParser.ConfigParser()
config.read(d+"/conf/properties.ini")



### Local Functions ####
def parseStorjStats(stats):
 parsed_result = demjson.decode(stats.replace("[","").replace("]",""))
 return parsed_result

def sendIFTTTRequest(json):
 key = config.get('IFTTTKey', 'KEY')
 url = 'https://maker.ifttt.com/trigger/storjcheck/with/key/'+key
 response = requests.post(url, data=json)
 return response

########################

def main(stats):
 input = parseStorjStats(stats)
 value1 = str(input[config.get('StorjValues', 'v1')])
 value2 = str(input[config.get('StorjValues', 'v2')])
 value3 = str(input[config.get('StorjValues', 'v3')])
 json = {"value1" : value1, "value2" : value2, "value3" : value3} 
 sendIFTTTRequest(json) 
 return

#print sys.argv[1]
main(sys.argv[1])
