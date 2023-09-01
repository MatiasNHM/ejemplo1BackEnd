from django.shortcuts import render
from django.http import HttpResponse

def vista2(request):
    a="""
<h1>hola2 </h1>  
"""
    return HttpResponse(a)
