from django.urls import path
from .views import home, DetailNews, EditNews, DeleteNews, UploadNews

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', DetailNews.as_view(), name='detail'),
    path('upload/', UploadNews.as_view(), name='upload'),
    path('edit/<int:pk>/', EditNews.as_view(), name='edit'),
    path('delete/<int:pk>/', DeleteNews.as_view(), name='delete'),
]