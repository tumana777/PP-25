from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from user.forms import UserRegisterForm
from .models import Profile

class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    login_url = 'user:login'

    def get_object(self, queryset=None):
        return self.request.user.profile

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('user:login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('core:index')

# class UserLogoutView(LogoutView):
#     next_page = reverse_lazy('user:login')