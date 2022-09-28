from django.shortcuts import render,get_object_or_404

import blog
from .models import Blog
def allBlogs(request):
    blog=Blog.objects.all().order_by('-date')
    return render(request,'blogs/allBlogs.html',{"blogs":blog,},)
def detail(request,blog_id):
    # pk means primary key , " get_object_or_404 " returns the object with matching pk or a 404 reponse
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blogs/detail.html',{"blog":blog})