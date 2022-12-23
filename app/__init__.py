# Python file for Flask routes

from flask import Flask, request, session, redirect, render_template
import db
from apis import duck, omdb, watchmode
app = Flask(__name__)
app.secret_key = "HI" # dummy key for now
db.db_table_inits()

def preset():
    db.create_movie("tt0389790", 'The Bee Movie', 2007, 'Fresh out of college, Barry the Bee finds the prospect of working with honey uninspiring. He flies outside the hive for the first time and talks to a human, breaking a cardinal rule of his species. Barry learns that humans have been stealing and eating honey for centuries, and he realizes that his true calling is to obtain justice for his kind by suing humanity for theft.', '6.1', "Netflix" ,'https://www.youtube.com/embed/VONRQMx78YI', 'https://resizing.flixster.com/18icyRbPRhjrgvKB_7-9Z8lNrI0=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzA0MzljODE3LTgzMDMtNGRiOS1iOTM0LTM1ODk1ODMwNDIyOC53ZWJw')
    db.create_movie('tt0108255', 'The Super Mario Bros. Movie', 2023, 'Mario make his first arrival to the Mushroom Kingdom, where a stranger from another land magically teleports into another unfamiliar world for adventure.', 'N/A', 'Yet to be released', 'https://www.youtube.com/embed/TnGl01FkMMo', 'https://m.media-amazon.com/images/M/MV5BYjY5MTYwMDYtNDk4OS00NmE1LWI2ZjItY2Q5ZmVmNTU4NTAyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_FMjpg_UX1000_.jpg')
    db.create_movie('tt13616990', 'Chainsaw Man', 2022, 'Following a betrayal, a young man left for the dead is reborn as a powerful devil-human hybrid after merging with his pet devil and is soon enlisted into an organization dedicated to hunting devils.', '8.8','Netflix', 'https://www.youtube.com/embed/j9sSzNmB5po' , 'https://m.media-amazon.com/images/M/MV5BZjY5MDFhZTgtOGVhMi00NTUzLTk5NjktNmRlMjI3NjI4MmE0XkEyXkFqcGdeQXVyMTMzNDExODE5._V1_SX300.jpg')
    db.create_movie('tt6226232', 'Young Sheldon', 2017, 'Meet a child genius named Sheldon Cooper (already seen as an adult in The Big Bang Theory (2007)) and his family. Some unique challenges face Sheldon, who is socially impaired.', '7.6', 'Netflix', 'https://www.youtube.com/embed/YsGmUhjvqSo', 'https://m.media-amazon.com/images/M/MV5BZDg3MGNhYjItZGU2Yi00MzU4LWE4NGUtYjA2OTVjNGUyMjE4XkEyXkFqcGdeQXVyNjg4NzAyOTA@._V1_FMjpg_UX1000_.jpg')
    db.create_movie('tt5108870', 'Morbius', 2022, 'Biochemist Michael Morbius tries to cure himself of a rare blood disease, but he inadvertently infects himself with a form of vampirism instead.', '5.2', 'Netflix', 'https://www.youtube.com/embed/oZ6iiRrz1SY' , 'https://www.sonypictures.com/sites/default/files/styles/max_560x840/public/title-key-art/morbius_onesheet_1400x2100_he.jpg?itok=-jQVkWIe')
    db.create_movie('tt2294629', 'Frozen', 2013, 'When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister Anna teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.', '7.4','Netflix', 'https://www.youtube.com/embed/TbQm5doF_Uc' , 'https://m.media-amazon.com/images/M/MV5BNzE1OTkwOTkwMV5BMl5BanBnXkFtZTgwNTcwMDk4NTE@._V1_.jpg')
    db.create_movie('tt0903747', 'Breaking Bad', 2008, 'A chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine with a former student in order to secure his family\'s future.','9.5', 'Netflix', 'https://www.youtube.com/embed/2gTC4uWP3_Y', 'https://m.media-amazon.com/images/M/MV5BYTU3NWI5OGMtZmZhNy00MjVmLTk1YzAtZjA3ZDA3NzcyNDUxXkEyXkFqcGdeQXVyODY5Njk4Njc@._V1_FMjpg_UY474_.jpg')
    for i in ['tt0347149', 'tt0266543', 'tt0120338']:
        try:
            mv = omdb.get_info(i)
            trailer = watchmode.get_trailer(i)
            print(mv)
            rating = mv['imdbRating'] 
            db.create_movie(mv['imdbID'],mv['Title'], mv['Year'], mv['Plot'],rating, '', trailer, mv['Poster'])
        except:
            print("oopsy poopsy")
    db.create_user('jo', 'qwe', duck.get_duck(), 0)
    db.create_comment('tt5108870', 'jo', 'When i was 13, i came out to my parents as a morbius male. They couldnt accept my morbality, so they sent me off to camp. They just didnt understand— i was morbed that way. At the camp, they gave us electromorb therapy to morb us into beta males. I resisted the treatment, being a morbius male, you cant morb me out of being morbed. I fooled the counselors into thinking they had successfully morbed be into a beta male, and i returned home. To this day, i live a double life— one for my parents, who still cannot accept morbality, and one where its always morbin time.')

