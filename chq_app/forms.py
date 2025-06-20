from django.forms import ModelForm, Textarea
from django import forms
from .models import master, order, replacement, new_order, boat_ticket



class chq_form(ModelForm):
    
    class Meta:
        model = master
        fields = '__all__'


class order_form(ModelForm):
    class Meta:
        model=order
        fields = '__all__'
       

class replace_form(ModelForm):
    item= forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 9}))

    class Meta:
        model=replacement
        fields = '__all__'

class new_order_form(ModelForm):
    order_details= forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 9}))
    
    class Meta:
        model=new_order
        fields = '__all__'


class boat_ticket_form(ModelForm):
    full_address= forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 3}))

    class Meta:
        model=boat_ticket
        fields = '__all__'
        