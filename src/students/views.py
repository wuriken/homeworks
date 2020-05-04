from django.http import HttpResponse

from students_tracker.helper import check_param_value_is_valid, create_student


def generate_student(request):
    student = create_student()
    return HttpResponse(student)


def generate_students(request):
    count = 10
    result = []
    if request.GET.get('count'):
        if check_param_value_is_valid(request.GET.get('count')):
            count = request.GET.get('count')
        result = [str(create_student()) + '\n' for _ in range(int(count))]
    return HttpResponse(result)
