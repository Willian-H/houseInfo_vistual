from django.urls import path, include
from forrent import views

urlpatterns = [

    path('show_rentmsg/', views.show_rentmsg),
    path('add_rentmsg/', views.add_rentmsg),
    path('add_rentmsg_to/', views.add_rentmsg_to),
    path('del_rentmsg/', views.del_rentmsg),
    path('show_rentmsg_all_bypage/', views.show_rentmsg_all_bypage),
    path('modify_rentmsg_ajax/', views.modify_rentmsg_ajax),

]
