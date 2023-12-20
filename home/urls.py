from django.urls import path
from . import views 

urlpatterns = [
    path('',views.defaultmessage, name='default'),
    path('home/',views.homemessage, name='home'),
    path('users/',views.usershow, name='users'),
    path('users/<int:id>/',views.getid, name='user'),
    path('users/<int:id>/delete/',views.deleteobj, name='delete'),
    path('reg/',views.registerform, name='register'),
    path('users/<int:id>/update/',views.Update,name='update'),
]
