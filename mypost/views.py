from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article
from . import forms

# Create your views here.
def home(request):
    posts = Article.objects.all().order_by('-pub_date')
    context = {
        'posts':posts
    }
    return render(request, 'mypost/home.html',context)

def full_article(request, blog_id):
    article = get_object_or_404(Article, pk=blog_id)
    return render(request, 'mypost/full_article.html',{'article':article})

def add_post(request):
    if request.method == 'POST':
        form = forms.AddBlog(request.POST)

        if form.is_valid():
            new_post = Article(title = request.POST['title'], blog_content = request.POST['blog_content'], author = request.POST['author'])
            new_post.save()
            return redirect('home')

    else:
        form = forms.AddBlog()

    context = {'form':form}
    return render(request, 'mypost/add_post.html', context)

