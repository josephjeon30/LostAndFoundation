# Python file for Flask routes

from flask import Flask, request, session, redirect, render_template

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

@app.route('/signup', methods=['GET'])
def signup():
    if 'username' in session:
        return redirect('/home')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    redirect('/')

@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'POST':
        if 'username' in request.form:
            user = request.form['username']
            pwd = request.form['password']
        if 'login' in request.form: # check if login or signup
            # check if login info in db
            print('foo')
        elif 'signup' in request.form:
            # check if username is unique
            print('foo')
    user = session['username']
    redirect('/home')

@app.route('/home', methods=['POST'])
def home():
    if 'username' in session:
        return render_template('home.html')
    redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run()