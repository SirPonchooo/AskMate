from flask import Flask, render_template, request, redirect
import connection
import csv
import data_manager

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/add-question', methods=['GET'])
def display_add_question():
    return render_template('add-question.html')


@app.route('/add-question', methods=['POST'])
def add_question():
    if request.method == 'POST':
        saved_data = {'id': "xxx",
                      "submission_time": "xxx",
                      "view_number": "xxx",
                      "vote_number": "xxx",
                      'title': request.form['title'],
                      'message': request.form['message'],
                      "image": "xxx"
                      }
        connection.write_file(saved_data, "question.csv")
        return redirect('/')
    return render_template('add-question.html')


@app.route('/list', methods=['GET', 'POST'])
def display_list_of_questions():
    list_of_questions = data_manager.get_questions()
    return render_template('list.html', questions=list_of_questions)



if __name__ == '__main__':
    app.run(debug=True)
