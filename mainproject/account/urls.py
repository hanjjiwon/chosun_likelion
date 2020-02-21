from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup

app_name = "account"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('signup/', signup, name='signup'),
]