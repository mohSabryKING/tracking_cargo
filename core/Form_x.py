from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import *
from .models import *

class Add_user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2',)


class Make_profile_form(forms.ModelForm):
    class Meta:
        model = User_profile_Model
        fields = ('user_img','user_email')
        widget={
            'user_x':forms.HiddenInput(),
        }



class Voyage_form(forms.ModelForm):
    class Meta:
        model = Voyage_tracking_info
        fields = ('ship_name','from_time','to_time','info')
        widget={
            'posted_by':forms.HiddenInput(),
            'from_country_x':forms.ChoiceField(),
            'to_country_y':forms.ChoiceField(),
        }


class Cargo_form(forms.ModelForm):
    class Meta:
        model = Cargo_info
        fields = ('cargo_title','info')
        widget={
             'part_of':forms.HiddenInput(),
        }