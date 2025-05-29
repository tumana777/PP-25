from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from user.forms import UserRegisterForm
from .models import Profile
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

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

    def form_valid(self, form):

        user = form.save(commit=False)
        user.is_active = False
        user.save()

        self.send_verification_email(user)
        messages.success(self.request, 'Account created successfully. Verification link has been sent to your email.')

        return redirect('user:login')

    def send_verification_email(self, user):
        token = default_token_generator.make_token(user)
        uid = user.pk
        verification_link = self.request.build_absolute_uri(reverse('user:activate', kwargs={'uid': uid, 'token': token}))

        send_mail(
            "Verify your account",
            f"Hello, {user.username}, please activate your account by clicking on the link below: {verification_link}",
            "",
            [user.email],
        )

def activate_account(request, uid, token):
    user = User.objects.get(pk=uid)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated successfully.')
        return redirect('user:login')
    else:
        return HttpResponse('Activation link is invalid!')

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('core:index')

# class UserLogoutView(LogoutView):
#     next_page = reverse_lazy('user:login')