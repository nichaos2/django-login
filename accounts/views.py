from django.shortcuts import render
from django.http import HttpResponseRedirect
from config.settings import MEDIA_ROOT, MEDIA_URL

from .models import Profile
from .forms import UserCreateForm


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class =  UserCreateForm  #UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
          form = self.form_class(request.POST, request.FILES)
          if form.is_valid():
              print('valid form')
              form.save()
              return HttpResponseRedirect('/')
          return HttpResponseRedirect('/')