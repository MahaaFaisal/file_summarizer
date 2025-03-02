import os
from django.conf import settings
from django.http import JsonResponse
from langchain_sambanova import ChatSambaNovaCloud

def get_summary_fun(content, age, gender):
    SAMBANOVA_API_KEY = settings.SAMBANOVA_API_KEY
    llm = ChatSambaNovaCloud(
        model="Meta-Llama-3.3-70B-Instruct",
    )
    messages = [ 
        ('system', 'you are a consice summerizer, summarize user input exactly to the point in the context of a %s yearsold %s' % (age, gender)),
        ('human', content)
    ]
    sambanova_response = llm.invoke(messages)
    return JsonResponse({'result': sambanova_response.content})

