from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    template = loader.get_template('contact/contact.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

