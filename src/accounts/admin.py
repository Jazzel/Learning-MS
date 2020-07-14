from django.contrib import admin
from . models import Profile, UserLog
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'role'
                    ]
    list_filter = ['role',
                    ]
    search_fields = [
        'user',
    ]

admin.site.site_header = ""
admin.site.register(Profile, UserAdmin)
admin.site.register(UserLog)
