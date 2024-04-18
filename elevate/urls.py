from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static 
from django.conf import settings 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index,name='index'),
    path('base/',views.base,name='base'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('signout/',views.signout,name='signout'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profiledetails/',views.profiledeatils,name='profiledetails'),
    path('address/',views.address,name='address'),
    path('shop/<str:category>/',views.shop,name='shop'),
    path('signout/',views.signout,name="signout"),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
