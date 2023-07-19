from django.urls import path

from cbv.basic_demos.views import DemoIndexView, Demo2IndexView

urlpatterns = [
    path('1', DemoIndexView.get_view()),
    path('2', Demo2IndexView.get_view()),
]
