import json

class ResponseObjectEncoder(json.JSONEncoder):
   def default(self, o):
        return o.__dict__


# from bson import ObjectId

# class ResponseObjectEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)  # Convert ObjectId to its string representation
#         return super().default(o)