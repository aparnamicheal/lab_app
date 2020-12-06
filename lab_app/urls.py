from django.urls import path
from . import views
urlpatterns = [
    path('labreg',views.labreg,name="lab"),
    path('login',views.log,name='login'),
    path('userreg',views.ureg),
    path('staff',views.stafreg),
    path('doct',views.addoct),
    path('category',views.category),
    path("newtest",views.newtst),
    #path("mail",views.mail),
    
]