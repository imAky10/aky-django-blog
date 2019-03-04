from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('<int:blog_id>/', views.full_article, name = 'full_article'),
    path('add_blog/', views.add_post, name = 'add_blog'),
    
]
