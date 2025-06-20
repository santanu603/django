from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'), 
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('entry/', views.entry, name='entry'),
    path('view_update/', views.view_update, name='view_update'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('filter/', views.filter_chq, name='filter_chq'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('delivery_management/',views.delivery_main, name='delivery_main'),
    path('filter_delivery/',views.filter_delivery,name='filter_delivery'),
    path('edit_delivery/<int:id>/', views.edit_delivery, name='edit_delivery'),
    path('replacement_main/',views.replacement_main,name='replacement_main'),
    path('filter_replacement/',views.filter_replacement, name='filter_replacement'),
    path('edit_replacement/<int:id>',views.edit_replacement, name='edit_replacement'),
    path('delete_delivery/<int:id>/',views.delete_delivery, name='delete_delivery'),
    path('delete_replacement/<int:id>',views.delete_replacement, name='delete_replacement'),
    path('note_calculator/', views.note_calculator, name='note_calculator'),
    path('video_gallery/', views.video_gallery, name='video_gallery'),
    path('cat_boat/', views.cat_boat, name='cat_boat'),
    path('b_neckband/',views.b_neckband, name='b_neckband'),
    path('b_airdopes/',views.b_airdopes, name='b_airdopes'),
    path('b_headphone/',views.b_headphone, name='b_headphone'),
    path('b_overhead/',views.b_overhead, name='b_overhead'),
    path('b_smartwatch/',views.b_smartwatch, name='b_smartwatch'),
    path('b_speaker/',views.b_speaker, name='b_speaker'),
    path('b_bar/',views.b_bar, name='b_bar'),
    path('new_order_entry/',views.new_order_entry, name='new_order_entry'),
    path('new_order_filter/',views.new_order_filter, name='new_order_filter'),
    path('edit_new_order/<int:id>/', views.edit_new_order, name='edit_new_order'),
    path('delete_new_order/<int:id>/',views.delete_new_order, name='delete_new_order'),
    path('boat_ticket_entry/',views.boat_ticket_entry, name='boat_ticket_entry'),
    path('boat_ticket_view/',views.boat_ticket_view, name='boat_ticket_view'),
    path('boat_pricelist/',views.boat_pricelist,name='boat_pricelist'),
    path('voxg_product_pricelist/',views.voxg_product_pricelist,name='voxg_product_pricelist'),
    path('voxg_battery_pricelist/',views.voxg_battery_pricelist,name='voxg_battery_pricelist'),
    path('jbl_pricelist/',views.jbl_pricelist,name='jbl_pricelist'),
    path('fingers_pricelist/',views.fingers_pricelist,name='fingers_pricelist'),
    path('fastrack_pricelist/',views.fastrack_pricelist,name='fastrack_pricelist'),
    path('agent_activities/',views.agent_activities,name='agent_activities'),
    path('special_discount/',views.special_discount,name='special_discount')
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)