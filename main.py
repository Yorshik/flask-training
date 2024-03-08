from flask import Flask
from flask import request
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


@app.route('/astronaut_selection', methods=['POST', "GET"])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1 class="mytext">Анкета претендента</h1>
                                <h2 class="mytext">на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="surname" aria-describedby="format" placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="education">
                                              <option>Начальное</option>
                                              <option>Среднее общее</option>
                                              <option>Среднее полное</option>
                                              <option>Среднее Профессиональное</option>
                                              <option>Высшее</option>
                                            </select>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-speciality">Какие у Вас есть профессии?</label>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-speciality-input" id="1" name="check1">
                                                <label class="form-speciality-label" for="1">Инженер-исследователь</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-speciality-input" id="2" name="check2">
                                                <label class="form-speciality-label" for="2">Инженер-строитель</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-speciality-input" id="3" name="check3">
                                                <label class="form-speciality-label" for="3">Пилот</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-speciality-input" id="4" name="check4">
                                                <label class="form-speciality-label" for="4">Метеоролог</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-speciality-input" id="5" name="check5">
                                                <label class="form-speciality-label" for="5">Инженер по жизнеобеспечению</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-speciality-input" id="6" name="check6">
                                                <label class="form-speciality-label" for="6">Инженер по радиационной защите</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-speciality-input" id="7" name="check7">
                                                <label class="form-speciality-label" for="7">Врач</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-speciality-input" id="8" name="check8">
                                                <label class="form-speciality-label" for="8">Экзобиолог</label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['email'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        print(
            request.form['check1'],
            request.form['check2'],
            request.form['check3'],
            request.form['check4'],
            request.form['check5'],
            request.form['check6'],
            request.form['check7'],
            request.form['check8']
        )
        print(request.form['education'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    dct = {
        'Меркурий': ['Жарковато', 'Воды нема', 'Магнитное поле в 100 раз меньше чем у Земли', "Но она красивая"],
        'Венера': ['Очень жарко', "Атмосфера непригодная", "Слабое магнитное поле", "Красота"],
        'Марс': ["Прохладно", "Есть вода и атмосфера, не очень пригодная для жизни", "Небольшое магнитное поле",
                 "И еще она очень красивая"],
        'Юпитер': ["Невероятно холодно", "Отсутствует поверхность, пройтись не получится", "Сильное магнитное поле",
                   "Красивая, но опасная"],
        'Сатурн': ["Еще холоднее", "Пройтись не получится", "Магнитное поле есть", "Красивые кольца"],
        'Уран': ["Холодон", "Пройтись не получится", "Магнитное поле есть", "Красивая синяя планета"],
    }
    return f'''
            <html>
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1"><title>Привет, Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
                    rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                </head>
                <body>
                    <h1 class="top">Мое предложение: {planet_name}</h1>
                    <div class="alert alert-dark" role="alert">
                      {dct[planet_name][0]}
                    </div>
                    <div class="alert alert-success" role="alert">
                      {dct[planet_name][1]}
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      {dct[planet_name][2]}
                    </div>
                    <div class="alert alert-warning" role="alert">
                      {dct[planet_name][3]}
                    </div>
                </body>
            </html>
    '''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''
            <html>
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1"><title>Привет, Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
                    rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                </head>
                <body>
                    <h1 class="top">Результаты отбора</h1>
                    <h2 class="top">Претендента на участие в миссии {nickname}</h2>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} отбора
                    </div>
                    <div class="alert">
                        составляет {rating}!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                </body>
            </html>
    '''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
