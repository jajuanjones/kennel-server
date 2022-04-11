import sqlite3
import json
from models import Employee

def get_all_employees():
    """This function will return all employees from list
    """
    # create a connection with database
    with sqlite3.connect('./kennel.sqlite3') as conn:
        # use row and create a database cursor
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # make our SQL query to grab all employees
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        """)
        # create an empty list to hold all employees from database
        employees = []
        # convert rows into python list
        dataset = db_cursor.fetchall()
        # iterate over list of employees too get data for each row
        for row in dataset:
        # add list item to employees list
            employee = Employee(row['id'], row['name'],
                                row['address'], row['location_id'])

            employees.append(employee.__dict__)
    # serialize list to json
    return json.dumps(employees)

def get_single_employee(id):
    """This function will return a single employee from list
    """
    # create a conection with database
    with sqlite3.connect('./kennel.sqlite3') as conn:
        # use Row and create a cursor for database
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # create our SQL query to grab data based on client specification
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, (id,))
        # convert grabbed row into python list
        data = db_cursor.fetchone()
        # create an instance of the grabbed row
        employee = Employee(data['id'], data['name'],
                            data['address'], data['location_id'])
        # serialize instance into json
        return json.dumps(employee.__dict__)

def get_employee_by_location(location_id):
    """This function will filter employees based on client specified location_id
    """
    with sqlite3.connect('./kennel.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)

def create_employee(employee):
    """this function will create a new employee object and add it to our employee list
    """
    # get our max id from the end of employee list
    max_id = EMPLOYEES[-1]["id"]
    # create a new id based off the max id
    new_id = max_id - 1
    # set our employee param id to the new id
    employee["id"] = new_id
    # append our param to the end of employee list
    EMPLOYEES.append(employee)
    # return param
    return employee

def delete_employee(id):
    """This function will remove an employee from EMPLOYEES list
    """
    # in case of no index found, inital index value of -1 is given
    # this prevents the last index of the list from being removed
    employee_index = -1
    # iterate employees list with enumurate to get the index of each value
    for i, employee in enumerate(EMPLOYEES):
        # if employee id is found, save the value of its index
        if employee["id"] == id:
            employee_index = i
    # if index of employeeindex exists (is greater than 0), remove from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
        
def update_employee(id, new_employee):
    """This function will replace the data of a dictionary at an index
    """
    # iterate over array using enumerate to get index of each dictionary
    # then for each employee
    for i, employee in enumerate(EMPLOYEES):
        # if location id matches id specified
        if employee["id"] == id:
            # we will change the data to new data at that index
            EMPLOYEES[i] = new_employee
            # stop the function
            break
