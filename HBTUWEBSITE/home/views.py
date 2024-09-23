from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        "variable":"this is the variable"
        
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")

def Login(request):
    return render( request, 'teamx1.html')

def services(request):
    return render( request, 'Projects.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, message=message, date= datetime.today() )
        contact.save()
        messages.success(request, "Your message has been recorded")
        
    return render( request, 'teamx2.html')

def AiProject(request):
    return render( request, "teamx3AI.html" )

def DLproject(request):
    return render( request, "teamx4DeepLearning.html")

def Webdev(request):
    return render( request, "teamx5.html")

def Login2(request):
    return render( request, "Login.html")