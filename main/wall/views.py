from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User

from .models import Post


class UserPostListView(ListView):
    # Модель Post в model.py
    model = Post

    # Имя шаблона html
    template_name = 'blog/user_posts.html'

    '''
    # objects, model_постфикс, наш вариант
    # 1ый варианта
    # контекст переменная хранения данных
    # представление-модель-что это
    # context_object_name = 'blog_post_user_list'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')
    '''

    # 2ой вариант
    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Post.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['blog_post_user_list'] = queryset.order_by('-date_created')
        return context
