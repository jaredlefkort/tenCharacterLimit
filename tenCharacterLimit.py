#Author: Jared Lefkort
#Date: 3/3/2016

f = open("input.txt", 'r')
#this will open the file "input" in read mode

contents = f.readlines()
#This will read the contents of the file into a list 

f.close()
#this will close the file

f = open("output.txt", 'r+')
#this will open the file "output" in read and write mode

for item in contents:
	
	item = item[0:10]
	#this will only print/add/read the first ten characters of each item in contents
	
	item = item.strip("\n")
	
	f.write(item)
	#this will write each item to the file
	
	print(item)
	#this will print the first ten characters of each item
	
f.close()
#this will close the file