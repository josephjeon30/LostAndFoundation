# Python file for Flask routes

from flask import Flask, request, session, redirect, render_template
import db
from apis import duck, omdb, watchmode
app = Flask(__name__)
app.secret_key = "HI" # dummy key for now
db.db_table_inits()

def preset():
    db.create_movie("tt0389790", 'The Bee Movie', 2007, 'Fresh out of college, Barry the Bee finds the prospect of working with honey uninspiring. He flies outside the hive for the first time and talks to a human, breaking a cardinal rule of his species. Barry learns that humans have been stealing and eating honey for centuries, and he realizes that his true calling is to obtain justice for his kind by suing humanity for theft.', '', 'https://resizing.flixster.com/18icyRbPRhjrgvKB_7-9Z8lNrI0=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzA0MzljODE3LTgzMDMtNGRiOS1iOTM0LTM1ODk1ODMwNDIyOC53ZWJw')
    db.create_movie('tt13616990', 'Chainsaw Man', 2022, 'Following a betrayal, a young man left for the dead is reborn as a powerful devil-human hybrid after merging with his pet devil and is soon enlisted into an organization dedicated to hunting devils.', '', 'https://resizing.flixster.com/Y2EVUWoQ-QO0ixvBZY1gX5_zW_Q=/ems.cHJkLWVtcy1hc3NldHMvdHZzZXJpZXMvMjcxZDIzMDktYmMxZi00YTY1LTkwNmQtYjU5YThjNjRmZDE0LnBuZw==')
    db.create_movie('tt0108255', 'The Super Mario Bros. Movie', 2023, 'Mario make his first arrival to the Mushroom Kingdom, where a stranger from another land magically teleports into another unfamiliar world for adventure.', '', 'https://m.media-amazon.com/images/M/MV5BYjY5MTYwMDYtNDk4OS00NmE1LWI2ZjItY2Q5ZmVmNTU4NTAyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_FMjpg_UX1000_.jpg')
    db.create_movie('tt6226232', 'Young Sheldon', 2017, 'Meet a child genius named Sheldon Cooper (already seen as an adult in The Big Bang Theory (2007)) and his family. Some unique challenges face Sheldon, who is socially impaired.', '', 'https://m.media-amazon.com/images/M/MV5BZDg3MGNhYjItZGU2Yi00MzU4LWE4NGUtYjA2OTVjNGUyMjE4XkEyXkFqcGdeQXVyNjg4NzAyOTA@._V1_FMjpg_UX1000_.jpg')
    db.create_movie('tt5108870', 'Morbius', 2022, 'Biochemist Michael Morbius tries to cure himself of a rare blood disease, but he inadvertently infects himself with a form of vampirism instead.', '', 'https://www.sonypictures.com/sites/default/files/styles/max_560x840/public/title-key-art/morbius_onesheet_1400x2100_he.jpg?itok=-jQVkWIe')
    db.create_movie('tt2294629', 'Frozen', 2013, 'When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister Anna teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.', '', 'https://m.media-amazon.com/images/M/MV5BNzE1OTkwOTkwMV5BMl5BanBnXkFtZTgwNTcwMDk4NTE@._V1_.jpg')
    db.create_movie('tt0389790', 'The Bee Movie', 2007, 'Fresh out of college, Barry the Bee finds the prospect of working with honey uninspiring. He flies outside the hive for the first time and talks to a human, breaking a cardinal rule of his species. Barry learns that humans have been stealing and eating honey for centuries, and he realizes that his true calling is to obtain justice for his kind by suing humanity for theft.', '', 'https://resizing.flixster.com/18icyRbPRhjrgvKB_7-9Z8lNrI0=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzA0MzljODE3LTgzMDMtNGRiOS1iOTM0LTM1ODk1ODMwNDIyOC53ZWJw')
    db.create_movie('tt5108870', 'Morbius', 2022, 'Biochemist Michael Morbius tries to cure himself of a rare blood disease, but he inadvertently infects himself with a form of vampirism instead.', '', 'https://www.sonypictures.com/sites/default/files/styles/max_560x840/public/title-key-art/morbius_onesheet_1400x2100_he.jpg?itok=-jQVkWIe')
    db.create_movie('tt5108870', 'Morbius', 2022, 'Biochemist Michael Morbius tries to cure himself of a rare blood disease, but he inadvertently infects himself with a form of vampirism instead.', '', 'https://www.sonypictures.com/sites/default/files/styles/max_560x840/public/title-key-art/morbius_onesheet_1400x2100_he.jpg?itok=-jQVkWIe')
    db.create_movie('tt5108870', 'Morbius', 2022, 'Biochemist Michael Morbius tries to cure himself of a rare blood disease, but he inadvertently infects himself with a form of vampirism instead.', '', 'https://www.sonypictures.com/sites/default/files/styles/max_560x840/public/title-key-art/morbius_onesheet_1400x2100_he.jpg?itok=-jQVkWIe')
    db.create_movie( 'tt0389790', 'The Bee Movie', 2007, 'Fresh out of college, Barry the Bee finds the prospect of working with honey uninspiring. He flies outside the hive for the first time and talks to a human, breaking a cardinal rule of his species. Barry learns that humans have been stealing and eating honey for centuries, and he realizes that his true calling is to obtain justice for his kind by suing humanity for theft.', '', 'https://resizing.flixster.com/18icyRbPRhjrgvKB_7-9Z8lNrI0=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzA0MzljODE3LTgzMDMtNGRiOS1iOTM0LTM1ODk1ODMwNDIyOC53ZWJw')
    db.create_movie('tt5108870', 'Morbius', 2022, 'Biochemist Michael Morbius tries to cure himself of a rare blood disease, but he inadvertently infects himself with a form of vampirism instead.', '', 'https://www.sonypictures.com/sites/default/files/styles/max_560x840/public/title-key-art/morbius_onesheet_1400x2100_he.jpg?itok=-jQVkWIe')
    db.create_movie('tt5108870', 'Morbius', 2022, 'Biochemist Michael Morbius tries to cure himself of a rare blood disease, but he inadvertently infects himself with a form of vampirism instead.', '', 'https://www.sonypictures.com/sites/default/files/styles/max_560x840/public/title-key-art/morbius_onesheet_1400x2100_he.jpg?itok=-jQVkWIe')

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
    
    db.create_user(user, pwd, duck.get_duck())
    session['username'] = user
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' not in session:
        return redirect('/login')
    preset()
    print(session)
    return render_template('index.html', movies = db.get_movies())

