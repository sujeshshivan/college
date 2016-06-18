from django.shortcuts import render

def index(request):
    return render(request, 'mysite/base.html')


def contact(request):
	return render(request, 'mysite/contact.html')