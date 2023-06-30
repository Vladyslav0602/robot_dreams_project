from flask import Flask, request, render_template, redirect, abort
import random

app = Flask(__name__, template_folder='template_html')


# Exercise 1
@app.route('/users', methods=['GET'])
def get_users():
    names = ['Alice', 'Anna', 'Vitalij', 'Vlad', 'Bob']
    random.shuffle(names)
    return ', '.join(names)


@app.route('/books', methods=['GET'])
def get_books():
    books = ['Kobzar', 'Harry Potter', 'Abetka', 'Witcher', 'Alice in Wonderland']
    random.shuffle(books)
    html_list = '<ul>'
    for book in books:
        html_list += f'<li>{book}</li>'
    html_list += '</ul>'
    return html_list


# Exercise 2
@app.route('/users/id', methods=['GET'])
def get_users_by_id():
    user_id = request.args.get('id')
    if user_id:
        user_id = int(user_id)
        if user_id % 2 == 0:
            return f'Text with id: {user_id}'
        else:
            abort(404)
    else:
        names = ['Alice', 'Anna', 'Vitalij', 'Vlad', 'Bob']
        random.shuffle(names)
        return ', '.join(names)


@app.route('/books/title', methods=['GET'])
def get_books_by_title():
    title = request.args.get('title')
    if title:
        transformed_title = title.capitalize()
        return transformed_title
    else:
        books = ['Kobzar', 'Harry Potter', 'Abetka', 'Witcher', 'Alice in Wonderland']
        random.shuffle(books)
        html_list = '<ul>'
        for book in books:
            html_list += f'<li>{book}</li>'
        html_list += '</ul>'
        return html_list


# Exercise 3
@app.route('/params', methods=['GET'])
def get_params():
    params = request.args
    return render_template('params.html', params=params)


# Exercise 4
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = '''
            <form method="post" action="/login">
                <input type="text" name="username" placeholder="Username" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <input type="submit" value="Login">
            </form>
        '''
        return form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if len(username) < 5:
            abort(400, 'Username must be at least 5 characters long')
        elif len(password) < 8 or not any(char.isdigit() for char in password) or not any(
                char.isupper() for char in password):
            abort(400, 'Invalid password')

        return redirect('/users')


# Exercise 5
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


# Exercise 6
@app.route('/')
def home():
    return '''
        <h1>Welcome to the Home Page</h1>
        <ul>
            <li><a href="/login">Login</a></li>
            <li><a href="/users">Users</a></li>
            <li><a href="/books">Books</a></li>
            <li><a href="/params">Params</a></li>
        </ul>
    '''


# Exercise 7
@app.route('/users/count', methods=['GET'])
def get_users_with_count():
    count = request.args.get('count')
    if count:
        count = int(count)
    else:
        count = random.randint(1, 10)  # Рандомна кількість, якщо параметр не передано

    if request.args.get('id'):
        user_id = int(request.args.get('id'))
        if user_id % 2 == 0:
            return f'Text with id: {user_id}'
        else:
            abort(404)
    else:
        names = ['Alice', 'Anna', 'Vitalij', 'Vlad', 'Bob']
        random.shuffle(names)
        return ', '.join(names[:count])


@app.route('/books/count', methods=['GET'])
def get_books_with_count():
    count = request.args.get('count')
    if count:
        count = int(count)
    else:
        count = random.randint(1, 10)  # Рандомна кількість, якщо параметр не передано

    if request.args.get('title'):
        title = request.args.get('title')
        transformed_title = title.capitalize()
        return transformed_title
    else:
        books = ['Kobzar', 'Harry Potter', 'Abetka', 'Witcher', 'Alice in Wonderland']
        random.shuffle(books)
        return ', '.join(books[:count])


# Exercise 8
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


if __name__ == '__main__':
    app.run()
