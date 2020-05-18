from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from students.forms import ContactUs
from students.models import Student
from students.tasks import send_mail_async

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


def students(request):
    students = Student.objects.all()
    return render(request, 'students-list.html', context={'students': students})


def create_student(request):
    from students.forms import StudentCreateForm
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    else:
        form = StudentCreateForm()

    context = {'create_form': form}

    return render(request, 'create.html', context=context)


def edit_student(request, pk):
    from students.forms import StudentCreateForm
    student = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        form = StudentCreateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    else:
        form = StudentCreateForm(instance=student)

    context = {'form': form}

    return render(request, 'edit.html', context=context)


def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return HttpResponseRedirect(reverse('students:list'))


def contact_us(request):
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            result = {}
            result.update({'title': cleaned_data.get('title')})
            result.update({'message': cleaned_data.get('message')})
            result.update({'email_from': cleaned_data.get('email_from')})
            send_mail_async.apply_async(args=[result])
        return HttpResponseRedirect(reverse('index'))
    form = ContactUs()
    context = {'form': form}
    return render(request, 'contact-us.html', context=context)
