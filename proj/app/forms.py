from django import forms


class UserForm(forms.Form):
    name = forms.CharField(required=False, min_length=5, max_length=15,
                           widget=forms.TextInput(attrs={'class': "name"}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': "password"}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "email"}))
    
    required_css_class = 'myclasses'


class UserLoginForm(forms.Form):    
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "email"}))
    
    password = forms.CharField(widget=forms.TextInput(attrs={'class': "password"}))

    # required_css_class = 'myclasses'

