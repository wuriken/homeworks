from django.contrib import admin

from groups.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'group_name', 'faculty', 'university_name', 'headman', 'curator')
    readonly_fields = ('university_name', )
    list_select_related = ('curator', 'headman')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('curator', 'headman')


admin.site.register(Group, GroupAdmin)
