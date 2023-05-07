from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
from user.models import Profile


def new(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article:detail', id=article.id)
    return render(request, 'new.html', {'form': form})


def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'detail.html', {'article': article, "profile": profile})


def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=Article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
    return render(request, 'edit.html', {'form': form, 'article': article})


def destroy(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    return redirect('main:index')
