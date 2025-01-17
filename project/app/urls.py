from django.urls import path
from.import views
urlpatterns = [
    path('',views.login_view,name='login_view'),
    path('sign/',views.signup_view),
    path('home/', views.home_view, name='home_view'),
    path('home/product/',views.product_view),
    path('home/product/cart/',views.cart_view),
    path('home/cart/',views.cart_view),
   
    
]
