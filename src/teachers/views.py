from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from teachers.models import Teacher


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers-list.html', context={'teachers': teachers})


def create_teacher(request):
    from teachers.forms import TeacherCreateForm
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    else:
        form = TeacherCreateForm()

    context = {'create_form':form}

    return render(request, 'create.html', context=context)


def edit_teacher(request, pk):
    from teachers.forms import TeacherCreateForm
    student = get_object_or_404(Teacher, id=pk)
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    else:
        form = TeacherCreateForm(instance=student)

    context = {'form':form}

    return render(request, 'edit.html', context=context)

def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    teacher.delete()
    return HttpResponseRedirect(reverse('teachers:list'))
