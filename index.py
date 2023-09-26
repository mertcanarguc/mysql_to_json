import mysql.connector
import json
import os
import datetime

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'example',
}

# Custom converter for JSON
def json_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    if isinstance(o, datetime.date):
        return o.__str__()

# Establish connection
connection = mysql.connector.connect(**config)
cursor = connection.cursor(dictionary=True)

# Get the SQL query from the user
query = input("Please enter the SQL query: ")
cursor.execute(query)

# Fetch results and convert them to JSON
results = cursor.fetchall()
json_data = json.dumps(results, default=json_converter, indent=4)

# Ask the user for the filename for the output JSON
filename = input("Please enter the name for the JSON output file: ") + ".json"

# Save each result to 'temp' folder line by line
with open(os.path.join("temp", filename), 'w') as file:
    file.write("[\n")
    for index, result in enumerate(results):
        json_line = json.dumps(result, default=json_converter)
        if index < len(results) - 1:  # If it's not the last object, add a comma
            file.write(json_line + ",\n")
        else:  # If it's the last object, don't add a comma
            file.write(json_line + "\n")
    file.write("]\n")

print(f"Saved to 'temp' folder as '{filename}'!")

cursor.close()
connection.close()
