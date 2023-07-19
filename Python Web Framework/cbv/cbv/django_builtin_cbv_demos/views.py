import django.views.generic as generics
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from cbv.django_builtin_cbv_demos.models import Employee
import inspect


class BuiltinView(generics.View):
    # Define a http method to be checked and executed
    def get(self, request):
        return HttpResponse("Automatically generated generic GET view from Django's builtin CBVs")

    # Define a http method to be checked and executed (In standard Django there are only GET and POST)
    def post(self, request):
        pass

    # Django REST framework has all other methods like:
    # def put(self, request)
    #   pass


class BuiltinTemplateView(generics.TemplateView):
    template_name = "basic_template.html"
    extra_context = {
        "title": "Generic Template View"  # Static context
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()  # Dynamic context
        # context['employees'] = self.get_queryset()  # Dynamic context

        return context


class BuiltinListView(generics.ListView):
    model = Employee
    context_object_name = 'employees'   # 'object_list' by default
    template_name = 'basic_template.html'
    extra_context = {
        "title": "Generic List View"  # Static context
    }

    # Some more stuff:
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('first_name')


class BuiltinDetailsView(generics.DetailView):
    model = Employee
    # context_object_name = 'employees'  # 'object' by default
    template_name = 'details_template.html'
    extra_context = {
        "title": f"Generic Details View"  # Static context
    }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name'
                }
            )
        }


class BuiltinCreateView(generics.CreateView):
    # This example works similarly for generics.UpdateView and generics.DeleteView
    model = Employee
    template_name = 'create_employee_template.html'
    fields = '__all__'

    # Static success url
    success_url = '/builtin_cbvs/list_view'   # in this example - current app list directory

    # Dynamic success url
    def get_success_url(self):
        return reverse('details employee', kwargs={
            'pk': self.object.pk
        })

    # # Replacing form with custom form class
    # form_class = EmployeeForm

    # Edit generic form
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        print(form.fields)
        for name, field in form.fields.items():
            field.widget.attrs['placeholder'] = 'enter ' + ' '.join(name.split('_'))

        return form

    # NOTE:
    # CRUD views must have redirect implementation either:
    # a) define absolute url in the model
    # b) add success_url for the CRUD view
    # But not BOTH!

class BuiltinUpdateView(generics.UpdateView):
    model = Employee
    template_name = 'edit_employee_template.html'
    fields = '__all__'

    def get_success_url(self):
        # return reverse('details employee', kwargs={
        #     'pk': self.object.pk
        # })

        # both reverse and reverse_lazy work, but when using lazy we can avoid errors in listView
        # or other similar scenarios
        return reverse_lazy('details employee', kwargs={
            'pk': self.object.pk
        })
