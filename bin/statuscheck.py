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
# print d

config = ConfigParser.ConfigParser()
config.read(d + "/conf/properties.ini")


# Local Functions
def parse_storj_stats(stats):
    parsed_result = demjson.decode(stats.replace("[", "").replace("]", ""))
    return parsed_result


def send_ifttt_request(json):
    key = config.get('IFTTT', 'KEY')
    trigger = config.get('IFTTT', 'TRIGGER')
    url = 'https://maker.ifttt.com/trigger/' + trigger + '/with/key/' + key
    response = requests.post(url, data=json)
    return response


########################


def main(stats):
    results = parse_storj_stats(stats)
    value1 = str(results[config.get('StorjValues', 'v1')])
    value2 = str(results[config.get('StorjValues', 'v2')])
    value3 = str(results[config.get('StorjValues', 'v3')])
    json = {"value1": value1, "value2": value2, "value3": value3}
    send_ifttt_request(json)
    return


# print sys.argv[1]
main(sys.argv[1])
