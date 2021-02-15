"""
Main file. May include other file in future.
"""

import requests

response = requests.get("http://localhost:8000/api/from_drone")

print(response.json())