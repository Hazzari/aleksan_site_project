from datetime import date

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.http import require_GET

dateOfBirth = date(1984, 1, 7)


def calculate_age(dateOfBirth):
    today = date.today()
    return today.year - dateOfBirth.year - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))


def index(request):
    age = calculate_age(dateOfBirth)

    args = {'age': age,
            'arg2': 2}

    return render(request, 'homepage/index.html', args)


class Sysadmin(TemplateView):
    template_name = 'homepage/sysadmin.html'


class Developer(TemplateView):
    template_name = 'homepage/developer.html'


class Contacts(TemplateView):
    template_name = 'homepage/cont.html'
#
# class IndexPageView(TemplateView):
#     # пустого класса уже достаточно чтобы сделать запрос
#     # МОЖНО СДЕЛАТЬ ЕЩЕ ПРОЩЕ- Сразу импортировать в URLS.PY и там уже:
#     # в path('', views.TemplateView.as_view(), template_name = 'homepage/index.html'),
#     # Сразу передать страницу
#     template_name = 'homepage/index.html'
