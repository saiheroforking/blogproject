from django.views.generic import TemplateView, CreateView, ListView,UpdateView,DetailView,DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import SignupForm
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
from .models import Notification



class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    success_message = "Account created successfully. Please log in."


class LoginBlog(LoginView):
    template_name = 'login.html'


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 5
    login_url = reverse_lazy('login')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        user = self.request.user

        if user == post.author or user.is_superuser:
            form.add_error(None, "You cannot comment on your own post.")
            return self.form_invalid(form)
        form.instance.user = user
        form.instance.post = post

        if hasattr(user, 'role') and user.role == 'READER':
            form.instance.is_approved = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


class HomeView(TemplateView):
    template_name = 'home.html'



@login_required
def notifications(request):
    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by('-created_at')

    return render(request, 'blog/notifications.html', {
        'notifications': notifications
    })
