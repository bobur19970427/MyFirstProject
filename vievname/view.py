from django.shortcuts import render

def reverse(request):
	return render(request, 'reverse.html')

def reversed(request):
	user_text = request.GET['usertext']
	rever_text = user_text[::-1]
	return render(request, 'reversed.html', {'usertext': user_text, 'revertext':rever_text})