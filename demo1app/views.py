from django.http import HttpResponse
from django.shortcuts import render
from .models import place,person
# Create your views here.
# def home(request):
#     return render(request,"home.html")
# def about(request):
#     return HttpResponse("this is 'about'")
# def contact(request):
#     return render(request,"contact.html")
# def detail(request):
#     return HttpResponse("hey...this is detail")
# def thanks(request):
#     return HttpResponse("THANKUUUU...")
# def new(request):
#     name='abhijith'
#     return render(request,'new.html',{'obj':name})
def new(request):
     prsn=person.objects.all()
     obj=place.objects.all()
     return render(request,'index.html',{'result':obj,'result1':prsn})
# def result(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,'result.html',{'sum':add,'difference':sub,'product':mul,'division':div,'num1':x,'num2':y})