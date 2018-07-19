import logging

import requests

# Assume you're developing an application that consumes a third-party HTTP API.
# Using your favourite language and framework, please write a very simple unit test-case
# that proves that the application handles http404 errors as expected.
# It doesn't matter what exactly that expected behaviour is,
# just show us how you structure a test and write expectations/assertions.

url='http://localhost:5000/two'


def addition(first_number=2):
    web_service_result = requests.get(url)
    if web_service_result.status_code == 200:
        # TODO: Test if integer, etc.:
        try:
            web_service_value=int(web_service_result.json())
            result = first_number+web_service_value
            logging.info('Final Result: %.3f', result)
            return result
        except:
            logging.exception('Issue while doing the addition')
    else:
        logging.warning('Issue with the Web Service')