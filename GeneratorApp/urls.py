from django.urls import path

from . import views
from .feeds import AtomSiteNewsFeed, PostsFeed

urlpatterns = [
    path("feed/rss", PostsFeed(), name="rss_feed"),
    path("feed/atom", AtomSiteNewsFeed(), name="atom_feed"),
    path("", views.PostList.as_view(), name="home"),
    path(
        "<slug:slug>/", views.PostDetail.as_view(), name="post_detail"
    ),  # TODO: Change to int:ID
]
