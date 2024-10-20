from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Возьмём нужное. А ненужное не возьмём:
    ice_cream_list = IceCream.objects.values(
        'id',
        'title',
        'price',
        'description'
        ).filter(
            is_published=True,
            is_on_main=True,
            category__is_published=True
        )
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
