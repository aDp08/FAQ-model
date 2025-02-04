from django.test import TestCase


import pytest
from faqs.models import FAQ

@pytest.mark.django_db
def test_faq_model_method():
    faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
    assert faq.get_question_length() == 15  

