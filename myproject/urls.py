from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import CreateView

from app import views
from app.views import ArticleListView, ArticleDetailView

urlpatterns = [
   # path('cart/', include('cart.urls', namespace='cart')),
    # ===== АДМИНКА =====
    path('admin/', admin.site.urls),

    # ===== АУТЕНТИФИКАЦИЯ =====
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),

    # ===== ОСНОВНЫЕ СТРАНИЦЫ =====
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),

    # ===== ПОИСК =====
    path('search/', views.search_articles, name='search'),

    # ===== СТАТЬИ (CRUD) =====
    # 1. Список всех статей
    path('articles/', views.ArticleListView.as_view(), name='article_list'),

    # 2. СОЗДАНИЕ (должно быть ПЕРВЫМ среди article/)
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),

    # 3. Просмотр одной статьи
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),

    # 4. Редактирование
    path('article/<slug:slug>/update/', views.ArticleUpdateView.as_view(), name='article_update'),

    # 5. Удаление
    path('article/<slug:slug>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
]

# ===== МЕДИА-ФАЙЛЫ В РЕЖИМЕ РАЗРАБОТКИ =====
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)