@app.route('/login', methods=['GET'])
def login():
    if 'username' in session:
        if not db.check_user_exists(session['username']):
            return redirect('/logout')
        return redirect('/')
    movlist = db.get_movies()
    if len(movlist) < 1:
        preset()
    print(db.check_user_exists('jo'))
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
    
    db.create_user(user, pwd, duck.get_duck(), 0)
    session['username'] = user
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' not in session :
        return redirect('/login')
    if not db.check_user_exists(session['username']):
        return redirect('/login')
    movlist = db.get_movies()
    return render_template('index.html', movies = movlist, info = db.get_user_data(session['username']))

@app.route('/view/<imdb_id>', methods=['GET', 'POST'])
def view_movie(imdb_id):
    if 'username' not in session:
        return redirect('/login')
    movie_info = ()
    streams = watchmode.get_streaming(imdb_id)
    if len(request.args) > 0:
        db.create_comment(imdb_id, session['username'], request.args['cmnt'])
        return redirect('/view/' + imdb_id)
    if not db.check_movie_exists(imdb_id):
        mv = omdb.get_info(imdb_id)
        trailer = watchmode.get_trailer(imdb_id)
        rating = mv['imdbRating'] 
        db.create_movie(mv['imdbID'],mv['Title'], mv['Year'], mv['Plot'],rating, '', trailer, mv['Poster'])
    movie_info = db.get_movie(imdb_id)
    return render_template('view.html', movie = movie_info, streaming = streams, info = db.get_user_data(session['username']), comments = db.get_comments(imdb_id)) 

@app.route('/search/<page>', methods=['GET', 'POST'])
def movie_search(page):
    if 'username' not in session:
        return redirect('/login')
    try:
        res = ()
        title = request.args['search'].strip()
        res = omdb.search(title, page)
        print(res)
        return render_template('search.html', results = res, searched = request.args['search'], pg = page, info = db.get_user_data(session['username']), page=page) 
    except:
        return render_template('search.html', results = [], searched = '', pg = -1, info = db.get_user_data(session['username'])) 

@app.route('/profile', methods=['GET', 'POST'])
def show_profile():
    if 'username' not in session:
        return redirect('/login')
    return render_template('profile.html', username = session['username'], info = db.get_user_data(session['username']))

@app.route('/changepfp', methods=['GET', 'POST'])
def change_pfp():
    if 'username' not in session:
        return redirect('/login')
    db.update_user_pfp(session['username'], duck.get_duck())
    return redirect('/profile')

@app.route('/changetheme', methods=['GET', 'POST'])
def change_theme():
    if 'username' not in session:
        return redirect('/login')
    print(db.get_user_data(session['username']))
    temp = (db.get_user_data(session['username'])[2] + 1) % 2
    db.update_user_theme(session['username'], temp) 
    return redirect('/profile')
    
if __name__ == '__main__':
    app.debug = True
    app.run()