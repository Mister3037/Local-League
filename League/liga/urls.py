from django.urls import path
from .views import *

app_name = 'liga'

urlpatterns = [
    path('', HomePageVIEW.as_view(), name="home"),
    path('table/', TablePageVIEW.as_view(), name="tables"),
    path('contact/', ContactUs.as_view(), name="contact"),
    path('team/<int:id>/', TeamDetailVIEW.as_view(), name="team_detail"),
]