from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView)
from django.contrib.auth import get_user_model
from accounts.models import Profile
User = get_user_model()

# Create your views here.
class HomeView(TemplateView):
    template_name = "teachers/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['head'] = 'Instructor'
        return context

class StudentsView(ListView):
    model = Profile
    template_name='teachers/students.html'

    def get_queryset(self):
        queryset = Profile.objects.filter(role__iexact="S")
        return queryset

class StudentsDetailView(DetailView):
    model = Profile
    template_name='teachers/students_details.html'
