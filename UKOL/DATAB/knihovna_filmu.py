import sqlite3


def create_connection():
    return sqlite3.connect('filmova_knihovna.db')

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            release_year INTEGER,
                            genre TEXT,
                            director_id INTEGER,
                            FOREIGN KEY(director_id) REFERENCES directors(id)
                        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS actors (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            birth_year INTEGER
                        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS directors (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            birth_year INTEGER
                        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS movie_actors (
                            movie_id INTEGER,
                            actor_id INTEGER,
                            PRIMARY KEY (movie_id, actor_id),
                            FOREIGN KEY(movie_id) REFERENCES movies(id),
                            FOREIGN KEY(actor_id) REFERENCES actors(id)
                        )''')

    conn.commit()
    conn.close()

create_tables()

def add_movie(title, release_year, genre, director_name, director_birth_year, actors):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO directors (name, birth_year) VALUES (?, ?)",
                   (director_name, director_birth_year))
    director_id = cursor.lastrowid

    cursor.execute("INSERT INTO movies (title, release_year, genre, director_id) VALUES (?, ?, ?, ?)",
                   (title, release_year, genre, director_id))
    movie_id = cursor.lastrowid

    for actor_name, actor_birth_year in actors:
        cursor.execute("INSERT INTO actors (name, birth_year) VALUES (?, ?)",
                       (actor_name, actor_birth_year))
        actor_id = cursor.lastrowid

        cursor.execute("INSERT INTO movie_actors (movie_id, actor_id) VALUES (?, ?)",
                       (movie_id, actor_id))

    conn.commit()
    conn.close()

add_movie(
    "Shindleruv seznam",
    1993,
    "History, Drama",
    "Steven Spielberg",
    1946,
    [
        ("Liam Neeson", 1952),
        ("Ben Kingsley", 1943)
    ]
)
add_movie(
    "Pelíšky",
    1999,
    "Komedie, Drama",
    "Jan Hřebejk",
    1967,
    [
        ("Miroslav Donutil", 1951),
        ("Jiří Kodet", 1937)
    ]
)

def add_actor(name, birth_year):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO actors (name, birth_year) VALUES (?, ?)",
                   (name, birth_year))
    conn.commit()
    conn.close()

def add_director(name, birth_year):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO directors (name, birth_year) VALUES (?, ?)",
                   (name, birth_year))
    conn.commit()
    conn.close()

add_actor("Leonardo DiCaprio", 1974)
add_director("Miloš Forman", 1932)

def search_movie_by_title(title):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE title LIKE ?", ('%' + title + '%',))
    movies = cursor.fetchall()
    conn.close()
    return movies

movies = search_movie_by_title("Shindleruv seznam")
for movie in movies:
    print(movie)


def update_movie(movie_id, title=None, release_year=None, genre=None, director_id=None):
    conn = create_connection()
    cursor = conn.cursor()


def delete_movie(movie_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()
    conn.close()

delete_movie(1)
print(movie)

