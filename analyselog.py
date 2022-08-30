#!/usr/bin/ env python3


import json

data = []

order = ["request", "URL", "status"]

file_name = "log.txt"

logAnalysis = open(file_name, "r")

for line in logAnalysis.readlines():
    logList = line.split(' ')
    logList = [x.strip("\"") for x in logList]
    logList = [x.strip("\n") for x in logList]
    structure = {key:value for key, value in zip(order, logList)}
    data.append(structure)
    
for dataJson in data:
    print(json.dumps(dataJson, indent = 4))