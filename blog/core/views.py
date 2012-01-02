from django.views.generic import ListView
from blog.core.models import Post

class PostsView(ListView):

    context_object_name = 'posts'
    queryset = Post.objects.order_by('-created')[:10]
    template_name = "home.html"