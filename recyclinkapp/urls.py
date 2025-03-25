from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='home.html'), name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('user/', views.user_dashboard, name='user_dashboard'),
    path('business/', views.business_dashboard, name='business_dashboard'),
    path('redeem/', views.redeem, name='redeem'),
    path('report/', views.report, name='report'),
    path('feedback/', views.feedback, name='feedback'),
    path('blog/', views.blog, name='blog'),
    path('update-points/', views.update_points, name='update_points'),
]

