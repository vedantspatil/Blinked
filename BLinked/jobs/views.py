from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    """
    renders the index page of job

    :param request: request Object from Client
    :return: index page with multiple jobs
    """
    template = loader.get_template('jobs/jobs.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def job(request, jobId):
    """
    renders the job page with job id = jobID

    :param request: request Object from Client
    :param jobId: id of the job requested for
    :return: page of that specific jobID
    """
    template = loader.get_template('jobs/job_details.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
