import os
import random
from csv import reader


from faker import Faker

from students.models import Student


def get_file_content(file_name: str) -> str:
    with open(os.path.join(os.getcwd(), file_name), 'r') as file:
        result = file.read()
    return result


def check_file_is_exist(file_name: str) -> bool:
    return os.path.exists(os.path.join(os.getcwd(), file_name))


def create_random_student():
    faker = Faker()
    return Student.objects.create(first_name=faker.first_name(),
                                  last_name=faker.last_name(), age=random.randint(17, 60)) # noqa


def get_fake_users_mails(count: int) -> str:
    faker = Faker()
    result = [f'{faker.name().split( )[-2]} {faker.email()}' for _ in range(count)] # noqa
    return str(result)


def check_param_value_is_valid(param: str) -> bool:
    if param and param.isdigit() and int(param) < 101 and int(param) > 0:
        return True
    else:
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
