from flask import Flask, request, render_template, redirect, abort, session, url_for
import random
import os

app = Flask(__name__, template_folder='template_html')
app.secret_key = os.urandom(24)  # Set a secret key for the session.


@app.route('/users')
def get_users():
    if 'username' in session:
        greeting = f'Hello, {session["username"]}'
        logout_btn = '<a class="logout-btn" href="/logout">Logout</a>'
    else:
        greeting = ''
        logout_btn = ''
    names = ['Alice', 'Anna', 'Vitalij', 'Vlad', 'Bob']
    count = random.randint(1, len(names))
    random.shuffle(names)
    return render_template('users.html', greeting=greeting, logout_btn=logout_btn, names=names, count=count)


@app.route('/books')
def get_books():
    if 'username' in session:
        greeting = f'Hello, {session["username"]}'
        logout_btn = '<a class="logout-btn" href="/logout">Logout</a>'
    else:
        greeting = ''
        logout_btn = ''
    books = ['Kobzar', 'Harry Potter', 'Abetka', 'Witcher', 'Alice in Wonderland']
    count = random.randint(1, len(books))
    random.shuffle(books)
    html_list = '<ul>'
    for book in books[:count]:
        html_list += f'<li>{book}</li>'
    html_list += '</ul>'
    return render_template('books.html', greeting=greeting, logout_btn=logout_btn, html_list=html_list)


@app.get('/books/<string:title>')
def transform_title(title):
    books = ['Kobzar', 'Harry Potter', 'Abetka', 'Witcher', 'Alice in Wonderland']
    result = books.count(title)
    if result > 0:
        transformed_title = title.capitalize()
        return transformed_title
    else:
        abort(500)


@app.route('/params')
def get_params():
    if 'username' in session:
        greeting = f'Hello, {session["username"]}'
        logout_btn = '<a class="logout-btn" href="/logout">Logout</a>'
    else:
        greeting = ''
        logout_btn = ''
    params = request.args
    return render_template('params.html', params=params, greeting=greeting, logout_btn=logout_btn)


# Exercise 2
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = render_template('login.html')
        return form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validating username and password (you can add your own validation logic)
        if len(username) < 5:
            abort(400, 'Username must be at least 5 characters long')
        elif len(password) < 8 or not any(char.isdigit() for char in password) or not any(
                char.isupper() for char in password):
            abort(400, 'Invalid password')

        # Store the username in the session
        session['username'] = username

        return redirect('/')


@app.get('/users/<int:count>')
def get_users_count(count):
    if 'username' in session:
        greeting = f'Hello, {session["username"]}'
        logout_btn = '<a class="logout-btn" href="/logout">Logout</a>'
    else:
        greeting = ''
        logout_btn = ''

    names = ['Alice', 'Anna', 'Vitalij', 'Vlad', 'Bob']

    if count > 0:
        count = min(count, len(names))
        selected_names = random.sample(names, count)
        users_list = selected_names
    else:
        random.shuffle(names)
        users_list = names

    return render_template('users_id.html', greeting=greeting, logout_btn=logout_btn, users=users_list)


@app.get('/books/<int:count>')
def get_books_count(count):
    if 'username' in session:
        greeting = f'Hello, {session["username"]}'
        logout_btn = '<a class="logout-btn" href="/logout">Logout</a>'
    else:
        greeting = ''
        logout_btn = ''

    books = ['Kobzar', 'Harry Potter', 'Abetka', 'Witcher', 'Alice in Wonderland']

    if count > 0:
        count = min(count, len(books))
        selected_books = random.sample(books, count)
        books_list = selected_books
    else:
        random.shuffle(books)
        books_list = books

    return render_template('books_id.html', greeting=greeting, logout_btn=logout_btn, books=books_list)


@app.route('/')
def home():
    if 'username' in session:
        greeting = f'Hello, {session["username"]}'
        logout_btn = '<a class="logout-btn" href="/logout">Logout</a>'
    else:
        greeting = ''
        logout_btn = ''
    return render_template('home.html', greeting=greeting, logout_btn=logout_btn)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = '''
            <form method="post" action="/register">
                <input type="text" name="username" placeholder="Username" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <input type="email" name="email" placeholder="Email" required><br>
                <input type="submit" value="Register">
            </form>
        '''
        return form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        if len(username) < 5:
            abort(400, 'Username must be at least 5 characters long')
        elif len(password) < 8 or not any(char.isdigit() for char in password) or not any(
                char.isupper() for char in password):
            abort(400, 'Invalid password')
        elif '@' not in email:
            abort(400, 'Invalid email')

        return f'Registration successful: username={username}, email={email}'


# Exercise 3 Check if the session contains a username on all pages
@app.before_request
def check_session_username():
    if request.endpoint in ['login', 'register', 'static']:
        return  # Exclude login, register, and static endpoints from session check

    if 'username' not in session:
        return redirect(url_for('login'))


# Exercise 4 Logout functionality
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
