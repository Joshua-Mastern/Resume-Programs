from flask import Flask, render_template, request, url_for, flash, redirect
from hashingFunction import *
from password_comparisons import calculation
from user_creation import create_user

global new_username
global new_password
global confirm_password

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['uname']
    password = request.form['psw']
    log = request.form['log']
    log = log[4:len(log)-1]
    

    #pass username and log of keystrokes, get stuff from DB in comparison file
    editDistance = enterpassword(username, password)
    key_match = calculation(username, log, editDistance)


    if key_match and editDistance <= 2:
        return ("Access granted")
    
    else:
        return ("Access Denied")

    return str(calculation(username, log))
    


@app.route('/signup', methods=['GET', 'POST'])
def create_account():
    global new_password
    global new_username
    global confirm_password
    
    if request.method == 'GET':
        return render_template('create_account.html')
    
    return render_template('pass_input.html')

@app.route('/pass_input', methods=['GET', 'POST'])
def keystroke_page():
    global new_password
    global new_username
    global confirm_password
    new_username = request.form['username']
    new_password = request.form['password']
    confirm_password = request.form['confirm_password']

    if request.method == 'POST':
        return render_template('pass_input.html')
    
    if request.method == 'POST':
             
        create_user(new_username, new_password, confirm_password)
        

        return render_template('pass_input.html')

@app.route('/test', methods=['GET', 'POST'])  
def create_keystrokes():
    global new_password
    global new_username
    global confirm_password

    if request.method == 'GET':
        create_user(new_username, new_password, confirm_password)
        return render_template('pass_input.html')

if __name__ == "__main__":
    app.run()

