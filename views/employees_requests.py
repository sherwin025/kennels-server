EMPLOYEES = [
    {
        "id": 1,
        "name": "Jeremy Bakker",
        "locationId": 2
    },
    {
        "id": 2,
        "name": "yahoo ligans",
        "locationId": 2
    },
    {
        "id": 3,
        "name": "mac attack",
        "locationId": 1
    },
    {
        "id": 4,
        "name": "lame o ",
        "locationId": 1
    },
    {
        "name": "Wayne",
        "locationId": 1,
        "id": 5
    },
    {
        "name": "yahoos",
        "locationId": 2,
        "id": 6
    },
    {
        "name": "eminems",
        "locationId": 4,
        "id": 7
    },
    {
        "name": "elizabete",
        "locationId": 1,
        "id": 8
    }
    ]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1 
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id): 
    emp_id = -1
    for x, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            emp_id = x
    if emp_id >= 0:
        EMPLOYEES.pop(emp_id)
        
def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break