from django import forms

class OrderForm(forms.Form):
    # widget=forms.TextInput(attrs={'class': 'css_input'}) Добавляем css
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
