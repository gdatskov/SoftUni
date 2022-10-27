from random import choice

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Regular views
def show_departments_without_render(request: HttpRequest, *args, **kwargs):
    # print(f'args = {args}')
    # print(f'kwargs = {kwargs}')

    print(request.method)
    print(request.GET)  # query params
    print(request.POST)  # body of HTTP request
    print(request.get_host())
    print(request.get_port())

    order_by = request.GET.get('order by', 'name')
    body = f'path: {request.path} args = {args}, kwargs = {kwargs}, order by: {order_by}'
    return HttpResponse(body)


def show_departments_with_render(request: HttpRequest, *args, **kwargs):
    context = {
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name')
    }

    return render(request, 'departments/all.html', context)


def show_department_details(request, department_id):
    # print(f'args = {args}')
    # print(f'kwargs = {kwargs}')
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)


def show_department_details_by_id(request, department_id):
    department_name = None
    if department_id == 1:
        department_name = "Devs"
    elif department_id == 2:
        department_name = "Trainers"
    html = f''' <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Department {department_name}</title>
                </head>
                <body>
                <h1>
                    Department name: {department_name}, Department ID: {department_id}
                </h1>
                </body>
                </html>
            '''
    return HttpResponse(html)


# Redirections
def redirect_to_first_dept(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    return redirect(f'/departments/rendered/?order_by={order_by}')


def redirect_to_softuni(request):
    to = 'https://softuni.bg'
    return redirect(to)


def redirect_to_named_url(request):
    return redirect('show depts with render')


def redirect_to_named_url_with_params(request):
    return redirect('show dept details', department_id=2)


# Errors
def view_not_find(request):
    return HttpResponseNotFound('Page view not found!!!11edno')


def view_return_error(request):
    status_code = 404   # get value from somewhere...
    return HttpResponse(f'Error {status_code}', status=status_code)


def raise_http_error(request):
    raise Http404('Not found')

# Debug = False
# def raise_http_error_customized_http(request):
#     raise Http404('Not found')
