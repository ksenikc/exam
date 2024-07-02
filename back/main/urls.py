from django.urls import path
from django.conf import settings
from .views import home, create_statements,UserOrdersListView,project
from users import views as user_views

urlpatterns = [
    path("", home),
    path("project/", project,name="projects"),
    path('create_statements/', create_statements, name='create_statements'),
    path('statements/<str:username>', UserOrdersListView.as_view(), name='statement_list'),
]
