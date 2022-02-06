from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'boldmessage':'Crunchy, creamy,cookie,candy,cupcake'}
    return render(request, 'rango/index.html',context=context_dict)
    # return HttpResponse("Rango says here is the about page!")

def about(request):
    # return HttpResponse("Rango says here is the about page.")
    context_dict = {'boldmessage':'This tutorial has been put together by Jing Xue'}
    return render(request, 'rango/about.html',context=context_dict)