from flask import Flask, request
import os
from helper import *

app = Flask(__name__)



@app.route('/requirements', methods = ['GET'])
def get_requirements():
    if check_file_is_exist('requirements.txt'):
        return get_file_content('requirements.txt')
    else:
        return 'File not found!!!'

@app.route('/space', methods = ['GET'])
def get_astros():
    return get_astros_count()

@app.route('/generate-users', methods = ['GET'])
def get_fake_users():
    if 'count' in request.args:
        count = request.args['count']
        if check_param_value_is_valid(count):
            return get_fake_users_mails(int(count))
        else:
            return 'Param count not valid - {}'.format(count)
    else:
        return 'Param [count] is missing'

@app.route('/mean', methods = ['GET'])
def get_mean():
    if check_file_is_exist('hw.csv'):
        return get_avg_weight_height('hw.csv')
    return 'File not found!!!'


if __name__ == '__main__':
    app.run(port=5001)
