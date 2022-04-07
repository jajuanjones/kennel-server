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
      