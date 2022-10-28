import random
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name: {self.name}, Age: {self.age}'


def index(request):
    context = {
        'title': 'DTL exercise homepage',
        'value': random.random(),
        # 'my value': random.random(),   # space is invalid context variable character
        # 'my.value': random.random(),   # punctuation is invalid context variable character
        # '42': random.random(),         # numbers are invalid context variable character
        # '_value': random.random(),    # context variable starting with underscore is invalid

        'info': {
            'adress': 'Sofia'
        },

        'student': Student('Gosho', 34),
        'student_info': Student('Gosho', 34).get_info(),

        'students': [
            'Pesho',
            'Pesho',
            'Gosho',
            'Gosho',
            'Gosho',
            'Gosho',
            'Gosho',
            'Maria',
            'Stamat',
        ],

        'now': datetime.now(),

        'students_empty': [],

        'values': list(range(20)),

    }

    return render(request, 'index.html', context)


def redirect_home(request):
    return redirect('index')


def about(request):
    return render(request, 'about.html')
