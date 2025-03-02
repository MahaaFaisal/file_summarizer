from django.http import JsonResponse
from pypdf import PdfReader

def get_content_fun(request):  
    try:
        file = request.FILES['pdf']
        reader = PdfReader(file)
        content = ""
        for page in reader.pages:
            content += page.extract_text() or ""  # Handle potential None values
        return JsonResponse({'result': content})
    except:
        return JsonResponse({'result': 'File Not Found'})