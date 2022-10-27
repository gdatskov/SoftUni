from django.urls import path

from templates_exercise.web.views import *

urlpatterns = [
    path('', index, name='index'),
    path('go-to-home/', redirect_home, name='redirect to home')
]