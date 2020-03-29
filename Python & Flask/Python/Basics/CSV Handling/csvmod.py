#incomplete file
import csv
import io
from datetime import datetime
path = "data.csv"
file = io.open(path,newline="")
"""
Notice we have implemented newline argument as an empty string
This will ensure that our program will run correctly on any
platform

"""
# now parse the csv file to our csv module
reader =csv.reader(file)
header = next(reader) # The first line is the header
"""
data = [row for row in reader] # now get the data for all row

print(header)
print(data[0])

The Problem with this method is that our data is till 
being treated as strings
we need to improve our code

"""
data = []
for row in reader:
    date= datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high=float(row[2])
    low=float(row[3])
    close=float(row[4])
    volume=int(row[5])
    adj_close=float(row[6])

data.append([date,open_price,high,low,close,volume,adj_close])
print(data[0])

