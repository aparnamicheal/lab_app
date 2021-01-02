from django.urls import path
from . import views
urlpatterns = [
    path('login',views.log,name='login'),
    path('userreg',views.ureg),
    path('labreg',views.labreg,name="lab"),
    path('staff',views.stafreg),
    path('doct',views.addoct),
    path('category',views.category),
    path("newtest",views.newtst),
    #index....# templates.........#
    path("lab",views.indx),
    path("index1",views.index1),
    #path("index2",views.index2),
    path("user_profile",views.userprofile),
    path("user_home",views.user_home),
    path("labowner_home",views.labowner_home),
    path("admin_home",views.admin_home),
    path("delete",views.delete)
    ]







