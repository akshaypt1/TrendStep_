from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings
from .views import home, product_view

urlpatterns = [
    path('',views.login_view,name='login_view'),
    path('sign/',views.signup_view),
    path('home/', views.home, name='home'),
    path('home/product/',views.product_view),
    path('product/<int:product_id>/',views.product_view, name='product_detail'),
    path('home/product/cart/',views.cart_view),
    path('home/cart/',views.cart_view,name='cart'),
    path('men/',views.men,name='men'),
    path('woman/',views.women,name='women'),

   
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)