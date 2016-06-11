from django import forms


class RequestTokenEmailForm(forms.Form):
	"""
	Holds fields for API token request form.

	Attributes:
		email (object): Email of user who requested an API token

	"""

	email = forms.EmailField(label = 'email')

class ContactUsForm(forms.Form):
	"""
	Holds fields for contact us form.

	Attributes:
		name (object): Name of user submitting form
		email (object): Email of user submitting form
		message (object): Message of user submitting form

	"""

	name = forms.CharField(label = 'name')
	email = forms.EmailField(label = 'email')
	message = forms.CharField(label = 'message')
