# path="file.csv"
# file=open(path)
# for line in file:
#     print(line)

path = "file.csv"
lines= [line for line in open(path)] #this will generate a dictionary of all lines
print(lines[1])
# lets strip white spaces
lines[0].strip()
# now strip white spaces and sperate the objects with comma, in the array
lines[1].strip().split(',')
# now make a dataset from every line from the csv file
dataset=[line.strip().split(',') for line in open(path)]
# lets check our dataset
print(dataset[0])
print(dataset[1])