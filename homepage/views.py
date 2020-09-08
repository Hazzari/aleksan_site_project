from datetime import date

from django.shortcuts import render
from django.views.generic import TemplateView

DATE_OF_BIRTH = date(1984, 1, 7)


def calculate_age(dateOfBirth):
    today = date.today()
    return today.year - dateOfBirth.year - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))


def index(request):
    age = calculate_age(DATE_OF_BIRTH)

    args = {'age': age, }

    return render(request, 'homepage/index.html', args)


class Sysadmin(TemplateView):
    template_name = 'homepage/sys.html'


class Developer(TemplateView):
    template_name = 'homepage/dev.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        age = calculate_age(DATE_OF_BIRTH)
        context['age'] = age
        return context


class Contacts(TemplateView):
    template_name = 'homepage/contact.html'
