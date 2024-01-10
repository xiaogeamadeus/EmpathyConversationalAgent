import os
import json
from datetime import datetime

# Function to count the number of objects in a JSON array and calculate time difference
def process_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list) and data:
                # Count the objects
                object_count = sum(1 for item in data if isinstance(item, dict))
                
                # Calculate the time difference between first and last object
                time_format = "%H:%M:%S"
                first_time = datetime.strptime(data[0]['currentTime'], time_format)
                last_time = datetime.strptime(data[-1]['currentTime'], time_format)
                time_difference = last_time - first_time
                
                return object_count, time_difference
            else:
                return 0, timedelta(0)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0, timedelta(0)

# Assuming JSON files are in the 'logs/batch1/' directory
directory = 'logs/batch5/'
json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

# Collecting file names, their object counts, and time differences in a list of tuples
file_data = []
for json_file in json_files:
    count, time_diff = process_json_file(os.path.join(directory, json_file))
    file_data.append((json_file, count, time_diff))

# Sorting the list by the count of objects in each file (second item of the tuple)
sorted_file_data = sorted(file_data, key=lambda x: x[1], reverse=True)

# Printing the sorted list
for json_file, count, time_diff in sorted_file_data:
    id = json_file.split('.')[0]
    print(f"UserId: {id}, {count} Conversations, Login Duration: {time_diff}")
