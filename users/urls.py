from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('user_owned', views.user_owned, name='users_owned'),
    url('rfid_owned', views.rfid_owned, name='rfid_owned'),
    url('', views.index, name='users')

]
