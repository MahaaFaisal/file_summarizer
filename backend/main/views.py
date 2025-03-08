from django.shortcuts import render
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.decorators import api_view, permission_classes
from main.srcs.get_content import get_content_fun
from main.srcs.summerize_content import get_summary_fun
from django.http import JsonResponse
from django.contrib.auth.models import User


def home (request):
    return render(request, "home.html", {"user": 'Maha', "title": 'akrm'})

@api_view(['POST'])
@permission_classes([HasAPIKey])
def get_content(request):
    return get_content_fun(request)

@api_view(['POST'])
@permission_classes([HasAPIKey])
def summarize_content(request):

    try:
        return get_summary_fun(request)
    except Exception as e:
        error_message = str(e)
        return (JsonResponse({'result': error_message}))

    '''
     render: works in the view layer of the web application, combines several steps
     1. takes a request, a template, a dictionary
     2. returns HTTP request with the rendered HTML content
    '''
