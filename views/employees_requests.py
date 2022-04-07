EMPLOYEES = [
    {
        "id": "1",
        "name": "Johnny Silver"
    },
    {
        "id": "2",
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
