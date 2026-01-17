from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import HomeView, SignUpView, LoginBlog, PostListView,PostCreateView,PostDetailView,PostUpdateView,PostDeleteView,CommentCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginBlog.as_view(), name='login'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
