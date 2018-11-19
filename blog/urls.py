from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('<int:post_id>/', views.post_view, name='post_view'),
    path('<int:post_id>/comment', views.new_comment, name='new_comment'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('dashboard/posts/', views.dashboard_posts, name='dashboard_posts'),
    path('dashboard/comments/', views.dashboard_comments, name='dashboard_comments'),
    path('dashboard/static/', views.dashboard_static, name='dashboard_static'),
    path('dashboard/page/', views.dashboard_page, name='dashboard_page'),
]