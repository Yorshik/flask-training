from flask import Flask
from flask import url_for

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


@app.route('/promotion_image')
def promotion_image():
    return f'''
            <html>
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1"><title>Привет, Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                </head>
                <body>
                    <h1 class="top">Жди нас, Марс!</h1>
                    <img src=/static/img/MARS.png>
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                </body>
            </html>
        '''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
