from django.urls import path

from .views import RegistrationAPIView

app_name = 'users'
urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
]
