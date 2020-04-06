# http://jessenoller.com/blog/2011/12/19/quick-example-of-extending-usercreationform-in-django
# modified from the above page
from django import forms
from .models import Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    email = forms.EmailField(required = True )
    location = forms.CharField(required = True)
    avatar = forms.ImageField(required = False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "location", "avatar") #

    def save(self, commit=True):
        user1 = super(UserCreateForm, self).save(commit=False)
       
        #TODO cleaned_data -> is it necessary?
        user1.email = self.cleaned_data["email"]
        user1.first_name = self.cleaned_data["first_name"]
        user1.last_name = self.cleaned_data["last_name"]
        user1.email = self.cleaned_data["email"]
        location1 = self.cleaned_data["location"]
        avatar1 = self.cleaned_data["avatar"]

        # For this to work I had to take of the post_save in the model Profile
        if commit:
            user1.save()
            profile = Profile(user = user1, location = location1, avatar = avatar1)
            profile.save()
        return user1