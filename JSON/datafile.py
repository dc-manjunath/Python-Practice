import json

from pathlib import Path

# Personal_details = [{
#   "person": {
#     "name": "John Doe",
#     "age": 30,
#     "isStudent": False,
#     "address": {
#       "street": "123 Main Street",
#       "city": "Anytown",
#       "zipcode": "12345"
#     },
#     "phoneNumbers": ["555-1234", "555-5678"]
#   },
#   "pets": [
#     {
#       "name": "Fluffy",
#       "type": "Cat"
#     },
#     {
#       "name": "Buddy",
#       "type": "Dog"
#     }
#   ]
# }]


# data = json.dumps(Personal_details)
# Path("Personal_details").write_text(data)

data = Path("Personal_details.json").read_text()
Details = json.loads(data)
print(Details[0])