from flask import Flask, render_template, redirect, request

import data_manager

app = Flask(__name__)


list_of_roccs = ["big rock", "shmaller roczkk"]

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/add-question', methods=['GET', 'POST'])
def display_add_question():
    return render_template('add-question.html')


@app.route('/list', methods=['GET', 'POST'])
def display_list_of_questions():
    list_of_questions = data_manager.get_questions()
    return render_template('list.html', questions=list_of_questions)


if __name__ == '__main__':
    app.run(debug=True)
