from django.shortcuts import render

def reverse(request):
	return render(request, 'reverse.html')