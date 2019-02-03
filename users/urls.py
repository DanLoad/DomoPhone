from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('user_owned', views.user_owned, name='users_owned'),
    url('all_owned', views.all_owned, name='all_owned'),
    url('rfid_owned', views.rfid_owned, name='rfid_owned'),
    url('rf_owned', views.rf_owned, name='rf_owned'),
    url('finger_owned', views.finger_owned, name='finger_owned'),
    url('', views.index, name='users')

]
