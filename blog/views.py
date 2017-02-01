from django.shortcuts import render
from blog.models import BlogPost

# Create your views here.
def index(request):
    blogposts = BlogPost.objects.all().order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'navbar': 'index', 'blogposts': blogposts})
