"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import about, index, predict_page, cuda_full, feedback, healthcheck, check_deepfake

app_name = 'ml_app'
handler404 = views.handler404

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('predict/', predict_page, name='predict'),
    path('cuda_full/', cuda_full, name='cuda_full'),
    path('api/healthcheck/', healthcheck, name='healthcheck'),  # Add this line
    path('api/check_deepfake/', check_deepfake, name='check_deepfake'),
]