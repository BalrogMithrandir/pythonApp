data = "C40D7074F5EC324EEBF17E0967BB91B2EF41377A0CF0594EA3D5FBBFCCF7988DEA01F148EFDF4B72403746F478D0C025D67A52F577CA6DF0F33BD8D780753649A93E646B1309D580394F8162F92A497DB2AE9044AE7AF823001140F330B2F5F9224DA06D157290244368773E14FADD99"

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
