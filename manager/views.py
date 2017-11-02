import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader

from .forms import ItemsForm
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

    # Get all categories data and set the context dict
    categories = Categories.objects.all().order_by('Name')
    items = None
    details = None

    # Check about view context and variables
    if ('added' in view):
        # Order items by creation date
        items = Items.objects.all().order_by('CreatedAt')
    elif 'changed' in view:
        # Order items by edit date
        items = Items.objects.all().order_by('ChangedAt')
    elif ('all' in view) and (category is None):
        # Order items randomly
        items = Items.objects.all().order_by('?')
    else:
        items = None
        details = None

    if (category is not None):
        # Get items from specific category and order by Title
        items = Items.objects.filter(Category=category).order_by('Title')

        # Check if there is any item selected
        if item is not None:
            # Get item details
            details = Items.objects.get(ID=item)

    context = {
        'categories': categories,
        'items': items,
        'details': details,
    }
    return HttpResponse(template.render(context, request))


@login_required
def items_add(request):
    """URL: /manager/items/add/."""
    template = loader.get_template('manager/items_add.html')

    # Only render the view if the user is authenticated
    if request.user.is_authenticated():
        # Check the request method from the page
        if request.method == 'GET':
            # Load Items form
            form = ItemsForm()
        else:
            # Start checking the POST request
            form = ItemsForm(request.POST)
            # If data is valid, proceeds to create a new item and redirect the user
            if form.is_valid():
                # Get form fields and values
                Category = form.cleaned_data['Category']
                Title = form.cleaned_data['Title']
                Description = form.cleaned_data['Description']
                User = request.user

                # Create model instance to save the data
                create = Items()
                create.Category = Category
                create.Title = Title
                create.Description = Description
                create.User = User

                # Commit the data
                create.save()

                # Redirect the user to the items list
                return redirect('/manager/items/all/')

    else:
        # Redirect the user for the last page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def items_edit(request, id):
    """URL: /manager/items/edit/$id$/."""
    template = loader.get_template('manager/items_edit.html')

    # Only render the view if the user is authenticated
    if request.user.is_authenticated():
        # Check the request method from the page
        if request.method == 'GET':
            # Load Items form
            data = Items.objects.get(pk=id, User=request.user)
            form = ItemsForm(instance=data)
        else:
            # Start checking the POST request
            form = ItemsForm(request.POST)
            # If data is valid, proceeds to create a new item and redirect the user
            if form.is_valid():
                # Get form fields and values
                Category = form.cleaned_data['Category']
                Title = form.cleaned_data['Title']
                Description = form.cleaned_data['Description']

                # Create model instance to save the data
                update = Items.objects.get(pk=id, User=request.user)
                update.Category = Category
                update.Title = Title
                update.Description = Description
                update.ChangedAt = datetime.datetime.now()

                # Commit the data
                update.save()

                # Redirect the user to the items list
                return redirect('/manager/items/all/')

    else:
        # Redirect the user for the last page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def items_delete(request, id):
    """URL: /manager/items/delete/$id$/."""
    template = loader.get_template('manager/items_delete.html')

    # Only render the view if the user is authenticated
    if request.user.is_authenticated():
        if request.method == 'POST':
            # Get the item ID with the same user authenticated ID
            delete = Items.objects.get(pk=id, User=request.user)
            # Commit the delete command
            delete.delete()

            # Redirect the user to the items list
            return redirect('/manager/items/all/')

    context = {

    }
    return HttpResponse(template.render(context, request))
