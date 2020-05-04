from django.db import models


class Group(models.Model):

    group_name = models.CharField(max_length=64)
    faculty = models.CharField(max_length=64)
    university_name = models.CharField(max_length=64)

    def __str__(self):
        return 'GroupName: {}. Faculty: {}. University: {}'.format(self.group_name, self.faculty, self.university_name)
