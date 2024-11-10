from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def shop(request):
    return render(request, 'shop.html')
def resume(request):
    return render(request, 'resume.html')
def services(request):
    return render(request, 'services.html')
def portfoliodetails(request):
    return render(request, 'portfoliodetails.html')
def servicedetails(request):
    return render(request, 'servicedetails.html')