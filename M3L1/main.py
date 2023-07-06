import random
from flask import Flask

app = Flask(__name__)

facts_list = [
    'Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
    'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.',
    'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.'
]

moneta_throw = [
    'Орёл',
    'Решка',
]

@app.route("/")
def index():
    return '<h1>Привет ты попал на сайт с рандомными фактами</h1>    <a href="/random_fact">Посмотреть случайный факт!</a>    <a href="/moneta_throw">Подбросить монетку!</a>'



@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/moneta_throw")
def moneta():
    return f'<p>{random.choice(moneta_throw)}</p>'



app.run(debug=True)

