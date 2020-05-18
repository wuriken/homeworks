from django import forms
from django.core.exceptions import ValidationError

from students.models import Student


class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
            'phone',
        )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not str(phone).isdigit():
            raise ValidationError(message='Field phone not a digit!')
        else:
            return phone
