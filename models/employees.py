class Employee():
    """This class initializes an employee object
    """
    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.location = None

new_employee = Employee(1, "Bucky Barnes", "Homie Dubbs Rd.", 3)
