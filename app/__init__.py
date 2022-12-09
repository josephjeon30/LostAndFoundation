# Python file for Flask routes

from flask import Flask, request, session, redirect, render_template
import db

app = Flask(__name__)
app.secret_key = "HI" # dummy key for now
db.db_table_inits()
create_movie(0, 'The Bee Movie', 2007, 'Fresh out of college, Barry the Bee finds the prospect of working with honey uninspiring. He flies outside the hive for the first time and talks to a human, breaking a cardinal rule of his species. Barry learns that humans have been stealing and eating honey for centuries, and he realizes that his true calling is to obtain justice for his kind by suing humanity for theft.', '', 'https://resizing.flixster.com/18icyRbPRhjrgvKB_7-9Z8lNrI0=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzA0MzljODE3LTgzMDMtNGRiOS1iOTM0LTM1ODk1ODMwNDIyOC53ZWJw')
create_movie(1, 'Chainsaw Man', 2022, 'Following a betrayal, a young man left for the dead is reborn as a powerful devil-human hybrid after merging with his pet devil and is soon enlisted into an organization dedicated to hunting devils.', '', 'https://resizing.flixster.com/Y2EVUWoQ-QO0ixvBZY1gX5_zW_Q=/ems.cHJkLWVtcy1hc3NldHMvdHZzZXJpZXMvMjcxZDIzMDktYmMxZi00YTY1LTkwNmQtYjU5YThjNjRmZDE0LnBuZw==')

@app.route('/login', methods=['GET'])
def login():
    if 'username' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/signup', methods=['GET'])
def signup():
    if 'username' in session:
        return redirect('/')
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

    if not db.verify_login(user, pwd):
        return render_template('login.html', status = 'error')
    session['username'] = user
    return redirect('/')

@app.route('/auth/signup', methods=['GET', 'POST'])
def authenticate_signup():
    if request.method != 'POST':
        return redirect('/')
    user = request.form['username']
    pwd = request.form['password']

    if db.check_user_exists(user):
        return render_template('signup.html', error = 'user_exists')
    
    if pwd != request.form['confirmation']:
        return render_template('signup.html', error = 'pwd_mismatch')
    
    db.create_user(user, pwd, 'pfp_placeholder')
    session['username'] = user
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' not in session:
        return redirect('/login')
    print(get_movies())
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()