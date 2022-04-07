CUSTOMERS = [
    {
        "id": 1,
        "name": "Joe Welsh"
    },
    {
        "id": 2,
        "name": "Sandra Bullock"
    }
]

def get_all_customers():
    """This function returns all customers from customers list
    """
    return CUSTOMERS

def get_single_customer(id):
    """This function returns a single customer matching id from our customers list
    """
    request_customer = None
    # create a for loop to iterate over customers list
    for customer in CUSTOMERS:
        if customer["id"] == id:
            request_customer = customer

    return request_customer
