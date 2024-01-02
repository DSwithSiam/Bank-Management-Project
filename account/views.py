from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from account.forms import UserRegisterFrom
from django.contrib.auth import login, logout

# Create your views here.
def profile(request):
    return render(request, 'profile')

class UserRegister(FormView):
    template_name = 'register.html'
    success_url = reverse_lazy('profile')
    form_class = UserRegisterFrom
    
    def form_valid(self, form):
        user =  form.save()
        login(user)
        return super().is_valid(form)
        
    