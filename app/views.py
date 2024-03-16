from django.shortcuts import render

from app.forms import*
from django.http import HttpResponse
from app.models import *

# Create your views here.
def create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}
    if request.method=="POST":
        SFDO=SchoolForm(request.POST)
        sn=SFDO.cleaned_data['sname']
        sp=SFDO.cleaned_data['sprincipal']
        sl=SFDO.cleaned_data['slocation']
        e=SFDO.cleaned_data['email']
        r=SFDO.cleaned_data['reenteremail']
        so = School.objects.get_or_create(sname=sn,sprincipal=sp,slocation=sl,email=e,reenteremail=r)[0]
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('not valid')





    return render(request,'create_school.html',d)

