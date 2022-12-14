from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from blog.models import BlogPost, Tag
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm, CreateTagForm, UpdateTagForm
from account.models import Account


def create_tag_view(request):
    # initial={'owner': request.user.id}

    form = CreateTagForm()
    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['owner'] = request.user.id
        form = CreateTagForm(request_data)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'blog/create_tag.html', context)


def update_tag_view(request):
    # initial={'owner': request.user.id}

    form = UpdateTagForm()
    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['owner'] = request.user.id
        form = UpdateTagForm(request_data)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'blog/edit_tag.html', context)


def create_blog_view(request):
    tags = Tag.objects.all()
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            author = Account.objects.filter(email=request.user.email).first()
            obj.author = author
            obj.save()
            form = CreateBlogPostForm()
    context = {'tags': tags}
    context['form'] = form

    return render(request, 'blog/create_blog.html', context)


def detail_blog_view(request, slug):
    context = {}
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'blog/detail_blog.html', context)


def edit_blog_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj

    form = UpdateBlogPostForm(
        initial={
            "title": blog_post.title,
            "body": blog_post.body,
            "image": blog_post.image,
            "id": blog_post.id,
        }
    )
    context['form'] = form

    return render(request, 'blog/edit_blog.html', context)


def delete_blog_post(request, id):
    context = {}
    BlogPost.objects.filter(id=id).delete()

    return redirect('home')


def delete_tag(request, id):
    context = {}
    Tag.objects.filter(id=id).delete()

    return redirect('home')


def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = BlogPost.objects.filter(
            Q(title__contains=q) |
            Q(body__icontains=q)
        ).distinct()
        for post in posts:
            queryset.append(post)

    # create unique set and then convert to list
    return list(set(queryset))
