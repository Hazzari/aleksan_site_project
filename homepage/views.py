from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.http import require_GET


def index(request):
    args = {'arg1': 1,
            'arg2': 2}

    return render(request, 'homepage/index.html', args)

#
# class IndexPageView(TemplateView):
#     # пустого класса уже достаточно чтобы сделать запрос
#     # МОЖНО СДЕЛАТЬ ЕЩЕ ПРОЩЕ- Сразу импортировать в URLS.PY и там уже:
#     # в path('', views.TemplateView.as_view(), template_name = 'homepage/index.html'),
#     # Сразу передать страницу
#     template_name = 'homepage/index.html'
