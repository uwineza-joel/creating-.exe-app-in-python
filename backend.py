import sqlite3

def connect():
    conn = sqlite3.connect('songs.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS song(id INTEGER PRIMARY KEY, title text, singer text, album text, year integer)")
    conn.commit()
    conn.close()

def insert(title, singer, album, year):
    conn = sqlite3.connect('songs.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO song VALUES(NULL, ?, ?, ?, ?)", (title, singer, album, year))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('songs.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", singer="", album="", year=""):
    conn = sqlite3.connect('songs.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM song WHERE title=? OR singer=? OR album=? OR year=?", (title, singer, album, year))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('songs.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM song WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, singer, album, year):
    conn = sqlite3.connect('songs.db')
    cur = conn.cursor()
    cur.execute("UPDATE song SET title=?, singer=?, album=?, year=? WHERE id=?", (title, singer, album, year, id))
    conn.commit()
    conn.close()

connect() 
#insert("Love like you do lyrics", "Ellie Goulding", "The Goldian", 2019)
#update(2, "Love like you do lyrics", "Ellie Goulding", "The Goldian", 2020)
#delete(3)
#print(view())
#print(search(year="2019"))