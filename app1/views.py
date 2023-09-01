from django.shortcuts import render
from django.http import HttpResponse

def vista1(request):
    return HttpResponse("""
                        <h3>Hola</h3>
                        <h1>Mundo</h1>
                        """)
