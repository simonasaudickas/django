from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.user_registration, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('profilis/', views.profilis, name='profilis'),
    path('post_article/',views.post_article, name='publikuoti-str')

]
