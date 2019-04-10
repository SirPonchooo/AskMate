from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/add-question', methods=['GET', 'POST'])
def display_add_question():
    return render_template('add-question.html')



if __name__ == '__main__':
    server.run()
