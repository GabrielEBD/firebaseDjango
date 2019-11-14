from django import forms

class Registro(forms.Form):
	temperatura = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class': 'temperatura', 'placeholder': 'temperatura'})) 
	humedad 	= forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class': 'humedad', 'placeholder': 'humedad'}))
