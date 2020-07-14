from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Attendance(models.Model):
    person = models.ManyToManyField(settings.AUTH_USER_MODEL)
    date = models.DateField()
    

    class Meta:
        verbose_name = ("Attendance")
        verbose_name_plural = ("Attendances")

    def __str__(self):
        return str(self.date)

    # def get_absolute_url(self):
        # return reverse("Attendance_detail", kwargs={"pk": self.pk})
