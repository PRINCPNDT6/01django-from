from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def Home(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')

        return render(request, 'website/profile.html', {
            'name' : Name,
            'email' : Email
        })
    return render(request, 'website/index.html')

def profile(request):
    return render(request, 'website/profile.html')

def loginpage(request):
    return render(request, 'website/loginpage.html')