from django.http import HttpResponse

from teachers.models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all()
    params = ['first_name', 'last_name', 'age', 'education', 'age__gt', 'age__lt']   # noqa
    for param in params:
        value = request.GET.get(param)
        if value:
            teachers = teachers.filter(**{param: value})
    return HttpResponse(teachers)
