data = "B8D935E4D6D8F2D6C8282F9FD96248C796A9ED5B5A1A9559D23CBB5F1B03073F"

print len(data)

# i = 0

# while i < len(data):
    # print "0x%s, 0x%s" % (data[0:4], data[4:8])
	
	# print "hello"
	
	
i = 0
numbers = []

while i < len(data):
	print "0x%s, 0x%s, 0x%s, 0x%s, \\" % (data[i:i+2], data[i+2:i+4], data[i+4:i+6], data[i+6:i+8])
	i = i+8
	
	
#Readme
#This file is used to split the subdomain from a long long long string to array used in our code
