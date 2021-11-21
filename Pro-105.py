import csv
import math
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data.pop(0)
def mean (data):

    total = 0
    n = len(data)

    for x in data:
        total += int (x)

    mean = total/n

    return mean
#Squaring and getting the values
s = []

for n in data:
    a = int (n) - mean(data)
    a = a** 2
    s.append(a)
#Getting sum 
sum = 0

for i in s:
    sum += i

#Dividing the sum by total values
result = sum/len(data)

#Getting the deviation by taking square root of result
std_dev = math.sqrt(result)

print(std_dev)