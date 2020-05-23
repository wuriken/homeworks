from django import forms

from groups.models import Group


class GroupCreateForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = (
            'group_name',
            'faculty',
            'university_name',
            'curator',
            'headman',
        )
