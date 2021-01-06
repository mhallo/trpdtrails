import unittest
import os
from bs4 import BeautifulSoup

import main

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'trailstatus.html')

class trpdtests(unittest.TestCase):
    def setUp(self):
        with open(TESTDATA_FILENAME,'r') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'html.parser')
            soup.find(id='block-threerivers-content')
            soup.find("div", {"class": "userContent"})
            soup.find('p')
            self.page = soup

    def test_park_parser(self):
        """
        Test the ability to parse out the parks from the webpage
        """
        expected_park_list = ['Baker Park Reserve', 'Carver Park Reserve',
         'Cleary Lake Regional Park', 'Crow-Hassan Park Reserve', 
         'Eagle Lake Regional Park', 'Elm Creek Park Reserve', 
         'French Regional Park', 'Glen Lake Golf Center', 
         'Hyland Lake Park Reserve', 'Lake Rebecca Park Reserve', 'Murphy-Hanrehan Park Reserve']

        result = main.populate_park_list(self.page)
        self.assertListEqual(expected_park_list, result)

if __name__ == '__main__':
    unittest.main()

