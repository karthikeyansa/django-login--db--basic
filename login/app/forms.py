from django import forms

class Sign(forms.Form):
	name = forms.CharField(max_length = 20,widget = forms.TextInput(attrs = {'class' : 'form-control','placeholder':'Name'}))
	password = forms.CharField(widget = forms.TextInput(attrs ={'class' : 'form-control','placeholder':'password'}))

class Index(forms.Form):
	name = forms.CharField(max_length = 20,
		widget = forms.TextInput(attrs = {'class' : 'form-control','placeholder':'Name'}))
	password = forms.CharField(widget = forms.TextInput(attrs ={'class' : 'form-control','placeholder':'password'}))