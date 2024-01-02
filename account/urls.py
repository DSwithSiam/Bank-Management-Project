from django.urls import path
from . views  import *

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('register/', UserRegister.as_view(), name="register"),
]
