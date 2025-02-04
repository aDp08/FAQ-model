
from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_list, name='faq_list'),  # FAQ list view
    path('add/', views.add_faq, name='add_faq'),  # Add FAQ page
    path('faq/', views.faq_view, name='faq_view'),
    path('submit_question/', views.submit_question, name='submit_question'),
    path('login/', views.login_view, name='login'),

]
