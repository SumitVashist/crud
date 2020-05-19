from django import forms
from django.core import validators


def named(value):
    if len(value)<4:
        raise forms.ValidationError('the length of name field shoould be greater than 4')
        #return in



class FeedbackForm(forms.Form):
    name=forms.CharField(validators=[named])
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea ,validators=[validators.MaxLengthValidator(40)])
