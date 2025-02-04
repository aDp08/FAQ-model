

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faqs/', include('faqs.urls')),  # Include faqs app URLs
]
