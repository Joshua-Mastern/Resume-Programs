##################################################################
# Team Griffin							 #
# Date: 5/8/2020						 #
# Program: Xor							 #
# Python Version: 2.7						 #
# Descr: Xors data from a key file with provided input and sends #
#		result to output stream				 #
##################################################################

from sys import stdin, stdout

# store name of file with key which is to be placed in same directory
key_file = "key"


# read data from key_file as binary data
keyData = bytearray(open(key_file, "rb").read())

# read data from stdin as binary data
inputData = bytearray(stdin.read())

# create bytearray of same size of keyData
outputData = bytearray(len(inputData))

# take a collection of bits from key and xor with a collection of bits from stdin for all data
for i in range(len(inputData)):
	outputData[i] = inputData[i] ^ keyData[i]

#redirect xored data to stdout
stdout.write(outputData)

