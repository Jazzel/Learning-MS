from django.urls import path
from .views import HomeView

app_name = "students"
urlpatterns = [
    path('', HomeView.as_view(), name="student"),
]
