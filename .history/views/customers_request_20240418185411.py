CUSTOMERS = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"},
    {"id": 3, "name": "Alice Johnson"}
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer

def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer
