import sqlite3, random as rand

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
    c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text, pfp text)")
    c.execute("CREATE TABLE IF NOT EXISTS movies (mov_id int, name text, year int, synopsis text, trailer text, poster text)")
    db_close()

def check_movie_exists(mov_id):  
    c = db_connect()
    c.execute('SELECT id FROM movies WHERE mov_id=?', (mov_id))
    mov = c.fetchone()
    db_close()
    if mov: 
        return False
    return True

def create_movie(mov_id, name, year, synopsis, trailer, poster): 
    c = db_connect() 
    if (check_movie_not_exists(mov_id)):
        c.execute('INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?)', (mov_id, name, year, synopsis, trailer, poster))
    db_close()
    
def check_user_exists(username): 
    c = db_connect()
    c.execute('SELECT username FROM users WHERE username=?', [username])
    user = c.fetchone() 
    db_close()
    return bool(user)

def create_user(username, password, pfp): 
    c = db_connect()
    c.execute('INSERT INTO users VALUES (?,?,?)', (username, password, pfp))
    db_close()

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
    c.execute('SELECT * FROM movies WHERE mov_id=?', (movie_id))
    info = c.fetchall()
    print(info)
    print(info[0])
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


