EMPLOYEES = [
    {"id": 1, "name": "Jenna Solis"},
    {"id": 2, "name": "Alex Johnson"},
    {"id": 3, "name": "Emily Chen"}
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee
