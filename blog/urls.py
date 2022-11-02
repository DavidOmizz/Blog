from . import views
from django.urls import path
# from .views import BlogList


urlpatterns = [
    # path('', views.BlogList.as_view(), name='home'),
    path('', views.BlogList, name='home'),
    path('<slug:slug>/', views.post_detail, name ='blog_single'),
]