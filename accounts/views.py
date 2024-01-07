from django.contrib import messages
from django.shortcuts import render
from django.views.generic import FormView

from transactions.views import ConfarmationEmail
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin




class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

def UserLogoutView(request):
    logout(request)
    return redirect('home')



class UserBankAccountUpdateView(LoginRequiredMixin, View):
    template_name = 'accounts/edit_profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})


class UserBankAccountView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        user = self.request.user
        return render(request, self.template_name, {'user': user})


class UserPasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/pass_change.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'pk'
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = self.request.user
        if form.is_valid():
            login(self.request, user)
            messages.success(
                    request,
                    f'Password has been successfully changed'
                )
            mail_subject = 'Password has been successfully changed'        
            to_email = self.request.user.email
            ConfarmationEmail(self.request.user ,to_email, "Transfer", mail_subject, 0, 'accounts/pass_change_email.html')

            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    