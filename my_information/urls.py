from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('blog/<blog_id>/', views.blog_detail, name='blog'),
    path('Thanks', views.Thanks_page, name='Thanks')
]
