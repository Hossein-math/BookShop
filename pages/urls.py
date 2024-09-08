from django.urls import path

from pages.views import AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
]