import json

class ResponseObjectEncoder(json.JSONEncoder):
   def default(self, o):
        return o.__dict__