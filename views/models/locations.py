class Location():
    """This class initializes a location obj
    """
    def __init__(self, id, address) -> None:
        self.id = id
        self.address = address
        
new_location = Location(1, "Honey Walnut St.")
