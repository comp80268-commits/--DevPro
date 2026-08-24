from django.contrib import admin
from django.utils.html import format_html
from .models import Article



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Настройка отображения модели Article в админ-панели
    """

    # ===== Что показывать в списке =====
    list_display = (
        'id',
        'title',
        'created_at',
        'is_published',
        'preview_content',
        'image_preview'
    )

    # ===== По каким полям кликать для перехода =====
    list_display_links = ('id', 'title')

    # ===== Какие поля можно редактировать прямо в списке =====
    list_editable = ('is_published',)

    # ===== Фильтры (справа) =====
    list_filter = (
        'is_published',
        'created_at',
        'updated_at'
    )

    # ===== Поиск =====
    search_fields = (
        'title',
        'content',
        'slug'
    )

    # ===== Сортировка по умолчанию =====
    ordering = ('-created_at',)

    # ===== Автоматическое заполнение slug =====
    prepopulated_fields = {'slug': ('title',)}

    # ===== Поля только для чтения =====
    readonly_fields = (
        'created_at',
        'updated_at',
        'image_preview_inline'
    )

    # ===== Группировка полей на странице редактирования =====
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'content', 'image')
        }),
        ('Изображение (превью)', {
            'fields': ('image_preview_inline',),
            'classes': ('collapse',)  # Скрыто по умолчанию
        }),
        ('Публикация', {
            'fields': ('is_published',),
        }),
        ('Системные даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Скрыто по умолчанию
        }),
    )

    # ===== Действия с выбранными записями =====
    actions = ['make_published', 'make_unpublished']

    # ===== Количество записей на странице =====
    list_per_page = 20

    # ===== Сохранение фильтров =====
    save_on_top = True

    # ===== Методы для отображения в списке =====

    def preview_content(self, obj):
        """Показывает первые 50 символов контента"""
        if len(obj.content) > 50:
            return obj.content[:50] + '...'
        return obj.content

    preview_content.short_description = 'Превью текста'

    def image_preview(self, obj):
        """Показывает миниатюру изображения в списке"""
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return '-'

    image_preview.short_description = 'Фото'

    def image_preview_inline(self, obj):
        """Показывает большое превью на странице редактирования"""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px; border-radius: 8px;" />',
                obj.image.url
            )
        return 'Изображение не загружено'

    image_preview_inline.short_description = 'Превью изображения'

    # ===== Действия =====

    def make_published(self, request, queryset):
        """Опубликовать выбранные статьи"""
        count = queryset.update(is_published=True)
        self.message_user(request, f'Опубликовано {count} статей.')

    make_published.short_description = '✅ Опубликовать выбранные статьи'

    def make_unpublished(self, request, queryset):
        """Снять с публикации выбранные статьи"""
        count = queryset.update(is_published=False)
        self.message_user(request, f'Снято с публикации {count} статей.')

    make_unpublished.short_description = '📌 Снять с публикации'

# ========== СПОСОБ 2: Старая регистрация (без декоратора) ==========
# admin.site.register(Article, ArticleAdmin)