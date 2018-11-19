"""
For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/views/
"""
from django.http import HttpResponse


def hello_page(request):
    html = "<html><body>Hello World!</body></html>"
    return HttpResponse(html)
