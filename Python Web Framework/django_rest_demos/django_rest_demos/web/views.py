from django.shortcuts import render
from django.views import generic as django_views


class IndexView(django_views.TemplateView):
    template_name = 'index.html'

