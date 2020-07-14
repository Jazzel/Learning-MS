from django.contrib import admin
from .models import  Course,File

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'rating'
                    ]
    list_filter = ['rating',
                    ]
    search_fields = [
        'name',
    ]

class FileAdmin(admin.ModelAdmin):
    list_display = ['file',
                    'url',
                    ]
    list_filter = ['course',
                    ]
    search_fields = [
        'file',
        'url',
    ]

admin.site.register(Course,CourseAdmin)
admin.site.register(File,FileAdmin)
