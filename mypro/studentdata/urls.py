from django.urls import path
from .import views 
urlpatterns = [
    path('',views.home, name='studentdata-see' ),
    path('add/',views.adddata, name='add' ),
    path('delet/<str:id>',views.delet, name='delet' ),
    path('update/<str:id>',views.update, name='update')
    ]