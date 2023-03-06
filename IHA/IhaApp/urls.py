from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginPage, name='index'),
    path('register', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create', views.create_iha, name='create_iha'),
    path('update/<int:iha_pk>', views.update_iha, name='update_iha'),
    path('delete/<int:iha_pk>', views.delete_iha, name='delete_iha'),
    path('404', views.error_page_404, name='404'),
]
