from django.db import models

from core.models import PublishedModel, TitleModel


class Category(PublishedModel, TitleModel):
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения',
        default=100,
    )

    class Meta:
        verbose_name = 'объект «Категория»'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel, TitleModel):
    slug = models.SlugField('Слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'объект «Топпинг»'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel, TitleModel):
    class Meta:
        verbose_name = 'объект «Обёртка»'
        verbose_name_plural = 'Обёртки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel, TitleModel):
    description = models.TextField('Описание')
    price = models.DecimalField(
        'Цена',
        max_digits=5,
        decimal_places=2,
        default=0
        )
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения',
        default=100,
    )
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обёртка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name='Топпинги')
    is_on_main = models.BooleanField(default=False, verbose_name='На главную')

    class Meta:
        verbose_name = 'объект «Мороженое»'
        verbose_name_plural = 'Мороженое'
        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title
