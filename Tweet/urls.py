from django.urls import path

from .import views

from django.contrib.auth import views as auth_views

urlpatterns = [
	# path('admin/', admin.site.urls),
    # path('', views.index, name = 'index'),
    path('tweet_list/', views.tweet_list, name = 'tweet_list'),
    path('create/', views.tweet_create, name = 'tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name = 'tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name = 'tweet_delete'),
    path('register/', views.register, name = 'register'),
    path('search/', views.search, name = 'search'), 
    path('login/', auth_views.LoginView.as_view(template_name= 'registration/login.html'), name = 'logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'tweet_list'), name = 'logout'), 
] 