@app.route('/view/<imdb_id>', methods=['GET'])
def view_movie(imdb_id):
    movie_info = ()
    if not db.check_movie_exists(imdb_id):
        mv = omdb.get_info(imdb_id)
        print(mv)
        tomato_rating = mv['Ratings'][1]['Source'] + ": " + mv['Ratings'][1]['Value'] 
        db.create_movie(mv['imdbID'],mv['Title'], mv['Year'], mv['Plot'],tomato_rating,  mv['Poster'])
    movie_info = db.get_movie(imdb_id)
    return render_template('view.html', movie = movie_info) 

@app.route('/search', methods=['GET', 'POST'])
def movie_search():
    if 'username' not in session:
        return redirect('/login')
    try:
        res = ()
        title = request.args['search'].strip()
        res = omdb.search(title)
        print(res)
        return render_template('search.html', results = res) 
    except:
        return render_template('search.html', results = []) 

@app.route('/profile', methods=['GET', 'POST'])
def show_profile():
    if 'username' not in session:
        return redirect('/login')
    return render_template('profile.html', username = session['username'], pfp = db.get_user_data(session['username'])[1])

@app.route('/changepfp', methods=['GET', 'POST'])
def change_pfp():
    if 'username' not in session:
        return redirect('/login')
    db.update_user_pfp(session['username'], duck.get_duck())
    return redirect('/profile')
    
if __name__ == '__main__':
    app.debug = True
    app.run()