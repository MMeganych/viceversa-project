from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	len_result = len(user_text.split())
	len_original_text = 'has ' + str(len_result) + ' words'
	return render(request, 'reverse.html', {'usertext':user_text,
		'reversedtext':reversed_text,'lentext':len_original_text})

