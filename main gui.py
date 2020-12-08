from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from cryptography.fernet import Fernet
import cryptography
import pyAesCrypt
import decrypt
import os
key = Fernet.generate_key()
app = Flask(__name__)
bufferSize = 64 * 1024
password = "foopassword"
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    f = request.form['username']
    p = request.form['password']
    try:
        pyAesCrypt.decryptFile(f+".txt.aes", f+"out.txt", password, bufferSize)
        opened = open((f+".txt"), "r").read()
        if p in opened:
            session['logged_in'] = True
            return "Hello Boss!"
        else:
            print("What")
            flash('wrong password!')
            return home()
    except:
        flash('wrong password!')
        print("What")
        return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)