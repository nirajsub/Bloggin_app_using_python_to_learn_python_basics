from authentication import create_user, authenticate_user
from post import create_post, get_all_posts
from database import create_tables
create_tables()

logged_in = False  # Set initial logged-in status as False
current_user_id = None  # Store the current user ID

def menu():
    print('1. Create a new user')
    print('2. Login')
    print('3. Create new post')
    print('4. View all posts')
    print('5. Logout')
    print('q. Quit')

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
    user_id = authenticate_user(username, password)
    if user_id:
        logged_in = True
        current_user_id = user_id
        print('Login successful!')
        return True, user_id
    else:
        print('Invalid credentials.')
        return False, None

def create_new_post(user_id):
    title = input('Enter post title: ')
    content = input('Enter post content: ')
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

def logoutmenu():
    print('1. Get Menu')
    print('2. Login')
    answer = input('Enter your choice..:')
    return answer

def logout():
    global logged_in, current_user_id  # Access the global logged_in variable
    if logged_in:
        logged_in = False  # Set logged-in status to False
        current_user_id = None # Reset the current user ID
        print('Logout successful!')
    else:
        print('You are not currently logged in.')
    answer = logoutmenu()
    while answer != '1':
        if answer == '2':
            logged_in, user_id = login()
        else:
            print('Invalid choice.')
        answer = menu()

choice = menu()
while choice != 'q':
    if choice == '1':
        create_new_user()
    elif choice == '2':
        logged_in, user_id = login()
    elif choice == '3':
        if logged_in:
            create_new_post(user_id)
        else:
            print('Please login first.')
    elif choice == '4':
            view_all_posts(user_id)
    elif choice == '5':
                logout()
    else:
        print('Invalid choice.')
    choice = menu()