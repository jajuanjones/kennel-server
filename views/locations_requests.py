LOCATIONS = [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
]

def get_all_locations():
    """This function returns locations in locations list
    """
    return LOCATIONS

def get_single_location(id):
    """This function will return single location from locations list
    """
    requested_location = None
    # create a for loop to iterate over locations list and grab locations
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location

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
