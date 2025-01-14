from django.urls import path
from.import views
urlpatterns = [
    path('',views.login),
    path('sign',views.sign),
    path('',views.home),
    
    
]