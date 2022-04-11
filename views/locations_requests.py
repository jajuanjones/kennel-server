import sqlite3
import json
from models import Location
def get_all_locations():
    """This function returns locations in locations list
    """
    # create a connection with the database
    # with as allows us to only run code inside of block when that connection is active
    with sqlite3.connect('./kennel.sqlite3') as conn:
        # create a cursor for our rows
        # Q: What is Row and what is row_factory?
        # A: Row is a way to process the database info we get back
        # A: setting this to row_factory allows us to transform our tuple from the data into
        #   a more useful object
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # create an sql query that gets all of our rows
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)
        # create an empty list of locations
        locations = []
        # convert our SQL rows into python lists
        dataset = db_cursor.fetchall()
        # iterate list of data
        for row in dataset:
            # and for every location create a new instance of a location
            location = Location(row['id'], row['name'], row['address'])
            # add new data to our location list
            # Q: What is dict doing?
            # A:
            locations.append(location.__dict__)
    # serialize data into JSON
    return json.dumps(locations)

def get_single_location(id):
    """This function will return single location from locations list
    """
    # create a connection with our database
    with sqlite3.connect('./kennel.sqlite3') as cnn:
        # create a database cursor for our rows
        cnn.row_factory = sqlite3.Row
        db_factory = cnn.cursor()
        # make an sql query that fetches data on client spec
        db_factory.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """,(id,))
        # convert our data in python
        data = db_factory.fetchone()
        # create an instance of a location based on the recieved data
        location = Location(data['id'], data['name'], data['address'])
        # serialize our data into json
        return json.dumps(location.__dict__)

def create_location(location):
    """This function creates a new location dictionary to be used in post request
    """
    # get the max id from the last index of LOCATIONS list
    max_id = LOCATIONS[-1]["id"]
    # create a new id that is 1 greater than the current max
    new_id = max_id + 1
    # set our new id to a new location
    location["id"] = new_id
    # add our new location to end of LOCATIONS array
    LOCATIONS.append(location)
    # return our location object
    return location

def delete_location(id):
    """This function will remove a location dictionary from list
    """
    # first give the initial index value of -1, in case an index isn't found
    location_index = -1
    # iterate of locations with enumerate to get the index of each value
    for i, location in enumerate(LOCATIONS):
        # if location is found store its index
        if location["id"] == id:
            location_index = i
    # if location is found, remove from list with pop
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    """This function will replace the data of location with specified id
    """
    # iterate over location list using enumerate to get the index of each value
    for i, location in enumerate(LOCATIONS):
        # then if a value has the id that matches the user specified id
        if location["id"] == id:
            # replace the values of the location at that index with new data
            LOCATIONS[i] = new_location
            # then stop the function
            break
