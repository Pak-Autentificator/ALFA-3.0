from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("blog/", views.index, name="main"),
    path("blog/post<id>", views.post, name="post"),
    path("about.html", views.about, name="about"),
    path("contacts.html", views.contacts, name="contacts"),
    path("services.html", views.services, name="services"),
    path("blog/category/<id>", views.category, name="category"),
    path("blog/search/", views.search, name="search"),
    path("blog/create/", views.create, name="create"),
    path("blog/login/", LoginView.as_view(), name='blog_login'),
    path("blog/logout/", LogoutView.as_view(), name='blog_logout'),
    path("blog/profile/", views.profile, name='blog_profile'),
    path('blog/profile/update/', views.update_file, name='update_file'),

]
