from django.contrib import admin
from .models import Category, Resource

# Register your models here.
class ResourseAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'category',
                    ]
    list_filter = ['title',
                    'category__name',
                    ]
    search_fields = [
        'title',
    ]

class CategoryAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]


admin.site.register(Category,CategoryAdmin)
admin.site.register(Resource,ResourseAdmin)