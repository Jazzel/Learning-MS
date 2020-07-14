from django.db import models
from django.conf import settings

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rating = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    assigned_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,related_name="added_by", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        # return reverse("Course_detail", kwargs={"pk": self.pk})

class File(models.Model):
    course = models.ManyToManyField(Course, blank=True)
    file = models.FileField(upload_to='course-files', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = ("File")
        verbose_name_plural = ("Files")

    def __str__(self):
        return self.classes.name

    # def get_absolute_url(self):
        # return reverse("Class_detail", kwargs={"pk": self.pk})