import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/hello')
def hello():
    logger.info('This is an INFO log message')
    return 'Hello, world!'


@app.route('/html')
def return_html():
    logger.info('This is an INFO log message')
    return '<h1>This is an HTML response</h1>'


@app.route('/json')
def return_json():
    logger.info('This is an INFO log message')
    return {'message': 'This is a JSON response'}


if __name__ == '__main__':
    app.run()
