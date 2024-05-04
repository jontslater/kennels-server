import json

class Location:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

class LocationEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Location):
            return {'id': obj.id, 'name': obj.name, 'address': obj.address}
        return super().default(obj)

# Use the custom encoder when serializing the data
json.dumps({'location': Location(1, 'Location Name', 'Location Address')}, cls=LocationEncoder)
