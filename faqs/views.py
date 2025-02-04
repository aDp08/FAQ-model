from django.shortcuts import render, redirect
from .models import FAQ, UserQuestion
from .forms import FAQForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import FAQSerializer


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        return FAQ.objects.all().values('question', 'answer', f'question_{lang}')

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faqs/faq_list.html', {'faqs': faqs})

def add_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
        else:
            print(form.errors) 
    else:
        form = FAQForm()

    return render(request, 'faqs/add_faq.html', {'form': form})


@csrf_protect  
@require_POST  
def submit_question(request):
    try:
        data = json.loads(request.body)
        question = data.get("question", "")

        if not question:
            return JsonResponse({"error": "Question cannot be empty!"}, status=400)

        # Save question to database
        UserQuestion.objects.create(question=question)

        return JsonResponse({"message": "Question submitted successfully!"}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data!"}, status=400)


def faq_page(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq_page.html', {'faqs': faqs})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/admin/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def faq_view(request):
    faqs = FAQ.objects.all()  
    return render(request, 'faqs/faq_page.html', {'faqs': faqs})

