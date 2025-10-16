from django.shortcuts import render
from login_page.models import Loginmodel

# Create your views here.
from django.views.generic import View
class CreateLoginview(View):
    def get(self,request): 
        return render(request,"login_user.html")
    
    def post(self,request):
        print(request.POST)
        Loginmodel.objects.create(name =request.POST.get("username"),
                                  email =request.POST.get("useremail"),
                                  password =request.POST.get("userpassword"))
        
        return render(request,"login_user.html")
