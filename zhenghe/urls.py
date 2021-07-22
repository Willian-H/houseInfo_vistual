from django.urls import path, include
from zhenghe import views

urlpatterns = [
    path('login/', views.to_login),
    path('checklogin/', views.check_login),
    path('add_user/', views.add_user),
    path('add_user_to/', views.add_user_to),
    path('menu/', views.menu),
    path('welcome/', views.welcome),

    path('showall_secondhand/', views.showall_secondhand),
    path('showall_secondhand_echarts/', views.showall_secondhand_echarts),
    path('show_secondhouse_bypage/', views.show_secondhouse_all_bypage),
    path("update_secondhouse_ajax/", views.modify_secondhouse_ajax),
    path('drop_secondhouse_ajax/', views.drop_secondhouse_ajax),
    path('to_add_secondhouse/', views.to_add_secondhouse),
    path('add_secondhouse/', views.add_secondhouse),

    path('showall_new/', views.showall_new),
    path('showall_new_echarts/', views.showall_new_echarts),
    path('show_newhouse_bypage/', views.show_newhouse_all_bypage),
    path("update_newhouse_ajax/", views.modify_newhouse_ajax),
    path("drop_newhouse_ajax/", views.drop_newhouse_ajax),
    path('to_add_newhouse/', views.to_add_newhouse),
    path('add_newhouse/', views.add_newhouse),

    path('showall_rent/', views.showall_rent),
    path('showall_rent_echarts/', views.showall_rent_echarts),
    path('show_renthouse_bypage/', views.show_renthouse_all_bypage),
    path("update_renthouse_ajax/", views.modify_renthouse_ajax),
    path("drop_renthouse_ajax/", views.drop_renthouse_ajax),
    path('to_add_renthouse/', views.to_add_renthouse),
    path('add_renthouse/', views.add_renthouse),

    path("test/", views.test)
]
