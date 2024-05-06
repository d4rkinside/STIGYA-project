from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('change-password/', views.change_password, name='change_password'),
    path('productlist/', views.productlist, name='productlist'),
    path('add/',views.add,name='add'),
    path('edit/',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name='delete'),
    path('sele/',views.sele,name='sele'),
    path('addtocart',views.addtocart,name='addtocart')
]
