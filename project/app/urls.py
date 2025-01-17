from django.urls import path
from.import views
urlpatterns = [
    path('',views.login_view),
    path('sign/',views.signup_view),
    path('home/',views.home_view),
   
    
]
