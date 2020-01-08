from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View, ListView

from lab5.models import Product, Review
import math


# Список продуктов
class ListProductView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 3

    def get(self, request, page=1):

        # Количество продуктов на странице
        elements_on_page = 9

        # Количество продуктов в строке
        elements_in_row = 3

        products = Product.objects.all()
        pages_count = math.ceil(len(products) / elements_on_page)

        start_index = (int(page) - 1) * elements_on_page
        end_index = start_index + elements_on_page
        products = products[start_index:end_index]

        index = 1
        rows = []
        row = []
        for product in products:
            row.append(product)

            if index == elements_in_row:
                rows.append(row)
                row = []
                index = 1
            else:
                index += 1

        if len(row) > 0:
            rows.append(row)

        return render(request, 'product_list.html', {"products": rows, "page": page, "pages_count": pages_count})


# Страница с информацией о продукте и отзывами
class ProductView(View):

    def get(self, request, product_id):

        elements_in_row = 2
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product_id=product_id)
        reviews_count = len(reviews)

        index = 1
        rows = []
        row = []
        for review in reviews:
            row.append(review)

            if index == elements_in_row:
                rows.append(row)
                row = []
                index = 1
            else:
                index += 1

        if len(row) > 0:
            rows.append(row)

        if len(rows) == 0:
            rows = None

        return render(request, 'product.html', {"product": product, "reviews": rows, "reviews_count": reviews_count})





