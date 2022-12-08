# Python file for Flask routes

from flask import Flask, request, session, redirect, render_template
import db

app = Flask(__name__)
app.secret_key = "HI" # dummy key for now

@app.route('/', methods=['GET'])
def login():
    if 'username' in session:
        return redirect('/home')
    return render_template('login.html')

@app.route('/signup', methods=['GET'])
def signup():
    if 'username' in session:
        return redirect('/home')
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

@app.route('/auth/login', methods=['GET', 'POST'])
def authenticate_login():
    if request.method != 'POST':
        return redirect('/')

    user = request.form['username']
    pwd = request.form['password']

    if not verify_login(user, pwd):
        return render_template('login.html', status = 'error')
    session['username'] = user
    return redirect('/home')

@app.route('/auth/signup', methods=['GET', 'POST'])
def authenticate_signup():
    if request.method != 'POST':
        return redirect('/')
    user = request.form['username']
    pwd = request.form['password']

    if check_user_exists(user):
        return render_template('signup.html', error = 'user_exists')
    
    if pwd != request.form['confirmation']:
        return render_template('signup.html', error = 'pwd_mismatch')
    
    create_user(user, pwd, 'pfp_placeholder')
    session['username'] = user
    return redirect('/home')

@app.route('/home', methods=['POST'])
def home():
    if 'username' not in session:
        return redirect('/')
    return render_template('home.html')

if __name__ == '__main__':
    app.debug = True
    app.run()