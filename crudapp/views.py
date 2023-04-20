from django.shortcuts import render
from .models import GeeksModel

# Create your views here.


def create_view(request):
    context={}
    form=GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context['form']=form
    return render(request,"create_view.html",context)
        
