from django.shortcuts import render

from blog.models import BlogSettings, Post

def index_renderer(request, context):
    blog_data = BlogSettings.objects.get(pk=1)
    context['blog_title'] = blog_data.title
    return render(request,'blog/index.html', context)

def static_page_renderer(request, context):
    blog_data = BlogSettings.objects.get(pk=1)
    context['blog_title'] = blog_data.title
    return render(request, 'blog/static-page.html', context)
    
def dashboard_renderer(request, context):
    return render(request, 'blog/editor-dashboard.html', context)
  