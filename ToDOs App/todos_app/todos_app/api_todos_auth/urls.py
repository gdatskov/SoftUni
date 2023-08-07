from django.urls import path

from todos_app.api_todos_auth.views import RegisterAPIView, LogoutAPIView, LoginAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register api user view'),
    path('login/', LoginAPIView.as_view(), name='login api user view'),
    path('logout/', LogoutAPIView.as_view(), name='logout api user view'),
]
