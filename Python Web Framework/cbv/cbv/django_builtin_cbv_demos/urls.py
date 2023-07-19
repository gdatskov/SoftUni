from django.urls import path
import django.views.generic as generics

from cbv.django_builtin_cbv_demos.views import BuiltinView, BuiltinTemplateView, BuiltinListView, BuiltinDetailsView, \
    BuiltinCreateView, BuiltinUpdateView

urlpatterns = [
    path('', BuiltinView.as_view()),
    path('template_view/', BuiltinTemplateView.as_view()),
    path('redirect', generics.RedirectView.as_view(url='/basic_cbvs/1')),
    path('list_view', BuiltinListView.as_view()),
    path('details_view/<int:pk>', BuiltinDetailsView.as_view(), name='details employee'),
    path('create_employee', BuiltinCreateView.as_view(), name='create employee'),
    path('edit_employee/<int:pk>', BuiltinUpdateView.as_view(), name='edit employee'),

]