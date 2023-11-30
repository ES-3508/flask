from flask import Flask, jsonify
import json

class CommonMethod:
    def __init__(self):
        super().__init__()

    def convert_object_to_json(obj):
      return json.dumps(obj)
    
   