from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed


class PostsFeed(Feed):
    title = "RSSGenerator"
    link = ""
    description = "RSSGenerator - Posts."

    def items(self):
        return Post.objects.order_by("-created_on")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)


class AtomSiteNewsFeed(PostsFeed):
    feed_type = Atom1Feed
    subtitle = PostsFeed.description
