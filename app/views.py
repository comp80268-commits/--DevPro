from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Article
from .forms import ArticleForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'app/home.html')


def about(request):
    team = [
        {'name': 'Айбек Асанов', 'role': 'Team Lead / Backend Developer', 'bio': '5 лет опыта в Django'},
        {'name': 'Гульнара Исакова', 'role': 'Frontend Developer', 'bio': 'Эксперт в Bootstrap и CSS'},
        {'name': 'Эрмек Абдиев', 'role': 'DevOps Engineer', 'bio': 'Специалист по деплою и Docker'},
        {'name': 'Айгуль Курманова', 'role': 'QA Engineer', 'bio': 'Находит все баги'},
        {'name': 'Бекболот Турусбеков', 'role': 'Mobile Developer', 'bio': 'Создаёт мобильные приложения'}
    ]
    return render(request, 'app/about.html', {'team': team})


def contact(request):
    return render(request, 'app/contact.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'app/profile.html')


class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Article.objects.all()  # авторизованные видят все статьи, включая черновики
        return Article.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'app/article_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Article.objects.all()  # авторизованные видят все статьи, включая черновики
        return Article.objects.filter(is_published=True)




class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app/article_form.html'
    context_object_name = 'article'
    extra_context = {'title': 'Создать статью'}


    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app/article_form.html'
    context_object_name = 'article'
    success_url = reverse_lazy('article_list')
    extra_context = {'title': 'Редактировать статью'}


def search_articles(request):
    query = request.GET.get('q', '')
    results = Article.objects.filter(is_published=True)
    if query:
        results = results.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'app/search.html', {'results': results, 'query': query})

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'app/article_confirm_delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('article_list')

