import json

with open(r"ScheduleToDay.json", "r") as read_file:
    data = json.load(read_file)
x = print(data[1]['time'])
