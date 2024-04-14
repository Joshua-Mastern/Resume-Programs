import csv
import hashlib
import os
from CnxReadWriteFunctions import *
from base64 import b64encode

# optimal string alignment distance
def osa(str1, str2):
    # map of last character of hash to length of before-hashed password
    # index number + 5 is the length of password
    randChars = ['c','4','e','0','2','7','b','6','a','9','5','d','f','1','3','8']

    # use the last character of each hash to find length of each password and segment
    s = list(str1)
    keyLen = randChars.index(s[63])+5
    s = list(str2)
    testLen = randChars.index(s[63])+5
    keySegLen = int(64/keyLen)
    testSegLen = int(64/testLen)
    
    # make table
    table = [[None for i in range(keyLen+1)] for j in range(int(testLen+1))]
    for i in range(len(table[0])):
        table[0][i] = i
    for i in range(len(table)):
        table[i][0] = i

    for row in range(1, len(table)):
        for col in range(1, len(table[0])):
            # check for insertion, deletion, and substitution
            if str1[(col-1)*keySegLen:(col-1)*keySegLen+3] == str2[(row-1)*testSegLen:(row-1)*testSegLen+3]:
                table[row][col] = table[row-1][col-1]
            else:
                table[row][col] = min(table[row][col-1], table[row-1][col], table[row-1][col-1]) + 1

            # check for swaps (not in levenshtein algorithm)
            if row > 1 and col > 1 and (str2[(row-1)*testSegLen:(row-1)*testSegLen+3] == str1[(col-2)*keySegLen:(col-2)*keySegLen+3]) and (str2[(row-2)*testSegLen:(row-2)*testSegLen+3] == str1[(col-1)*keySegLen:(col-1)*keySegLen+3]):
                table[row][col] = min(table[row][col], table[row-2][col-2] + 1)
    
  
  
    return table[testLen][keyLen]

def targetDistance(num):
    # if the strings have more than three differences, they are too different
    if num > 2:
        return False
    return True

def hashingAlg(string, length, rem, salt):
    # create a hash for each character and combine them to make one hash
    pepper = "fsKegnOEfwsZcLSjl5pJvR7yNEh4JylbWJxWMuL3LX8"
    stringHash = ""
    index = 0
    charsUsed = ""
    for letter in string:
        charsUsed = charsUsed + letter
        saltedLetter = salt * charsUsed.count(letter) + letter + pepper
        if rem != 0 and index == len(string)-1:
            # last segment if there is remainder
            stringHash = stringHash + hashlib.sha256(saltedLetter.encode("UTF-8")).hexdigest()[:length+rem]
        else:
            stringHash = stringHash + hashlib.sha256(saltedLetter.encode("UTF-8")).hexdigest()[:length]
        index += 1

    # map of last character of hash to length of before-hashed password
    # index number + 5 is the length of password
    randChars = ['c','4','e','0','2','7','b','6','a','9','5','d','f','1','3','8']

    # replace last character of hash with character representing length of password
    s = list(stringHash)
    s[63] = randChars[len(string)-5]
    stringHash = "".join(s)
        
    return stringHash

def newpassword(username, password, average, SD):
    # get password and hash it with each letter hashed
    key = password
    keyLen = len(key)
    keySegLen = int(64/keyLen)
    keyRem = 64 % keyLen
    salt = b64encode(os.urandom(32)).decode("utf-8")
    keyHash = hashingAlg(key, keySegLen, keyRem, salt)
    key = "qwertyuiopasdfghjklzxcvbnm"
    newrow = [username, keyHash, average, SD, salt]
    salt = "qwertyuiopasdfghjklzxcvbnm"

    cnx = connect()
    #write newrow to database
    write(cnx, newrow)
    cnx.close()


def enterpassword(username, test):
    # get input and hash it with each letter hashed
    testLen = len(test)
    testSegLen = int(64/testLen)
    testRem = 64 % testLen

    #create connection to database and read values
    cnx = connect()
    #data is tuple (username [tpye string], passwordhash [tpye string], keyavg [tpye string], keysd [type float], passwordsalt [tpye string])
    data = read(cnx, username)
    cnx.close()
    salt = data[0][4]
    keyHash = data[0][1]
    testHash = hashingAlg(test, testSegLen, testRem, salt)
    

    # edit distance function 
    editDistance = osa(keyHash, testHash)

    #overwrite values for security
    salt = "qwertyuiopasdfghjklzxcvbnm"
    data = (None,) * len(data)

    return editDistance

def main():
    cnx=connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT username FROM captable")
    results = cursor.fetchall()
    cursor.close()
    cnx.close()
    usernames = [row[0] for row in results]
    
    username = input("Enter username: ")
    if username not in usernames:
        newpassword(username)
    else:
        test = input("Enter your password: ")
        enterpassword(username, test)

if __name__=="__main__":
    main()