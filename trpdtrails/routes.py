from trpdtrails import app
import logging

@app.route('/parks', methods=['GET'])
def parks():
    return 'This will return the list of all of the parks'

@app.route('/parks/<park>', methods=['GET'])
def get_park(park):
    return f'This will return the information about the specific park, {park}, if it exists'