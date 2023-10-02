import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Post, Category
from django.db.models import Q
from .forms import PostForm, UpdateFileForm




def dummy():
    return str(random.randint(1, 10))



def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count // 2 + 1
    return {"cat1": all[:half], "cat2": all[half:]}


# Create your views here.
def index(request):
    # posts = Post.objects.all()
    # posts = Post.objects.filter(title__contains='python')
    # posts = Post.objects.filter(published_date__year=2023)
    # posts = Post.objects.filter(category__name__iexact='python')
    #post = Post.objects.get(pk=2)
    posts = Post.objects.order_by('-published_date')
    dict = {'posts': posts}
    dict.update(get_categories())
    return render(request, "blog/index.html", context=dict)


def post(request, id=None):
    post = get_object_or_404(Post, pk=id)
    context = {"post": post}
    context.update(get_categories())
    return render(request, "blog/post.html", context=context)


def category(request, id=None):
    c = get_object_or_404(Category, pk=id)
    posts = Post.objects.filter(category=c).order_by('-published_date')
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context=context)



def about(request):
    return render(request, "blog/about.html")


def contacts(request):
    return render(request, "blog/contacts.html")


def services(request):
    return render(request, "blog/services.html")


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context=context)


@login_required
def create(request):
    context = {}
    form = PostForm
    if request.method == "POST":
        form = PostForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = now()
            post.user = request.user
            post.save()
            return index(request)

    return render(request, "blog/create.html", context=context)


def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'blog/profile.html', context)

@login_required
def update_file(request):
    if request.method == "POST":
        form = UpdateFileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'blog/profile.html')
    else:
        form = UpdateFileForm(instance=request.user)
    return render(request, 'blog/update_file.html', {'form': form})




