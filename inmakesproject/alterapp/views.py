from django.http import HttpResponse
from django.shortcuts import render
from . models import dtable, datatable
# Create your views here.
def demo(request):
    obj=dtable.objects.all()
    orc=datatable.objects.all()
    return render(request,'index.html',{'result':obj,'rest':orc})