from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('website/website-blog-post.html')
def latestblog(arg=6):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    categories = Category.objects.all()
    post_dict = {}
    return {'posts':posts}
