
from django.urls import path
from .views import UserBankAccountView, UserPasswordChange, UserRegistrationView, UserLoginView, UserLogoutView,UserBankAccountUpdateView
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserBankAccountView.as_view(), name='profile' ),
    path('profile/edit/', UserBankAccountUpdateView.as_view(), name='edit_profile' ),
    path('pass/change/<int:pk>', UserPasswordChange.as_view(), name='user_pass_change' ),
]