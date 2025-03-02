from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter
# from main.views import PostViewSet

app_name = "main"

# post_router = DefaultRouter()
urlpatterns = [
    path("", views.home, name="home"),
    # path("", views.send_request, name="send_request")
    path("get_content", views.get_content, name="get_content"),
    path("summarize_content", views.summarize_content, name="summarize_content")
]