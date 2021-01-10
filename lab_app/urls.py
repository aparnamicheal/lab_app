from django.urls import path
from . import views
urlpatterns = [
    path('login',views.log,name='login'),
    path('userreg',views.ureg),
    path('labreg',views.labreg,name="lab"),
    path('staff',views.stafreg),
    path('doct_reg',views.doctreg),
    path('doctor_home',views.doctor_home),
    path('category',views.category),
    path("newtest",views.newtest),
    #index....# templates.........#
    path("lab",views.indx),
    path("index1",views.index1),
    #path("index2",views.index2),
    path("user_profile",views.userprofile),
    path("labownerprofile_index",views.labownerprofile_index),
    path("user_home",views.user_home),
    path("labowner_home",views.labowner_home),
    path("admin_home",views.admin_home),
    path("delete",views.delete),
    path("deletion",views.deletion),
    path("change_password",views.change_password),
    path("staff_view",views.staff_view),
    path("staff_home",views.staff_home),
    path("find_lab",views.find_lab),
    path("book_now",views.book_now),
    path("book_confirm",views.book_confirm),
    #path("view_labtest",views.view_labtest),
    path("lbowner_staffView",views.lbowner_staffView),
    path("addstaff_home",views.addstaff_home),
    path("staff_delete",views.staff_delete),
   
    ]







