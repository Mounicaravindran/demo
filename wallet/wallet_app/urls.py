from django.urls import re_path
from wallet_app import views

urlpatterns = [
    re_path(r'^init$', views.InitializeWallet.as_view()),
    re_path(r'^wallet$', views.EnableWallet.as_view()),
]