from django.shortcuts import render
from .models import JokeType

# Create your views here.
def index(request):
    """The home page for Joketime"""
    return render(request,'jokes/index.html')

def joketypes(request):
    """show all joketypes"""
    joketypelist=JokeType.objects
    context={'joketypes':joketypelist}
    return render(request,'jokes/joketypes.html',context)

def joketype(request,joketype_id):
    """How a single joke type and its jokes"""
    myjoketype=JokeType.objects.get(id=joketype_id)
    myjokes=myjoketype.jokes_set
    context={'joketype':myjoketype,'jokes':myjokes}
    return render(request,'jokes/joketype.html',context)   