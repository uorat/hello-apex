from __future__ import print_function

import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    logger.info("value1 = " + event['key1'])
    logger.info("value2 = " + event['key2'])
    logger.info("value3 = " + event['key3'])
    return event
    # return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
