from django.contrib import admin

from groups.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'group_name', 'faculty', 'university_name')
    readonly_fields = ('university_name', )

admin.site.register(Group, GroupAdmin)