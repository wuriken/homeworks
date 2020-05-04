from django.db import models


class Teacher(models.Model):

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    education = models.CharField(max_length=64)

    def __str__(self):
        return 'FirstName: {}. LastName: {}. Age: {}. Education: {}'.\
            format(self.first_name, self.last_name, self.age, self.education)
