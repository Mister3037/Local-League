from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('register/', RegisterVIEW.as_view(), name='register'),
    path('login/', LoginVIEW.as_view(), name="login"),
    path('logout/', LogoutVIEW.as_view(), name="logout"),
    # path('<int:id>', )
    path('profile/', ProfileVIEW.as_view(), name='profile'),
]