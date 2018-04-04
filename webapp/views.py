from django.http import HttpResponse

def index(request):
	return HttpResponse("Yes the project is named after Boondock Saints. You're lucky I didn't name it Will Hunting")