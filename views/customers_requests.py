CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct",
        "email": "hannah@hannah.com"
    },
    {
        "id": 2,
        "name": "Patrick Mattera",
        "address": "106 Hardcourt ave",
        "email": "patrick@patrick.com"
    },
    {
        "id": 3,
        "name": "German Fernandez",
        "address": "47 Cumerford st",
        "email": "german@german.com"
    },
    {
        "name": "sherwin vargas",
        "address": "100 antioch pike",
        "email": "svargas025@gmail.com",
        "id": 4
    }
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
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1 
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id): 
    customer_index = -1 
    for x, animal in enumerate(CUSTOMERS):
        if animal["id"] == id:
            customer_index = x
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)