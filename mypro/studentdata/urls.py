from django.urls import path
from .import views 
urlpatterns = [
    path('',views.home, name='studentdata-see' ),
    path('add/',views.adddata, name='add' ),
   path(' home/<slug:id>',views.delet, name='delet' )
    ]