from django.urls import include , path
from .views import home_user

urlpatterns = [
    path("",home_user,name='user')
]