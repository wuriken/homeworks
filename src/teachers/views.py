from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from teachers.models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all()
    params = ['first_name', 'last_name', 'age', 'education', 'age__gt', 'age__lt']   # noqa
    for param in params:
        value = request.GET.get(param)
        if value:
            teachers = teachers.filter(**{param: value})
    return HttpResponse(teachers)


def create_teacher(request):
    from teachers.forms import TeacherCreateForm
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TeacherCreateForm()

    context = {'create_form': form}

    return render(request, 'create.html', context=context)
