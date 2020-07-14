from django.db import models
from courses.models import Course
from django.conf import settings

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    assigned_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL,blank=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="created_by", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Class")
        verbose_name_plural = ("Classes")

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    

    class Meta:
        verbose_name = ("Subject")
        verbose_name_plural = ("Subjects")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        # return reverse("Class_detail", kwargs={"pk": self.pk})
