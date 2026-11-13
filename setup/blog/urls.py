from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostViews.as_view(), name='home'),
]