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

# we will pass in 'email' as the param for this method
def get_customers_by_email(email):
    """This function will return customers filtered by their email
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], 
                                row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

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
    with sqlite3.connect('./kennel.sqlite3') as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, ( id, ))

def update_customer(id, new_customer):
    """This function will replace the dictionary with the id user specifies
    """
    with sqlite3.connect('./kennel.sqlite3') as conn:
        db_cursor = conn.cursor()
        # update our row with new data using update query
        db_cursor.execute("""
        UPDATE customer
            SET
                name = ?,
                address = ?,
                email = ?,
                password = ?,
        WHERE id = ?
        """, (new_customer["name"], new_customer["address"],
              new_customer["email"], new_customer["password"], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    return True
        