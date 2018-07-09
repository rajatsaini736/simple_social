from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.genetic import CreateView
# Create your views here.
class SignUp(CreateView):
	form_class = form.UserCreateForm
	success_url = reverse_lazy('Login')
	template_name = 'accounts/signup.html'

