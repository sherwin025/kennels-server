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
    },
    {
        "name": "nashville west",
        "address": "234 broadway",
        "id": 3
    },
    {
        "name": "Nashville East",
        "address": "123 Chatoona",
        "id": 4
    }
    ]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None
    
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
        
    return requested_location

def create_location(location):
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1 
    location["id"] = new_id
    LOCATIONS.append(location)
    return location

def delete_location(id):
    location_id = -1
    for x, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_id = x
    if location_id >= 0:
        LOCATIONS.pop(location_id)
        
def update_location(id, locationnew):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = locationnew
            break