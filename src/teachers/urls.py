from django.urls import path
from .views import HomeView, StudentsView, StudentsDetailView

app_name = "teachers"

urlpatterns = [
    path('', HomeView.as_view(), name="instructor"),
    path('students/', StudentsView.as_view(), name="students"),
    path('students/details/<int:pk>/', StudentsDetailView.as_view(), name='student_details'),
]
