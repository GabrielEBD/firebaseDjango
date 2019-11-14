from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from .forms import Registro

import json

import pyrebase

config = {
	
	'apiKey': "AIzaSyB0gZU8KYZQNA-qZW81Uinp8JQEVG5jo-4",
    'authDomain': "monitoreo-8fa29.firebaseapp.com",
    'databaseURL': "https://monitoreo-8fa29.firebaseio.com",
    'projectId': "monitoreo-8fa29",
    'storageBucket': "monitoreo-8fa29.appspot.com",
    'messagingSenderId': "199947077699",
    'appId': "1:199947077699:web:f7c2cb124287920944acf6",
    'measurementId': "G-J2M63MZXRF"

}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def valid(data):
	if {'temperatura','humedad'} <= set(data):
		return True
	else:
		return False


@csrf_exempt
def recive(request):
	if request.method == "POST":
		body_unicode = request.body.decode('utf-8')
		data = json.loads(body_unicode)
		if valid(data):
			#save
			result = db.child('registros').push(data)
			print(result)
			return HttpResponse(status=200, content = "ok")
		else:
			return HttpResponse(status=401, content = "invalid format")	
	else:
		return HttpResponse(status=401, content = "method not supporting")


def showData(request):
	context = {}
	context['list'] = []
	registros = db.child('registros').get()
	for registro in registros.each():
		context['list'].append(registro.val())
	#print(context['list'])
	return render(request, 'show.html',context)


def postData(request):
	context = {}
	form = Registro()
	context['form'] = form 
	if request.method == 'POST':
		form = Registro(request.POST)
		if form.is_valid():
			temperatura = form.cleaned_data['temperatura']
			humedad = form.cleaned_data['humedad']
			data = {'temperatura': temperatura, 'humedad':humedad}
			#data = {}
			result = db.child('registros').push(data)
	
	
	return render(request, 'form.html',context)