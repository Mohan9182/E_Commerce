from django.urls import path
import user.views as views

urlpatterns = [
    path('signup',views.signup),
    path('',views.index),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('camera',views.camera,name='camera'),
    path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
]
