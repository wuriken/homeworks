import os
import requests
from faker import Faker
from csv import DictReader, reader

def get_file_content(file_name: str) -> str:
    with open (os.path.join(os.getcwd(), file_name), 'r') as file:
        result = file.read()
    return result

def check_file_is_exist(file_name: str) -> bool:
    return os.path.exists(os.path.join(os.getcwd(), file_name))

def get_astros_count() -> {}:
    resp = requests.get('http://api.open-notify.org/astros.json')
    if resp.status_code == 200:
        if resp.json().get('number'):
            return {'Count' : resp.json()['number']}
    return {'Count':'-1'}

def get_fake_users_mails(count: int) -> str:
    result = []
    faker = Faker()
    for _ in range(count):
        result.append('{} {}'.format(faker.name().split(' ')[-2], faker.email()))
    return str(result)

def check_param_value_is_valid(param: str) -> bool:
    if param:
        if param.isdigit():
            if int(param) < 101 and int(param) > 0:
                return True
    return False

def get_avg_weight_height(file_name: str) -> {}:
    height_array = []
    weight_array = []
    result = {}
    with open(os.path.join(os.getcwd(), file_name), "r") as file:
        rows = reader(file)
        next(rows)
        for item in rows:
            if len(item) == 3:
                height_array.append(get_float_value(item[1]))
                weight_array.append(get_float_value(item[2]))
    result.update({'weight_avg': get_avg_from_array(weight_array, 0.45)})
    result.update({'height_avg': get_avg_from_array(height_array, 2.54)})
    return result

def get_float_value(input_str: str) -> float:
    try:
        result = float(input_str.strip())
        return result
    except ValueError:
        return 0

def get_avg_from_array(array: list, coefficient: float) -> float:
    return round(sum(array)/len(array) * coefficient, 2)