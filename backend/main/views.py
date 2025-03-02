from django.shortcuts import render
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.decorators import api_view, permission_classes
from main.srcs.get_content import get_content_fun
from main.srcs.summerize_content import get_summary_fun
import json
from django.http import JsonResponse

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
        content_json = get_content_fun(request)
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        content = json.loads(content_json.content)  # Parse JSON string to dict
        # content_dict = content_json.json()
        return get_summary_fun(content['result'], age, gender)
    except Exception as e:
        error_message = str(e)
        return (JsonResponse({'result': error_message}))

    '''
     render: works in the view layer of the web application, combines several steps
     1. takes a request, a template, a dictionary
     2. returns HTTP request with the rendered HTML content
    '''
