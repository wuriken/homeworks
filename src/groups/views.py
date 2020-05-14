from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from groups.models import Group


def groups(request):
    teachers = Group.objects.all()
    return render(request, 'groups-list.html', context={'groups': teachers})


def create_group(request):
    from groups.forms import GroupCreateForm
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupCreateForm()

    context = {'create_form': form}

    return render(request, 'create.html', context=context)


def edit_group(request, pk):
    from groups.forms import GroupCreateForm
    group = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupCreateForm(instance=group)

    context = {'form': form}

    return render(request, 'edit.html', context=context)


def delete_group(request, pk):
    teacher = get_object_or_404(Group, id=pk)
    teacher.delete()
    return HttpResponseRedirect(reverse('groups:list'))
