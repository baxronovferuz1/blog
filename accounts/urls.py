from django.urls import path
from .views import SignupView


urlpatterns=[
    path('sign/', SignupView.as_view(), name='sign'),
]