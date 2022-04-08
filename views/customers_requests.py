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

def delete_customer(id):
    """This function will remove a customer dictionary from list
    """
    # in case no index, inital index is -1
    customer_index = -1
    # iterate list and get the index for each value
    for i, customer in enumerate(CUSTOMERS):
        # if customer is found save the index of customer
        if customer["id"] == id:
            customer_index = i
    # if location has an index remove location at index from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """This function will replace the dictionary with the id user specifies
    """
    # iterate over customers list with enumerate to get index of each value
    # for every customer in list
    for i, customer in enumerate(CUSTOMERS):
        # if customer id matches specified id param
        if customer["id"] == id:
            # update the values of that found customer with with new data
            CUSTOMERS[i] = new_customer
            # end this function
            break
