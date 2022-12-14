import sqlite3, random as rand
from datetime import datetime

DB_FILE = "data.db"

db = None

def db_connect():
    global db
    db = sqlite3.connect(DB_FILE)
    return db.cursor()

def db_close():
    db.commit()
    db.close()

def db_table_inits(): 
    # Creates users table if it doesn't exist
    # Creats movies table
    c = db_connect()
    c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text, pfp text, themeID int)")
    c.execute("CREATE TABLE IF NOT EXISTS movies (mov_id text, name text, year int, synopsis text, rating text, streaming text, trailer text, poster text)")
    c.execute("CREATE TABLE IF NOT EXISTS comments (mov_id text, username text, content text, upload_time text, pfp text)")
    db_close()

def check_movie_exists(mov_id):  
    c = db_connect()
    c.execute('SELECT mov_id FROM movies WHERE mov_id=?', [mov_id])
    mov = c.fetchone()
    db_close()
    return bool(mov)

def create_movie(mov_id, name, year, synopsis, rating, streaming, trailer, poster): 
    if (not check_movie_exists(mov_id)):
        c = db_connect() 
        c.execute('INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (mov_id, name, year, synopsis, rating, streaming, trailer, poster))
        db_close()
    
def check_user_exists(username): 
    c = db_connect()
    c.execute('SELECT username FROM users WHERE username=?', [username])
    user = c.fetchone() 
    db_close()
    return bool(user)

def create_user(username, password, pfp, themeID): 
    c = db_connect()
    c.execute('INSERT INTO users VALUES (?,?,?,?)', (username, password, pfp, themeID))
    db_close()

def create_comment(mov_id, username, content):
    pfp = get_user_data(username)[1]
    c = db_connect()
    now = datetime.now()
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")
    c.execute('INSERT INTO comments VALUES (?,?,?,?,?)', (mov_id, username, content, dt_string, pfp))
    db_close()

def get_comments(movie_id):
    c = db_connect()
    c.execute('SELECT * FROM comments WHERE mov_id=?', [movie_id])
    info = c.fetchall()
    print(info)
    db.close()
    return info

def verify_login(username, password):
    c = db_connect()
    c.execute('SELECT username,password FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()
    db.close()
    if user: 
        return True
    return False

def get_movie(movie_id):  #returns a tuple of all info for a specific movie - used on movie page 
    c = db_connect()
    c.execute('SELECT * FROM movies WHERE mov_id=?', [movie_id])
    info = c.fetchall()
    db.close()
    return info[0]

def get_movies():
    c = db_connect()
    c.execute('SELECT * FROM movies')
    info = c.fetchall()
    db.close()
    return info

def get_last_movie(): 
    c = db_connect()
    c.execute('SELECT * FROM movies')
    info = c.fetchall()[-1]
    db.close()
    return info

def get_user_data(username):
    c = db_connect()
    c.execute('SELECT password,pfp,themeID FROM users WHERE username=?', [username])
    user_data = c.fetchone()
    db.close()
    return user_data

def update_user_pfp(username, pfp):
    c = db_connect()
    c.execute('UPDATE users SET pfp=? WHERE username=?', (pfp, username))
    c.execute('UPDATE comments SET pfp=? WHERE username=?', (pfp, username))
    db.commit()
    db.close()
    return None

def update_user_theme(username, themeID):
    c = db_connect()
    c.execute('UPDATE users SET themeID=? WHERE username=?', (themeID, username))
    db.commit()
    db.close()
    return None

def update_user_passwd(username, password):
    c = db_connect()
    c.execute('UPDATE users SET password=? WHERE username=?', (password,username) )
    db.commit()
    db.close()
    return None


