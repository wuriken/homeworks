from django.db import models


class Group(models.Model):

    group_name = models.CharField(max_length=64)
    faculty = models.CharField(max_length=64)
    university_name = models.CharField(max_length=64)
    curator = models.ForeignKey('teachers.Teacher',
                                on_delete=models.SET_NULL, null=True)
    headman = models.ForeignKey('students.Student',
                                on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'GroupName: {}. Faculty: {}. University: {}. Curator: {}. Headman: {}'.\
            format(self.group_name, self.faculty, self.university_name, self.curator.full_name, self.headman.full_name)
