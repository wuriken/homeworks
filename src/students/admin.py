from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'first_name', 'last_name', 'age')
    readonly_fields = ('age', )

    def get_queryset(self, request):
        queryset = super().get_queryset(request).filter(age__gte=18)
        if not request.user.is_superuser:
            pass
        return queryset


admin.site.register(Student, StudentAdmin)
