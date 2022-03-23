from django.shortcuts import render, redirect
from django.views import generic, View
from posts.forms import CreatePostForm
from posts.models import Post, Category


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/post-list.html'
    # paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-date_published')
        context['latest_posts'] = Post.objects.all().order_by(
            '-date_published')[:3]
        context['category'] = Category.objects.all()
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/post-detail.html'
    context_object_name = 'post'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/post-update.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/post-delete.html'
    context_object_name = 'post'
    success_url = '/posts'


class CreatePost(generic.CreateView):
    form_class = CreatePostForm
    template_name = 'posts/post-create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
