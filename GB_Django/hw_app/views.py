import logging
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.dates import MonthArchiveView, WeekArchiveView, ArchiveIndexView, YearArchiveView

from hw_app import models

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('<h1>Главная страница!</h1>')


def about(request):
    logger.info('About page accessed')
    return HttpResponse('<h1>Страница обо мне.</h1>')


class CustomerView(DetailView):
    model = models.Customer
    template_name = 'hw_app/customer_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = datetime.now()
        return context


class AllProducts(ArchiveIndexView):
    model = models.Order
    date_field = 'ordered_at'
    template_name = 'hw_app/all_products.html'
    allow_future = False
    week_format = '%U'
    year_format = '%Y'

    def get_context_data(self, **kwargs):
        customer = models.Customer.objects.get(pk=self.kwargs.get('pk'))
        orders = super().get_queryset().filter(customer=customer).prefetch_related('products')
        products = set(product for order in orders for product in order.products.values_list('title'))

        context = super().get_context_data(**kwargs)
        context['products'] = products
        context['customer'] = customer

        return context

    def get_queryset(self, **kwargs):
        orders = models.Order.objects.get_queryset().filter(customer=self.kwargs.get('pk'))

        return orders


class AllYearProducts(AllProducts, YearArchiveView):
    pass


class AllMonthProducts(AllProducts, MonthArchiveView):
    pass


class AllWeekProducts(AllProducts, WeekArchiveView):
    pass
