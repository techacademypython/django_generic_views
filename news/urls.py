from django.urls import path
from .views import NewsCreateView, HomePage, AddDataView, \
    NewsListView, NewsUpdateView, NewsDeleteView, NewsDetailView


urlpatterns = [
    path('', HomePage.as_view(), name="home_view"),
    path('add/', NewsCreateView.as_view(), name="news-create"),
    path('list/', NewsListView.as_view(), name="news-list"),
    path('update/<int:pk>/', NewsUpdateView.as_view(), name="news-update"),
    path('delete/<int:pk>/', NewsDeleteView.as_view(), name="news-delete"),
    path('detail/<int:pk>/', NewsDetailView.as_view(), name="news-detail"),

    path('data/', AddDataView.as_view(), name="add-data"),
]