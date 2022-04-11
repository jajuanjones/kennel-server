class Location():
    """This class initializes a location obj
    """
    def __init__(self, id, name, address) -> None:
        self.id = id
        self.name = name
        self.address = address

new_location = Location(1, "Nashville Somewhere", "Honey Walnut St.")
