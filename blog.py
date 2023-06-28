from authentication import create_user, authenticate_user
from post import create_post, get_all_posts
from database import create_tables

create_tables()

def menu():
    print('1. Create a new user')
    print('2. Login')
    print('3. Create new post')
    print('4. View all posts')
    print('5. Quit')

    choice = input('Enter your choice..:')
    return choice

def create_new_user():
    username = input('Enter username: ')
    password = input('Enter password: ')
    create_user(username, password)
    print('User created successfully!')

def login():
    username = input('Enter username: ')
    password = input('Enter password: ')
    if authenticate_user(username, password):
        print('Login successful!')
        return True
    else:
        print('Invalid credentials.')
        return False

def create_new_post():
    title = input('Enter post title: ')
    content = input('Enter post content: ')
    user_id = 1  # Assuming a single user for simplicity. You can enhance this for multiple users.
    create_post(title, content, user_id)
    print('Post created successfully!')

def view_all_posts():
    posts = get_all_posts()
    if not posts:
        print('No posts found.')
    else:
        for post in posts:
            post_id, title, content, username, timestamp = post
            print(f'Post ID: {post_id}')
            print(f'Title: {title}')
            print(f'Content: {content}')
            print(f'Author: {username}')
            print(f'Timestamp: {timestamp}')
            print('---')

choice = menu()

while choice != '5':
    if choice == '1':
        create_new_user()
    elif choice == '2':
        if login():
            logged_in = True
        else:
            logged_in = False
    elif choice == '3':
        if logged_in:
            create_new_post()
        else:
            print('Please login first.')
    elif choice == '4':
        view_all_posts()
    else:
        print('Invalid choice.')

    choice = menu()