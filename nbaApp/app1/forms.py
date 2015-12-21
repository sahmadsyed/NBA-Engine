from django import forms

class RequestTokenEmailForm(forms.Form):
	email = forms.EmailField(label = 'email')

class ContactUsForm(forms.Form):
	name = forms.CharField(label = 'name')
	email = forms.EmailField(label = 'email')
	message = forms.CharField(label = 'message')
