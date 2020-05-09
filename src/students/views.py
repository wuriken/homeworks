from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from students_tracker.helper import check_param_value_is_valid, create_random_student


def generate_student(request):
    student = create_random_student()
    return HttpResponse(student)


def generate_students(request):
    count = 10
    result = []
    if request.GET.get('count'):
        if check_param_value_is_valid(request.GET.get('count')):
            count = request.GET.get('count')
        result = [str(create_random_student()) + '\n' for _ in range(int(count))]
    return HttpResponse(result)


def create_student(request):
    from students.forms import StudentCreateForm
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = StudentCreateForm()

    context = {'create_form': form}

    return render(request, 'create.html', context=context)
