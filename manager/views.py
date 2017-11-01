from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    """URL: /manager/."""
    template = loader.get_template('manager/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def categories(request):
    """URL: /manager/categories/."""
    template = loader.get_template('manager/categories.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def items(request, view):
    """URL: /manager/items/$view$/."""
    template = loader.get_template('manager/items.html')
    context = {

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
