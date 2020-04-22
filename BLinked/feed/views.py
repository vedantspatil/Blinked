from django.shortcuts import render
from blink.models import Post, User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    """
    renders the index page of feed

    :param request: request Object from Client
    :return: index page with multiple blogs
    """
    context = {
        'page': 'Blogs',
        'posts': Post.objects.all()
    }
    return render(request, 'feed/blog/home.html', context)


class PostListView(ListView):
    """
    renders the index page of feed

    :param request: request Object from Client
    :return: index page with multiple blogs
    """
    model = Post
    template_name = 'feed/blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Blogs'
        return context


class PostDetailView(DetailView):
    """
    renders a specific blog page

    :param request: request Object from Client
    :return: page of that specific blog
    """
    model = Post
    template_name = 'feed/blog/post_detail.html'


class PostCreateView(CreateView):
    """
    renders a blog creation page

    :param request: request Object from Client
    :return: form for posting blog
    """
    model = Post
    fields = ['title', 'content']
    template_name = 'feed/blog/post_form.html'

    def form_valid(self, form):
        bUser = User.objects.get(username=self.request.user.username)
        form.instance.author = bUser
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Create Post'
        return context


class PostUpdateView(UpdateView):
    """
    renders a blog updation page

    :param request: request Object from Client
    :return: form for updating blog
    """
    model = Post
    fields = ['title', 'content']
    template_name = 'feed/blog/post_form.html'

    def form_valid(self, form):
        bUser = User.objects.get(username=self.request.user.username)
        form.instance.author = bUser
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Update Post'
        return context


class PostDeleteView(DeleteView):
    """
    renders a blog deletion page

    :param request: request Object from Client
    :return: form for confirming deletion of blog
    """
    model = Post
    success_url = '/feed/'
    template_name = 'feed/blog/post_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Delete post'
        return context

