from django.urls import path, include

from django_rest_demos.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    )
