from django.contrib import admin
from .models import Class, Subject
# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'course'
                    ]
    list_filter = ['course__name',
                    ]
    search_fields = [
        'name',
    ]

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'classes'
                    ]
    list_filter = ['classes__name',
                    ]
    search_fields = [
        'name',
    ]


admin.site.register(Class,ClassAdmin)
admin.site.register(Subject,SubjectAdmin)