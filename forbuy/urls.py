from django.urls import path, include
from forbuy import views

urlpatterns = [

    path('show_buymsg/', views.show_buymsg),
    path('add_buymsg/', views.add_buymsg),
    path('add_buymsg_to/', views.add_buymsg_to),
    path('del_buymsg/', views.del_buymsg),
    path('show_buymsg_all_bypage/', views.show_buymsg_all_bypage),
    path('modify_buymsg_ajax/', views.modify_buymsg_ajax),

]