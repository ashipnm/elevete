from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup' , signup , name='signup'),
    path('login/', user_login, name='login'),
    path('index/' , index , name='index'),
    
]
