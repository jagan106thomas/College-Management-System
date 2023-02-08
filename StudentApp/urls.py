from django.urls import path
from StudentApp import views
urlpatterns=[
    path('',views.log_fun,name='log'),
    path('logdata',views.logdata_fun),
    path('reg',views.read_data,name='reg'),
    path('regdata',views.regdata_fun),
    path('home',views.home_fun,name='home'),
    path('add_students',views.addstudent_fun,name='add'),
    path('readdata',views.read_Stud_data),
    path('display',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='update'),
    path('Delete/<int:id>',views.delete_fun,name='Delete'),
    path('log_out',views.log_out_fun,name='log_out')
]
