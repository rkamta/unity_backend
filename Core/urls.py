from django.urls import include,path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', auth_views.LoginView.as_view(template_name='index.html', redirect_authenticated_user=True), name='login'),
    # path('',views.index,name='index'),
    path('authorize', views.authorize, name='authorize'),
    path('SignUp', views.signup, name='SignUp'),
    # path('Register', views.registeruser, name='Register'),
    path('check_mail', views.check_mail, name='check_mail')
]
