"""
For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/views/
"""
from django.shortcuts import  render


def hello_page(request):
    return render(request, 'helloworld/helloworld.html')
