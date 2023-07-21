from django.http import HttpResponse
from django.shortcuts import render
from . models import destiny
from . models import team

# Create your views here.
def demo(request):
    obj=destiny.objects.all()
    ob1=team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':ob1})

#def addition(request):
#    x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
 #   r1=x+y
  #  r2=x-y
   # r3=x*y
 #   r4=x/y
  #  return render(request,"result.html",{'result1':r1,'result2':r2,'result3':r3,'result4':r4})
