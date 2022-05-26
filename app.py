from flask import Flask, request
from functions import processing_likes

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! <br/>' \
           'send POST request like --> http://127.0.0.1:8000/likes?names=Андрей,Жанна,Коля'


@app.route('/likes')
def view_likes():
    try:
        names = request.args.get('names')  # getting entered names in url address
        list_name = list(names.split(','))  # making from string list
        if list_name[0] == "":
            list_name = []
        answer, error = processing_likes(list_name)
        if error:
            return "{ <br/>" \
                   f'&emsp;"error": {error}<br/>' \
                   f'&emsp;"data": None<br/>' \
                   f'&emsp;"error_message": {answer}<br/>' \
                   "}"
        return "{ <br/>" \
               f'&emsp;"error": {error}<br/>' \
               f'&emsp;"data": {answer}<br/>' \
               f'&emsp;"error_message": None<br/>' \
               "}"
    except TypeError:
        return f"Упс, что-то пошло не так"


if __name__ == '__main__':
    app.run()
