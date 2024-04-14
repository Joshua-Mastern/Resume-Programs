import mysql.connector
#function to connect to cnx
def connect():
        cnx = mysql.connector.connect(
                host="192.168.176.8",
                user="Dodobirds",
                password="password",
                database="capstone"
                )

        return cnx

#cnx object and username as string are parameters
def read(cnx, username):
        cursor = cnx.cursor()
        query = "Select * FROM captable where username = %s"
        #put username in tuple
        keyValue = (username,)
        cursor.execute(query, keyValue)

        #data is a list of tuples. Each tuple follows this pattern:
        #(username (string), passwordhash (string), keyavg (keystroke data (string of numbers)), keysd (std. deviation (float)), passwordsalt (salt for password(string)))
        data = cursor.fetchall()
        cursor.close()

        #if username doesn't exist then data will be empty
        return data
#write function expects cnx object, data tuple containing all information to be added to the database
def write(cnx, data):
        cursor = cnx.cursor()
        query = "INSERT INTO captable (username, passwordhash, keyavg, keysd, passwordsalt) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        cnx.commit()
        cursor.close()

        return

def main():
        while(1):
                cnx = connect()
                username = input("Try a username: ")
                data = read(cnx, username)
                if(len(data)==0):
                        print("That username doesn't exist. Acct creation beginning.")
                        password = input("Enter Password: ")
                        data =(username, password, None, None, None)
                        write(cnx, data)
                        cursor = cnx.cursor()
                        cursor.execute("SELECT * FROM captable")
                        rows = cursor.fetchall()
                        cursor.close()
                        for row in rows:
                                print(row)
                else:
                        print(data)

if __name__=="__main__":
        main()
                