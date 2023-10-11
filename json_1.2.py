import json

indian_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}

with open('indian_capitals.json', 'w') as json_file:
    json.dump(indian_capitals, json_file)

print("Data has been written to 'indian_capitals.json' successfully.")
