from . import views
from django.urls import path
# from .views import BlogList


urlpatterns = [
    # path('', views.BlogList.as_view(), name='home'),
    path('', views.BlogList, name='home'),
    path('error', views.Error, name='error'),
    path('search-blogs', views.BlogSearchView.as_view(), name = "search_blogs"),
    # path('footer', views.Footer, name='home'),
    path('<slug:slug>/', views.post_detail, name ='blog_single'),
]