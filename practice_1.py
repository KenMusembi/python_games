from statistics import *
import csv


#this is the first python practice execrice to see what i have learnt

#print out a word
print('first print out')
	
#initialize variable
r = 300

#define a function
def mainfunction():
	t=r/9
	print('the soldiers in thermopalyae were', t)
	
	
#try and catch
try:
	mainfunction()
	
except:
	print('error')

#writing/appending to a file
text = 'sample texy\nNew line'

saveFile = open('example.txt','w')

saveFile.write(text)
saveFile.close()

#read file
readf =open('example.txt','r').read()
print(readf)

#classes
class calculator:
	
	def addition(q,w):
		add = q+w
		print(add)
		
	def subtract(q,w):
		sub =q-w
		print(sub)
		
calculator.addition(2,3)

#user input
x = input('enter name' )

print(x)

#statistics
example_list = [2,3,4,2,1,2,34,]

x = mean(example_list)
print(x)

#tuples and lists
n = 2,3,4,5
m = [2,34,4,]
print(n[0])

m.append(2)
m.insert(2,8)
m.remove(2)

with open('example.txt') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	
	  
	for row in readCSV:
		print(row)

#multiline print
print(''' 
			hey
			hello
''')

#dictionaries
exDict = {'jack':15, 'bob':12, 'george':32}
print(exDict)
print(exDict['jack'])

exDict2 = {'jacky':[12, 'blonde']}

#built in functions
#absolute value
num = -9
print(abs(num))

#make dir
import os
curDir = os.getcwd()
print(curDir)
help()

import time

time.sleep(2)

 
