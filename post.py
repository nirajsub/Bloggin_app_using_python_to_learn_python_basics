
import sqlite3

def create_post(title, content, user_id):
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)', (title, content, user_id))
    conn.commit()
    conn.close()

def get_all_posts():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT posts.id, title, content, username, timestamp FROM posts INNER JOIN users ON posts.user_id = users.id ORDER BY timestamp DESC')
    posts = cursor.fetchall()
    conn.close()
    return posts