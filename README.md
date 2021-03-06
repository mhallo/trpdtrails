# trpdTrails

The intent of this module/project is to provide an easier interface to check the status of the Cross Country Skiing Trails for the Three Rivers Park District.

As the website (from what I can tell) is just a Drupal webpage that is manually updated, the way to make it more readily accesible is to fetch and parse the page.

# Disclaimer
I do not work with the Three Rivers Park District of Minnesota.
The Three Rivers Park District does not maintain this project.
Support for this module will only last as long as I am willing and/or able to support it.

## Running the Server
```
export FLASK_APP=trpdtrails
```

Then in order to install and run the server you need to run:
```
pip install -e .
flask run
```

Additionally, development features can be seen with:
```
export FLASK_ENV=development
```


## Unit Tests

Unit Tests can be ran with:

```
python3 -m unittest
```

## Current Tasks
For the time being, the primary focus is to determine the way in which we can extract all of the park and trail information.
Then store the results in a organized and easily fetchable manner

## Future Improvements
Create a basic web server which can be reachable to get status' about all parks, or a specific parks trails
Create a scheduled polling timeframe for checking the website during the active hours. This is typically 11-5pm on weekdays, and 9-5pm on weekends, but varies by park.
Of course, as a courtesy to the Three Rivers Park District, this will be rate limited to not be a rude web citizen.

