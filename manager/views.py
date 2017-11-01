from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from .models import Categories, Items

# Create your views here.


def index(request):
    """URL: /manager/."""
    template = loader.get_template('manager/index.html')

    # Get last 10 categories using random order
    categories = Categories.objects.all().order_by('?')[:10]
    added = Items.objects.all().order_by('CreatedAt')[:10]
    changed = Items.objects.all().order_by('ChangedAt')[:10]

    context = {
        'categories': categories,
        'added': added,
        'changed': changed,
    }
    return HttpResponse(template.render(context, request))


def categories(request):
    """URL: /manager/categories/."""
    template = loader.get_template('manager/categories.html')

    categories = Categories.objects.all().order_by('Name')

    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))


def items(request, view, category=None, item=None):
    """URL: /manager/items/$view$/."""
    template = loader.get_template('manager/items.html')

    categories = Categories.objects.all().order_by('Name')
    items = None
    details = None

    if 'added' in view:
        items = Items.objects.all().order_by('CreatedAt')
    elif 'changed' in view:
        items = Items.objects.all().order_by('ChangedAt')
    elif ('all' in view) and (category is None):
        items = Items.objects.all().order_by('?')
    elif (category is not None) and (item is None):
        items = Items.objects.filter(Category=category).order_by('Title')
    elif (category is not None) and (item is not None):
        items = Items.objects.filter(Category=category).order_by('Title')
        details = Items.objects.get(ID=item)
    else:
        items = None
        details = None

    context = {
        'categories': categories,
        'items': items,
        'details': details,
    }
    return HttpResponse(template.render(context, request))


def items_add(request):
    """URL: /manager/items/."""
    template = loader.get_template('manager/items_add.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def items_edit(request, id):
    """URL: /manager/items/$id$/edit/."""
    template = loader.get_template('manager/items_edit.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def items_delete(request, id):
    """URL: /manager/items/$id$/edit/."""
    template = loader.get_template('manager/items_delete.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
