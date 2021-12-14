import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)
newData = fileData[0]
n = len(newData)
total = 0
for numbers in newData :
    total += float(numbers)
mean = total/n
squaredList= []
for number in newData :
    num = float(number) - mean
    num = num**2
    squaredList.append(num)
sum = 0
for i in squaredList :
    sum += i
result = sum / n-1
standard_deviation = math.sqrt(result)
print(standard_deviation)
print(mean)
