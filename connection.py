import csv
import os

def import_data(filename): # import csv data
    with open(filename, "r") as file:
        imported_data = csv.DictReader(file)
        data = list(imported_data)
        return data



def write_file(dict_list, filename):
    keys = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
    if filename == 'answers.csv':
        keys = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
    #file_directory = 'AskMate/sample_data/' + filename
    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, keys)
        writer.writerow(dict_list)