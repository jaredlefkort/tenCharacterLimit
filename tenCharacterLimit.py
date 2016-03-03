#Author: Jared Lefkort
#Date: 3/3/2016

f = open("input.txt", 'r')



contents = f.readlines()

f.close()

f = open("output.txt", 'r+')

for item in contents:
	item = item[0:10]
	item = item.strip("\n")
	
	f.write(item)
	print(item)

f.close()
	 
