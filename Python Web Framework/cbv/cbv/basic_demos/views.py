import random

from django.http import HttpResponse
from django.shortcuts import render


# Demo of a very basic(primitive) CBV
class DemoIndexView:
    def __init__(self):
        self.value = [
            random.randint(1, 10)
        ]

    @classmethod
    def get_view(cls):
        return cls().view

    def view(self, request):
        return HttpResponse(
            f"This is a cbv demo index view and a random value created at initializing the view instance: {self.value}"
        )


class Demo2IndexView(DemoIndexView):
    def __init__(self):
        super().__init__()
        self.value.append(
            random.randint(11, 20)
        )
    