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

def create_customer(customer):
    """This function will create a new customer
    """
    # get the max id from the end of the customers list
    max_id = CUSTOMERS[-1]["id"]
    # set new id to the max id plus 1
    new_id = max_id + 1
    # set our passing customer param id as the new id
    customer["id"] = new_id
    # append our new customer to the end of the customers list
    CUSTOMERS.append(customer)
    # return our customer param
    return customer
