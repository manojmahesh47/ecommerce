from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def allProdCat(request, c_slug=None):
    c_page = None
    products = None  # Initialize 'products' variable

    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=c_page, available=True)
        print(products)
    else:
        product_list = Product.objects.filter(available=True)
        paginator = Paginator(product_list, 6)

        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            products = paginator.page(page)
        except (EmptyPage, InvalidPage):
            products = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': c_page, 'products': products})

def proDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Product.DoesNotExist:

        return HttpResponse("Product not found", status=404)

    return render(request, 'product.html', {'product': product})
