from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime


# Load the environment variables from .env file
load_dotenv()

app = Flask(__name__)
FLASK_APP = os.getenv('FLASK_APP')
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_NAME = os.getenv('DATABASE_NAME')
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# Configuring the app
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Filling data into a table
# def seed_database():
#     # Adding Users
#     user1 = User(name='John Dorn', email='john_dorn@example.com')
#     user2 = User(name='Jane Smith', email='jane@example.com')
#     user3 = User(name='Benjamin Anderson', email='benjamin.anderson@example.com')
#     user4 = User(name='Chloe Williams', email='chloe.williams@example.com')
#     user5 = User(name='Daniel Martinez', email='daniel.martinez@example.com')
#     user6 = User(name='Emma Thompson', email='emma.thompson@example.com')
#     user7 = User(name='Grace Turner', email='grace.turner@example.com')
#     user8 = User(name='Henry Mitchell', email='henry.mitchell@example.com')
#
#     # Adding Books
#     book1 = Book(title='The Midnight Star', author='Alex Turner', price=29.99)
#     book2 = Book(title='Whispers in the Dark', author='Emily Parker', price=19.99)
#     book3 = Book(title='The Forgotten Realm', author='Michael Roberts', price=35.69)
#     book4 = Book(title='Echoes of Eternity', author='Sarah Bennett', price=15.78)
#     book5 = Book(title='The Enchanted Forest', author='Christopher Scott', price=49.85)
#     book6 = Book(title='A Twist of Fate', author='Jessica Evans', price=21.45)
#     book7 = Book(title='Shadows of the Past', author='David Sullivan', price=37.99)
#     book8 = Book(title='Beyond the Horizon', author='Jennifer Adams', price=43.47)
#
#     # Add users and books to the database
#     db.session.add_all([user1, user2, user3, user4, user5, user6, user7, user8, book1, book2, book3, book4, book5, book6, book7, book8])
#     db.session.commit()
#
#     # Now that the users and books are saved in the database, you can add purchases with the correct user_id and book_id
#     purchase1 = Purchase(user_id=user1.id, book_id=book1.id, purchase_date=datetime.now())
#     purchase2 = Purchase(user_id=user2.id, book_id=book2.id, purchase_date=datetime.now())
#     purchase3 = Purchase(user_id=user3.id, book_id=book3.id, purchase_date=datetime.now())
#     purchase4 = Purchase(user_id=user4.id, book_id=book4.id, purchase_date=datetime.now())
#     purchase5 = Purchase(user_id=user5.id, book_id=book5.id, purchase_date=datetime.now())
#     purchase6 = Purchase(user_id=user6.id, book_id=book6.id, purchase_date=datetime.now())
#     purchase7 = Purchase(user_id=user7.id, book_id=book7.id, purchase_date=datetime.now())
#     purchase8 = Purchase(user_id=user8.id, book_id=book8.id, purchase_date=datetime.now())
#
#     # Adding purchases to the database
#     db.session.add_all([purchase1, purchase2, purchase3, purchase4, purchase5, purchase6, purchase7, purchase8])
#     db.session.commit()


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    purchases = db.relationship('Purchase', back_populates='user')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    purchases = db.relationship('Purchase', back_populates='book')

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'price': self.price,
        }


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', back_populates='purchases')
    book = db.relationship('Book', back_populates='purchases')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'purchase_date': self.purchase_date.isoformat(),
        }


# Endpoints
# Exercise 5-6
@app.route('/users', methods=['GET'])
def get_users():
    size = request.args.get('size')
    if size is None:
        users = User.query.all()
    else:
        try:
            size = int(size)
            users = User.query.limit(size).all()
        except ValueError:
            abort(400, 'Invalid size parameter. Size must be an integer.')

    return jsonify([user.serialize() for user in users]), 200


@app.route('/books', methods=['GET'])
def get_books():
    size = request.args.get('size')
    if size is None:
        books = Book.query.all()
    else:
        try:
            size = int(size)
            books = Book.query.limit(size).all()
        except ValueError:
            abort(400, 'Invalid size parameter. Size must be an integer.')

    return jsonify([book.serialize() for book in books]), 200


@app.route('/purchases', methods=['GET'])
def get_purchases():
    size = request.args.get('size')
    if size is None:
        purchases = Purchase.query.all()
    else:
        try:
            size = int(size)
            purchases = Purchase.query.limit(size).all()
        except ValueError:
            abort(400, 'Invalid size parameter. Size must be an integer.')

    # Для кожної покупки отримуємо пов'язані з нею дані про користувача та книжку
    purchases_data = []
    for purchase in purchases:
        purchase_data = {
            'purchase_id': purchase.id,
            'purchase_date': purchase.purchase_date,
            'book_title': purchase.book.title,
            'user_name': purchase.user.name,
        }
        purchases_data.append(purchase_data)

    return jsonify(purchases_data), 200


# Exercise 8
@app.route('/users', methods=['POST'])
def create_user():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        if name is None or email is None:
            abort(400)  # Bad request
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!', 'user_id': user.id}), 201


@app.route('/books', methods=['POST'])
def create_book():
    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        price = data.get('price')
        if title is None or author is None or price is None:
            abort(400)  # Bad request
        book = Book(title=title, author=author, price=price)
        db.session.add(book)
        db.session.commit()
        return jsonify({'message': 'Book created successfully!', 'book_id': book.id}), 201


@app.route('/purchases', methods=['POST'])
def create_purchase():
    if request.method == 'POST':
        data = request.get_json()
        user_id = data.get('user_id')
        book_id = data.get('book_id')
        if user_id is None or book_id is None:
            abort(400)  # Bad request

        # Check if the User and Book exist in the database
        user = User.query.get(user_id)
        book = Book.query.get(book_id)
        if user is None or book is None:
            abort(404)  # Not found

        # Set purchase_date to the current date and time
        purchase_date = datetime.utcnow()

        purchase = Purchase(user_id=user_id, book_id=book_id, purchase_date=purchase_date)
        db.session.add(purchase)
        db.session.commit()
        return jsonify({'message': 'Purchase created successfully!', 'purchase_id': purchase.id}), 201


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host=HOST, port=PORT)
