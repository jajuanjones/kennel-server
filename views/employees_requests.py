EMPLOYEES = [
    {
        "id": 1,
        "name": "Johnny Silver"
    },
    {
        "id": 2,
        "name": "Sara Rile"
    }
]

def get_all_employees():
    """This function will return all employees from list
    """
    return EMPLOYEES

def get_single_employee(id):
    """This function will return a single employee from list
    """
    request_employee = None

    # for loop to iterate over employees list to grab employee
    for employee in EMPLOYEES:
        if employee["id"] == id:
            request_employee = employee

    return request_employee

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