from django.urls import path, reverse_lazy
from user.views import UserRegisterView, UserLoginView
from django.contrib.auth.views import LogoutView

app_name = 'user'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('user:login')), name='logout'),
]