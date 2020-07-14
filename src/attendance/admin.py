from django.contrib import admin
from .models import Attendance

# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['date',
                    ]
    list_filter = ['date',
                    ]
    search_fields = [
        'date',
    ]


admin.site.register(Attendance,AttendanceAdmin)
