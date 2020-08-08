from . import views
from django.urls import include

from django.urls import path
from .feeds import PostsFeed, AtomSiteNewsFeed

urlpatterns = [
    path("feed/rss", PostsFeed(), name="rss_feed"),
    path("feed/atom", AtomSiteNewsFeed(), name="atom_feed"),
    path("", views.PostList.as_view(), name="home"),
    path(
        "<slug:slug>/", views.PostDetail.as_view(), name="post_detail"
    ),  # TODO: Chnage to int:ID
]
