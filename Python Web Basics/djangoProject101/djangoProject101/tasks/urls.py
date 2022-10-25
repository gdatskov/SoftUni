from django.urls import path

from djangoProject101.tasks.views import show_bare_minimum_view, get_all_tasks, index1, index2

urlpatterns = [
    path('', index2),
    path('index1/', index1),
    path('not404/', show_bare_minimum_view),
    path('all/', get_all_tasks)
]