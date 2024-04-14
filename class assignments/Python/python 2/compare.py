###############################################################################################
#Team: Griffin										      #
#Python Version: 2.7.17									      #
#Description: Compares difference in two files to provide information about their differences.#
###############################################################################################

from sys import stdin, stdout, argv


#usage
#-o<val> -a<val>
#-o is for original and -a is for altered where their values are the name of their file.
original = ""
altered = ""

DEBUG = False

for x in argv:
	if(x[:2]=="-o"):
		original = x[2:]
	elif(x[:2]=="-a"):
		altered = x[2:]
	elif(x==argv[0]):
		pass
	else:
		print "{} is not a valid argument.".format(x)
                raise Exception("broke")
try:
	f = open(original)
	f.close()
except IOError:
	print "original file does not exist"
try:
        f = open(altered)
        f.close()
except IOError:
        print "altered file does not exist"

#process original data
originalData = bytearray(open(original, "rb").read())
alteredData = bytearray(open(altered, "rb").read())
hiddenData = bytearray()
text = ""
b = bytearray(1)
i = 0
if(DEBUG):
	print "len of altered is {}".format(len(alteredData))
	print "len of original is {}".format(len(originalData))
while(i < len(alteredData)):
	#check difference between them byte by byte
	if(not(alteredData[i] == originalData[i])):
		b[0]= alteredData[i]
		hiddenData+=b		
	i+=1
stdout.write(hiddenData)
