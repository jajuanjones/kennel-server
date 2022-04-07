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
    