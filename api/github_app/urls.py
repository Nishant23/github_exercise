from django.urls import  path
from . import views

urlpatterns = [
    path('get_repos/<org_name>', views.get_repos),
]