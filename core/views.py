from django.views.generic import ListView
from django.http import JsonResponse

class FAQListView(ListView):
    def get(self, request, *args, **kwargs):
        data = {
            "faqs": [
                {"question": "What is Django?", "answer": "Django is a high-level Python web framework."},
                {"question": "How do I create a Django app?", "answer": "Use the command `python manage.py startapp app_name`."}
            ]
        }
        return JsonResponse(data)
