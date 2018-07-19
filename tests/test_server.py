import logging
import unittest

from flask import request
import server


class TestServer(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestServer, self).__init__(*args, **kwargs)
        logging.basicConfig(level=logging.DEBUG)

    def test_1(self):
        with server.app.test_request_context('/hello', method='GET'):
            # now you can do something with the request until the
            # end of the with block, such as basic assertions:
            assert request.path == '/hello'
            assert request.method == 'GET'