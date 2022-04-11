import sqlite3
import json
from models import Customer

def get_all_customers():
    """This function returns all customers from customers list
    """
    # open connection to database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # built in python methods for manipulating data
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write a SQL query to grab all data from the table
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """)

        # init an empty list to hold customer reps
        customers = []

        # convert rows of data into a python list
        dataset = db_cursor.fetchall()

        # iterate list of customers returned from database
        for row in dataset:

            # create an customer instance from current cursor row
            customer = Customer(row['id'], row['name'],
                                row['address'], row['email'],
                                row['password'])

            customers.append(customer.__dict__)

    # use json package to properly seralize list as json
    return json.dumps(customers)

def get_single_customer(id):
    """This function returns a single customer matching id from our customers list
    """
    # make connection with database
    with sqlite3.connect('./kennel.sqlite3') as conn:
        # use Row and create a cursor
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # make our SQL query and find the data for the id specified in client
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, (id,))
        # load the one customer
        data = db_cursor.fetchone()
        # create customer instance from current row
        customer = Customer(data['id'], data['name'],
                            data['address'], data['email'],
                            data['password'])
        # serialize list with json
        return json.dumps(customer.__dict__)

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
