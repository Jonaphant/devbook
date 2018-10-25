
from django.urls import path, include
from . import views

app_name = 'userprofile'
urlpatterns = [
    path('', views.index, name="index"),
    path('info/<int:user_id>', views.info, name="info"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('info/<int:user_id>/update', views.updateInfo, name="updateInfo"),
]