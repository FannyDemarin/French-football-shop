from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm

from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    product_list = Product.objects.all()

    context = {
        'npm' : '2506561542 ',
        'name': 'Fanny Demarin',
        'class': 'KKI',
        'product_list': product_list
    }

    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.increment_views()

    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

def show_json(request):
    product_list = Product.objects.all()
    products_json = serializers.serialize('json', product_list)
    return HttpResponse(products_json, content_type='application/json')

def show_xml(request):
    product_list = Product.objects.all()
    products_xml = serializers.serialize('xml', product_list)
    return HttpResponse(products_xml, content_type='application/xml')

def show_json_by_id(request, product_id):
    try : 
        item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_xml_by_id(request, product_id):
    try:
        item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)