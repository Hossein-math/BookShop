from django.urls import path

from .views import SignUpView, CustomLogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]