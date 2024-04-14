#################################################################
#Name: Joshua Brack                                             #
#Date: 4/9/2021                                                 #
#Class: Cyen 403                                                #
#Title: EncryptoDecryptoGod                                     #
#Description: Encrypts or decrypts messages until user quits    #
#Usage: python encryptoDecryptoGod.py                           #
#################################################################


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode

def encryptMessage(message, public_key_name):
    public_key = RSA.import_key(open(public_key_name).read())
    rsa_encryption = PKCS1_OAEP.new(public_key)
    encryptedMessage = rsa_encryption.encrypt(message.encode())
    return b64encode(encryptedMessage).decode()

def decryptMessage(message, private_key_name):
    private_key = RSA.importKey(open(private_key_name).read())
    rsa_decryption = PKCS1_OAEP.new(private_key)
    message = message.encode()
    decryptedMessage = rsa_decryption.decrypt(b64decode(message))
    return decryptedMessage.decode()

while(True):
    userinput = input("Would you like to encrypt (e), decrypt (d), or quit (q)?\n")
    if(userinput == "e"):
        message = input("Specify the name of the file to be encrypted.\n")
        public_key_name = input("Specify the name of the the public key file\n")
        output_file_name = input("Specify the name of the file which will contain the results\n")

        #get message from file
        f=open(message, "r")
        message = f.read()
        f.close()
        
        #encrypt the message with the key
        results = encryptMessage(message, public_key_name)
        
        #paste the response to a new file
        f = open(output_file_name, "w+")
        f.write(results)
        f.close()
        print("Encryption complete.\n")

    elif(userinput == "d"):
        message = input("Specify the name of the file to be decrypted.\n")
        private_key_name = input("Specify the name of the the private key file\n")
        output_file_name = input("Specify the name of the file which will contain the results\n")
        
        #message = "questions.txt"
        #private_key_name = "private_key.pem"
        #output_file_name = "questionsDecrypted.txt"

        #get message from file
        f=open(message, "r")
        message=f.read()
        f.close()
        #decrypt the file
        results = decryptMessage(message, private_key_name)

        #paste the response to a new file
        f = open(output_file_name, "w+")
        f.write(results)
        f.close()
        print("Decryption complete.\n")

    elif(userinput == "q"):
        print("Program Terminating.\n")
        break
    else:
        print("Not acceptable input.\n")