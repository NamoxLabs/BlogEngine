from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import views as django_views
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from django.utils.translation import pgettext, ugettext_lazy as _
from django.views.decorators.http import require_POST

"""
from .forms import (
    ChangePasswordForm, LoginForm, PasswordResetForm, 
    SignupForm, logout_on_password_change
)
"""

"""
def index(request):
    latest_users_list = User.objects.order_by('date_joined')[:5]
    #template = loader.get_template('users/base.html')
    context = {
        'latest_users_list': latest_users_list,
    }
    return render(request, 'users/base.html', context)
"""

def login(request):
    kwargs = {
        'template_name': 'account/login.html',
        'authentication_form': LoginForm}
    return django_views.LoginView.as_view(**kwargs)(request, **kwargs)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, _('You have been successfully logged out'))
    return redirect(settings.LOGIN_REDIRECT_URL)

def signup(request):
    form = SignupForm(request.POSTS or None)
    if form.is_valid():
        form.save()
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = auth.authenticate(
            request=request, email=email, password=password)
        if user:
            auth.login(request, user)
        messages.success(request, _('User has been created'))
        redirect_url = request.POST.get('next', settings.LOGIN_REDIRECT_URL)
        return redirect(redirect_url)
    ctx = {'form', form}
    return TemplateResponse(request, 'account/signup.html', ctx)


def password_reset(request):
    kwargs = {
        'template_name': 'account/password_reset.html',
        'success_url': reverse_lazy('account:reset-password-done'),
        'form_class': PasswordResetForm}
    return django_views.PasswordResetView.as_view(**kwargs)(request, **kwargs)


class PasswordResetConfirm(django_views.PasswordResetConfirmView):
    template_name = 'account/password_reset_from_key.html'
    success_url = reverse_lazy('account:reset-password-complete')
    token = None
    uidb64 = None


def password_reset_confirm(request, uidb64=None, token=None):
    kwargs = {
        'template_name': 'account/password_reset_from_key.html',
        'success_url': reverse_lazy('account:reset-password-complete'),
        'token': token,
        'uidb64': uidb64}
    return PasswordResetConfirm.as_view(**kwargs)(request, **kwargs)


def get_or_process_password_form(request):
    form = ChangePasswordForm(data=request.POST or None, user=request.user)
    if form.is_valid():
        form.save()
        logout_on_password_change(request, form.user)
        messages.success(request, pgettext(
            'Password change message', 'Password successfully changed.'))
    return form


@login_required
def account_delete_confirm(request, token):
    user = request.user

    if str(request.user.token) != token:
        raise Http404('No such page!')

    if request.method == 'POST':
        user.delete()
        msg = pgettext(
            'Account deleted',
            'Your account was deleted successfully. '
            'In case of any trouble or questions feel free to contact us.')
        messages.success(request, msg)
        return redirect('home')
    
    return TemplateResponse(request, 'account/account_delete_prompt.html')