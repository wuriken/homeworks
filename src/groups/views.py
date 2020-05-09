from django.http import HttpResponseRedirect
from django.shortcuts import render


def create_group(request):
    from groups.forms import GroupCreateForm
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = GroupCreateForm()

    context = {'create_form': form}

    return render(request, 'create.html', context=context)
