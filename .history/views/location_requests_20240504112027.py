import sqlite3
import json
from models import location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

def get_all_locations():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Fetch location details
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, (location,))
        location_row = db_cursor.fetchone()

        if not location_row:
            return None

        location = {
            'id': location_row['id'],
            'name': location_row['name'],
            'address': location_row['address'],
            'animals': [],
            'employees': []
        }

        # Fetch animals for the location
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.location_id = ?
        """, (location,))
        animals_rows = db_cursor.fetchall()

        for row in animals_rows:
            animal = {
                'id': row['id'],
                'name': row['name'],
                'breed': row['breed'],
                'status': row['status'],
                'location_id': row['location_id'],
                'customer_id': row['customer_id']
            }
            location['animals'].append(animal)

        # Fetch employees for the location
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id
        FROM Employee e
        WHERE e.location_id = ?
        """, (location,))
        employees_rows = db_cursor.fetchall()

        for row in employees_rows:
            employee = {
                'id': row['id'],
                'name': row['name'],
                'location_id': row['location_id']
            }
            location['employees'].append(employee)

        return location


def get_single_location(id):
    requested_location = None
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    return requested_location

def create_location(location):
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location

def delete_location(id):
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the LOCATIONS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    # Iterate the LOCATIONS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Update the value.
            LOCATIONS[index] = new_location
            break
