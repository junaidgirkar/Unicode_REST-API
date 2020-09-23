from django.shortcuts import render

# Create your views here.
def welcomePage(request):
    return render(request, 'welcome.html')