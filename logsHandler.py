import json
from datetime import datetime

# read json file
data = []
with open('logs/original/log_2024-01-10.json', 'r') as file:
    for line in file:
        json_object = json.loads(line)
        data.append(json_object)

# group by userid
grouped_data = {}
for entry in data:
    userId = entry["userId"]
    if userId not in grouped_data:
        grouped_data[userId] = []
    grouped_data[userId].append(entry)

# write into new json file based on userid
for userId, entries in grouped_data.items():
    sorted_entries = sorted(entries, key=lambda x: datetime.strptime(x["currentTime"], '%H:%M:%S'))
    with open(f'logs/batch4/{userId}.json', 'w') as file:
        json.dump(sorted_entries, file, indent=4)
