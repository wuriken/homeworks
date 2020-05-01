from django.http import HttpResponse
from students_tracker.helper import *

def generate_student(request):
    student = create_student()
    return HttpResponse(student)

def generate_students(request):
    count = 10
    result = []
    if request.GET.get('count'):
        if check_param_value_is_valid(request.GET.get('count')):
            count = request.GET.get('count')
    for _ in range(int(count)):
        result.append(str(create_student()) + '\n')
    return HttpResponse(result)