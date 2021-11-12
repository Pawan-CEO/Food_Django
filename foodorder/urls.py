from django.conf.urls import url,include
from foodorder import views

urlpatterns=[
url('login',views.loginn),
url('home',views.home),
url('order',views.order),
url('addfood',views.addfoods),
url('signup',views.signup),
url('addcard',views.ddcard),
url('logout',views.logouts),
]