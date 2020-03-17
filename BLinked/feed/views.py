from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    """
    renders the index page of feed

    :param request: request Object from Client
    :return: index page with multiple blogs
    """
    template = loader.get_template('feed/blog.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def blog(request, blogId):
    """
    renders the blog page with blog id = blogID

    :param request: request Object from Client
    :param blogId: id of the blog requested for
    :return: page of that specific blogID
    """
    template = loader.get_template('feed/single-blog.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
