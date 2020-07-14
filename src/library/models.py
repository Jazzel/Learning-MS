from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    
    def __str__(self):
        return self.name


# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = ("Resource")
        verbose_name_plural = ("Resources")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
        # return reverse("Resource_detail", kwargs={"pk": self.pk})
