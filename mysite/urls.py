from django.urls import path
from .views import index,trackbook,register,signin,signout


urlpatterns=[
    path('',index,name='index'),
    path('trackbook/',trackbook,name='trackbook'),
    path('register/',register,name='register'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
]