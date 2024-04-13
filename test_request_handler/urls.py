from django.urls import path
from test_request_handler import views

urlpatterns = [
    path("", views.home, name="home"),
    path("testai/tests/v1/execute", views.postData, name="testai")
]