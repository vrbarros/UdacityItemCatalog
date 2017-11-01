from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    """First page from the app."""
    template = loader.get_template('manager/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
