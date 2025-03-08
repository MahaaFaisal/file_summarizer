import os
from django.conf import settings
from django.http import JsonResponse
import json
from main.srcs.get_content import get_content_fun
from langchain_sambanova import ChatSambaNovaCloud
from main.models import requests_table
from rest_framework_api_key.models import APIKey

def store_summary(request, content, summary):
    key = request.headers.get('Authorization').split(" ")[1]
    r = requests_table(
        user = APIKey.objects.get_from_key(key),
        content = content,
        summary = summary,
        age = request.POST.get("age"),
        gender = request.POST.get("gender")
    )
    r.save()

def get_summary_fun(request):
    age = request.POST.get("age")
    gender = request.POST.get("gender")

    content_json = get_content_fun(request)
    content_dict = json.loads(content_json.content)
    content = content_dict.get("result")

    SAMBANOVA_API_KEY = settings.SAMBANOVA_API_KEY
    llm = ChatSambaNovaCloud(
        model="Meta-Llama-3.3-70B-Instruct",
    )
    messages = [ 
        ('system', 'you are a consice summerizer, summarize user input exactly to the point in the context of a %s yearsold %s' % (age, gender)),
        ('human', content)
    ]
    sambanova_response = llm.invoke(messages)
    store_summary(request, content, sambanova_response.content)
    return JsonResponse({'result': sambanova_response.content})

