from django.shortcuts import render, redirect
from .models import Account

# Create your views here.
def index(request):
    a = Account.objects.all()
    context = {"accounts":a}
    return render(request, template_name="app1/index.html", context=context)

def register(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("emailaddress")
        a = Account(name=name,email=email)
        a.save()
        return redirect('/')
    else:
        return render(request, template_name="app1/registration.html")
    
def delete(request, id):
    a = Account.objects.filter(id=id)
    a.delete()
    return redirect('/')