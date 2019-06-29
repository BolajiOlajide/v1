from django.shortcuts import render

from blog_app.models import Post

# Create your views here.
def index(request):
    post = Post.objects.all().first()
    context = dict(post=post)
    return render(request, 'index.html', context)
