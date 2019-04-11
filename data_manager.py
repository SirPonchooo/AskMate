import connection
import csv


def get_all_answers():
    a_list = connection.import_data('answers.csv')
    return a_list


def get_questions():
    questions = connection.import_data('question.csv')
    return questions
