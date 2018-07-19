import logging
import unittest

import requests
import requests_mock
import addition

url='http://localhost:5000/two'

class TestAddition(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAddition, self).__init__(*args, **kwargs)
        logging.basicConfig(level=logging.DEBUG)

    def test_1(self):
        with requests_mock.Mocker() as m:
            m.get(url, status_code=404, text='Sorry Mate')
            print(requests.get(url).status_code)

    def test_ok(self):
        ''' Make sure you start the server first... '''
        self.assertEqual(4, addition.addition())

    def test_not_ok_404(self):
        ''' You don't need to start the server first...  beauty of the Mock '''
        with requests_mock.Mocker() as m:
            m.get(url, status_code=404, text='Sorry Mate')
            self.assertIsNone(addition.addition())