class Customer():
    """This class initalizes a customer object
    """
    def __init__(self, id, name, address, email, password):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
  
new_customer = Customer(1, "Ronald Robert", "Sherman Street", "rr@face.com", "asdiweEDIdkg15612")
