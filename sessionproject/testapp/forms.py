from django.forms import form

class AddItemForm(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()
    
