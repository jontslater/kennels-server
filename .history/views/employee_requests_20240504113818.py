import sqlite3
import json
from models import Employee
from models import Location

EMPLOYEES = [
    {"id": 1, "name": "Jenna Solis"},
    {"id": 2, "name": "Alex Johnson"},
    {"id": 3, "name": "Emily Chen"}
]

def get_all_employees():
    print(get_all_employees)
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id,
            l.name location_name,
            l.address location_address
        FROM employee e
        JOIN Location l
            ON l.id = e.location_id  
        """)

        # Initialize an empty list to hold all employee representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Employee class above.
            employee = Employee(
                            row['id'], 
                            row['name'],
                            row['location_id'])

            # Create a Location instance from the current row
            location = Location(
                            row['id'], 
                            row['location_name'],
                            row['location_address'])
            
            employee.location = location.__dict__
            employees.append(employee.__dict__)

    return employees

def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee
def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employees
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break

def get_employee_by_location_id(location):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id
        FROM Employee e
        WHERE e.location_id = ?
        """, (location,))

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(
                            row['id'],
                            row['name'],
                            row['location_id'])
            employees.append(employee.__dict__)

    return employees
