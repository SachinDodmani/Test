import requests
import csv
import json
import pdb

# Making a get request

response = requests.get('http://glsindia-dev.cisco.com:3838/data/output.json')

# print json content
data = response.json()
#data = json.load(response.json())

for key in data:
    print(key, ":", data[key])

pdb.set_trace()
#with open('d.json') as json_file:
#data = json.load(response.json())

#employee_data = data['cases']

# now we will open a file for writing
#data_file = open('data_file.csv', 'w')

# create the csv writer object
#csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
# count = 0
#
# for emp in employee_data:
#     if count == 0:
#         # Writing headers of CSV file
#         header = emp.keys()
#         csv_writer.writerow(header)
#         count += 1
#
#     # Writing data of CSV file
#     csv_writer.writerow(emp.values())
#
# data_file.close()