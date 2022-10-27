from django.urls import path
from django.shortcuts import render, redirect

from departments_app.departments.views import *

urlpatterns = [
    # named urls
    path("redirect1/", redirect_to_named_url),
    path("rendered/", show_departments_with_render, name='show depts with render'),

    path("redirect2/", redirect_to_named_url_with_params),
    path("<int:department_id>/details", show_department_details, name='show dept details'),

    # Errors
    path("not-found/", view_not_find, name='view not found'),
    path("error/", view_return_error, name='error view'),
    path("http-error/", raise_http_error, name='http error'),
    # path("http-error-custom-http/", raise_http_error_customized_http, name='http error customized'),


    # unnamed urls
    path("", show_departments_without_render),
    # path("redirect/", redirect_to_first_dept),
    path("redirect/to_softuni", redirect_to_softuni),
    path("rendered/", show_departments_with_render),
    path("<department_id>/", show_departments_without_render),
    path("int/<int:department_id>/", show_departments_without_render),
    path("<int:department_id>/details", show_department_details),
    # re_path("REGEX_PATH/", some_view), # Using RegEx is possible to limit user path to view with arguments
    path("<int:department_id>/details/byid", show_department_details_by_id),


]
