import unittest
import os
from bs4 import BeautifulSoup

import main

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'trailstatus.html')

class trpdtests(unittest.TestCase):
    def setUp(self):
        with open(TESTDATA_FILENAME) as fp:
            soup = BeautifulSoup(fp.read(), 'html.parser')
        
        soup.find(id='block-threerivers-content')
        soup.find("div", {"class": "userContent"})
        soup.find('p')
        self.page = soup
    
    def tearDown(self):
        self.page = None

    def test_park_parser(self):
        """
        Test the ability to parse out the parks from the webpage
        """
        expected_park_list = ['Baker Park Reserve', 'Carver Park Reserve',
         'Cleary Lake Regional Park', 'Crow-Hassan Park Reserve', 
         'Eagle Lake Regional Park', 'Elm Creek Park Reserve', 
         'French Regional Park', 'Glen Lake Golf Center', 
         'Hyland Lake Park Reserve', 'Lake Rebecca Park Reserve', 'Murphy-Hanrehan Park Reserve']

        main.populate_park_list(self.page)
        result = main.get_park_list()
        self.assertListEqual(expected_park_list, result)

    def test_status_parser(self):
        """
        Test the ablity to parse out the trail status information
        """
        expected_status_info = ['Good; Groomed: Prairie, Lesson Area Fair; Packed : Evergreen Fair; Groomed: Island, Hill, Timber, Fairway Note: Chalet open 9\xa0AM-5\xa0PM, daily.\xa0Rentals available online . Multi-use Trail: Open; Last groomed Jan. 8,\xa02021\xa0(skijoring, dog sledding, snowshoeing, hiking)', 'Fair; Groomed : Sugar Bush, Grimm Farm, Sky, Lake, Nature Center Poor; Groomed: King Note: Trailhead building open 9\xa0AM-5\xa0PM, daily. Rentals available online . Last groomed Jan. 9.', 'Poor; Packed: Poplar, Lakeside, Ironwood, Golf Course Loop Closed: Lower Ironwood Note: Rentals unavailable due to poor conditions; lights on until 10\xa0PM.', 'Multi-use Trail: Open. Note: Ski pass not required.', 'Good; Groomed: Eagle and Practice Trails Fair; Groomed: Pike', 'Good; Groomed: Valley Fair; Packed: Northern Lights, Lake, Creek Poor; Packed : Creek Fair; Tracked: Lake, Eagle, Monarch Poor; Tracked: Northern Lights, Creek Note: Rentals now available online .', 'Good; Groomed: Skyline, Meadow, Medicine, Lagoon, Lakeview Note: Trail lights on 5 AM-10\xa0PM. Visitor Center\xa0open 9\xa0AM-9\xa0PM. Rentals available online .', 'Fair; Packed: Glen Trail and Practice Loop Note: Trails and chalet open 11\xa0AM-5\xa0PM\xa0Mon-Fri and 9\xa0AM-5\xa0PM\xa0Sat-Sun.\xa0Rentals available online .', 'Good;\xa0Groomed: Star Loop, Willow Creek Loop, Frog Town, Scenic Foothills, Boulder Ridge. Fair;\xa0Packed, Not Tracked: Lake Trail, Hill Trail, Oak Knob, North Trail, Nature Center Trail. Note: Rentals available online .', 'Multi-use Trail : Open Note: Ski pass not required.', 'Closed : All trails']
        main.extract_trail_conditions(self.page)
        result = main.get_status_list()
        self.assertListEqual(expected_status_info, result)


if __name__ == '__main__':
    unittest.main()

