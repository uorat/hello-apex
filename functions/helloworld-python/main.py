from __future__ import print_function
import sys
import logging
import json
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info("execute __init__")

def handle(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))
    return get_cidrs(event['region'])

def get_cidrs(region):
    url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
    logger.info("execute requests.get(), url=%s" % (url))
    response = requests.get(url)
    logger.debug("executed GET requests, response=%s" % (response.json()))
    cidrs = response.json()['prefixes']
    logger.info("execute filter(), region=%s" % (region))
    regions = filter(lambda x: x['region'] == region , cidrs)
    return list(map(lambda x: x['ip_prefix'], regions))
