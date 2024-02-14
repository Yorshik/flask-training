from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.<br>
Человечеству мала одна планета.<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
И начнем с Марса!<br>
Присоединяйся!'''


@app.route('/image_mars')
def image_mars():
    return '''
        <html>
            <head>
                <title>Привет, Марс!</title>
            </head>
            <body>
                <h1>Жди нас, Марс!</h1>
                <img src=/static/img/MARS.png>
                <p>Вот она какая, красная планета.</p>
            </body>
        </html>
    '''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
